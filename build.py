"""Build the academic homepage: python3 build.py (standard library only)."""
from pathlib import Path
from html import escape
import json
import shutil
import hashlib

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'dist'
DATA = json.loads((ROOT / 'data/profile.json').read_text())
SITE_URL = 'https://zeyizhang-berkeley.github.io/homepage/'
NAV = [('about', 'About'), ('education', 'Education'), ('experience', 'Experience'), ('publications', 'Publications'), ('research', 'Research'), ('software', 'Software'), ('teaching', 'Teaching'), ('mentorship', 'Mentorship')]

def e(value):
    return escape(str(value), quote=True)

def asset_url(path):
    version = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()[:12]
    return path + '?v=' + version

def link(url, text, cls='', download=False):
    attrs = ' class="' + e(cls) + '"' if cls else ''
    if download:
        attrs += ' download'
    elif url.startswith(('https://', 'http://')):
        attrs += ' target="_blank" rel="noopener noreferrer"'
    return '<a href="' + e(url) + '"' + attrs + '>' + text + '</a>'

ICONS = {
    'Email': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',
    'GitHub': '<path d="M9 19c-4 1-4-2-6-2m12 5v-4c0-1-.3-2-1-2.5 3-.3 6-1.5 6-6.5 0-1.5-.5-2.5-1.5-3.5.5-1 .5-2.5 0-3.5-2-.5-3.5 1-4 1-2-.5-4-.5-6 0-.5 0-2-1.5-4-1-.5 1-.5 2.5 0 3.5C3.5 6.5 3 7.5 3 9c0 5 3 6.2 6 6.5-.7.5-1 1.5-1 2.5v4"/>',
    'Google Scholar': '<path d="m2 9 10-6 10 6-10 6-10-6Z"/><path d="M6 12v6c4 3 8 3 12 0v-6M22 9v8"/>',
    'OpenReview': '<path d="M4 3h13l3 3v15H4V3Z"/><path d="M16 3v5h4M8 12h8M8 16h6"/>',
    'ORCID': '<circle cx="12" cy="12" r="9"/><path d="M8 10v7m0-10v.1M12 7h2a5 5 0 0 1 0 10h-2V7Z"/>',
    'LinkedIn': '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 10v7m0-10v.1M11 17v-7m0 3a3 3 0 0 1 6 0v4"/>',
    'CV': '<path d="M14 2H5v20h14V7l-5-5Z"/><path d="M14 2v6h5M8 12h8M8 16h8"/>',
    'Theme': '<path d="M20.5 13a8.7 8.7 0 0 1-9.5-9.5A9 9 0 1 0 20.5 13Z"/>',
    'Arrow': '<path d="M7 17 17 7M7 7h10v10"/>',
}

def icon(name):
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + ICONS[name] + '</svg>'

def chips(items):
    items = [x for x in items if x.get('url')]
    return '<div class="chips">' + ''.join(link(x['url'], e(x['label']) + icon('Arrow'), 'chip') for x in items) + '</div>' if items else ''

def people(items):
    return ', '.join(link(p['url'], e(p.get('title', '') + ' ' + p['name']), 'person') if p.get('url') else e(p['name']) for p in items)

def pubrefs(numbers):
    return '<span class="paper-refs">' + ' '.join(link('#paper-' + str(n), '[' + str(n) + ']') for n in numbers) + '</span>' if numbers else ''

def section(id_, title, body, note='', cls='', panel=False):
    note_html = '<p class="section__note">' + note + '</p>' if note else ''
    if panel:
        body = '<div class="section-panel">' + body + '</div>'
    return '<section class="section ' + cls + '" id="' + id_ + '" aria-labelledby="' + id_ + '-title"><div class="section__head"><h2 id="' + id_ + '-title">' + title + '</h2>' + note_html + '</div>' + body + '</section>'

def publication(p):
    authors = ', '.join(('<strong>' + e(a['name']) + '</strong>' if a['is_self'] else e(a['name'])) + ('<sup>*</sup>' if a['equal_contribution'] else '') for a in (p.get('authors') or []))
    title = '<h3>' + e(p['title']) + '</h3>' if p.get('title') else '<p class="announcement">' + e(p['description']) + '</p>'
    citation = e(p['status'] if p['number'] == 10 else p['citation'])
    resource_links = []
    for resource in p.get('links', []):
        url = resource['url']
        if p['section'] == 'Manuscripts' and resource['label'] and e(resource['label']) in citation:
            citation = citation.replace(e(resource['label']), link(url, e(resource['label'])), 1)
            continue
        label = ('arXiv' if 'arxiv.org/' in url else
                 'OpenReview' if 'openreview.net/' in url else
                 'Paper' if 'doi.org/' in url else resource['label'])
        resource_links.append(link(url, '[' + e(label) + ']'))
    resources = ' <span class="pub__resources">' + ' '.join(resource_links) + '</span>' if resource_links else ''
    summary = '<p class="pub__summary">' + e(p['summary']) + '</p>' if p.get('summary') else ''
    # Only render a figure after the user has selected an image from the paper.
    figure = p.get('image')
    figure_html = ''
    if figure:
        full_src = figure.get('full_src', figure['src'])
        figure_html = '<figure class="pub__figure"><button class="pub__figure-link" type="button" data-figure-src="' + e(full_src) + '" aria-haspopup="dialog" aria-controls="figure-lightbox" title="Enlarge figure" aria-label="Enlarge figure for ' + e(p['title']) + '"><img src="' + e(figure['src']) + '" alt="' + e(figure['alt']) + '" width="' + e(figure['width']) + '" height="' + e(figure['height']) + '" loading="lazy" decoding="async"></button></figure>'
    cls = 'pub pub--with-figure' if figure else 'pub'
    return '<article class="' + cls + '" id="paper-' + str(p['number']) + '" aria-label="Work ' + str(p['number']) + '">' + figure_html + '<div class="pub__body">' + title + ('<p class="pub__authors">' + authors + '</p>' if authors else '') + '<p class="pub__citation">' + citation + resources + '</p>' + summary + '</div></article>'

INSTITUTION_LOGOS = {
    'berkeley': 'berkeley.png',
    'lbnl': 'berkeley-lab.png',
    'sjtu': 'sjtu.png',
    'bytedance': 'bytedance.png',
    'qchem': 'qchem.png',
    'nyu-ecnu': 'nyu-shanghai.png',
}

def institution_logo(key):
    return '<div class="affiliation__logo"><img src="assets/institutions/' + INSTITUTION_LOGOS[key] + '" alt="" width="24" height="24" loading="lazy" decoding="async"></div>'

def project_card(p, id_, label='', wide=False):
    summary = p.get('homepage_summary', p['summary'])
    title = p.get('homepage_title', p['name'])
    references = list(p.get('publication_numbers', []))
    for detail in p.get('details', []) + p.get('subprojects', []):
        references.extend(detail.get('publication_numbers', []))
    references = sorted(set(references))
    resources = p.get('homepage_links', p.get('links', []))
    label_html = '<p class="project__label">' + e(label) + '</p>' if label else ''
    return '<article class="project' + (' project--wide' if wide else '') + '" id="' + id_ + '">' + label_html + '<h3>' + e(title) + '</h3><p>' + e(summary) + pubrefs(references) + '</p>' + chips(resources) + '</article>'

def build_research():
    cards = ''.join(project_card(p, p['id'], p['label'], p.get('wide', False)) for p in DATA['research_highlights'])
    skills = DATA['skills']
    labels = [('programming_languages', 'Programming'), ('scientific_computing_and_ml_frameworks', 'Scientific computing & ML'), ('simulation_software', 'Simulation software'), ('coding_agents', 'Coding agents')]
    skill_html = '<div class="toolkit"><h3>Tools I work with</h3><dl>' + ''.join('<div><dt>' + e(label) + '</dt><dd>' + e(', '.join(skills[key])) + '</dd></div>' for key, label in labels) + '</dl></div>'
    return '<div class="projects">' + cards + '</div>' + skill_html

def build_software():
    groups = []
    for group in DATA['software_groups']:
        rows = []
        for item in group['items']:
            name = e(item['name'])
            role_class = ' software__role--developer' if item['role'] == 'Developer' else ''
            resources = list(item.get('links', []))
            if item.get('url'):
                label = 'Code' if item['url'].startswith('https://github.com/') else 'Website'
                resources.insert(0, {'url': item['url'], 'label': label})
            links_html = ' <span class="software__resources">' + ' '.join(link(r['url'], '[' + e(r['label']) + ']') for r in resources) + '</span>' if resources else ''
            rows.append('<li class="software__item" id="' + e(item['id']) + '"><p class="software__role' + role_class + '">' + e(item['role']) + '</p><div class="software__body"><h4>' + name + links_html + '</h4><p class="software__description">' + e(item['summary']) + '</p></div></li>')
        groups.append('<div class="software-group" id="' + e(group['id']) + '"><h3>' + e(group['title']) + '</h3><ol class="software-list">' + ''.join(rows) + '</ol></div>')
    return ''.join(groups)

def build_experience():
    rows = []
    for x in DATA['experience']:
        org = link(x['organization_url'], e(x['organization'])) if x.get('organization_url') else e(x['organization'])
        summary = '<p class="exp__summary">' + e(x['homepage_summary']) + '</p>' if x.get('homepage_summary') else ''
        rows.append('<li class="affiliation" id="' + e(x['id']) + '">' + institution_logo(x['id']) + '<div class="affiliation__body"><h3>' + org + '</h3><div class="affiliation__role-date"><p class="exp__role">' + e(x['role']) + '</p><p class="exp__date">' + e(x['dates']) + '</p></div>' + summary + '</div></li>')
    return '<ol class="affiliations">' + ''.join(rows) + '</ol>'

def build_education():
    rows = []
    for x in DATA['education']:
        extra = '<p class="exp__meta">Advisors: ' + people(x['advisors']) + '</p>' if x.get('advisors') else ''
        if x.get('program'):
            extra += '<p class="exp__meta">' + link(x['program_url'], e(x['program'])) + ' · GPA ' + e(x['gpa']) + '</p>'
        if x.get('scholarships'):
            awards = ', '.join(link(a['url'], e(a['name'])) if a.get('url') else e(a['name']) for a in x['scholarships'])
            extra += '<p class="exp__meta">' + awards + '</p>'
        key = 'berkeley' if 'Berkeley' in x['institution'] else 'sjtu'
        rows.append('<li class="affiliation">' + institution_logo(key) + '<div class="affiliation__body"><h3>' + e(x['institution']) + '</h3><div class="affiliation__role-date"><p class="exp__role">' + e(x['degree']) + '</p><p class="exp__date">' + e(x['dates']) + '</p></div>' + extra + '</div></li>')
    return '<ol class="affiliations">' + ''.join(rows) + '</ol>'

def build_teaching():
    groups = []
    for x in DATA['teaching']:
        courses = ''.join('<li><div><strong>' + e(c['code']) + '</strong><span>' + e(c['name']) + '</span></div><span class="exp__date">' + e(c['dates']) + '</span></li>' for c in x['courses'])
        groups.append('<div class="teaching-group"><h3>' + e(x['institution']) + '</h3><p class="exp__role">' + e(x['role']) + '</p><ul class="courses">' + courses + '</ul></div>')
    return ''.join(groups)

def build_mentorship():
    rows = []
    for x in DATA['mentorship']:
        current = ''
        if x.get('current_role'):
            current = '<p class="mentee__now">Now: ' + e(x['current_role']) + ', ' + e(x['current_institution'])
            if x.get('current_group'):
                current += ' · ' + e(x['current_group'])
            current += '</p>'
        rows.append('<li><h3>' + e(x['name']) + '</h3><p class="exp__meta">' + e(x['mentee_role']) + ' · ' + e(x['mentee_institution']) + '</p>' + current + '</li>')
    return '<ul class="mentees">' + ''.join(rows) + '</ul>'

def build():
    OUT.mkdir(exist_ok=True)
    if not (ROOT / 'assets/Zeyi_Zhang_CV.pdf').exists():
        raise FileNotFoundError('Place the current CV at assets/Zeyi_Zhang_CV.pdf.')
    links = [x for x in DATA['profile']['links'] if x['label'] != 'LinkedIn']
    links.insert(3, {'label': 'OpenReview', 'url': 'https://openreview.net/profile?id=~Zeyi_Zhang3'})
    links += [x for x in DATA['profile']['links'] if x['label'] == 'LinkedIn']
    social = ''.join('<li>' + link(x['url'], icon(x['label']) + e(x['label'])) + '</li>' for x in links)
    nav = ''.join('<li>' + link('#' + id_, e(label), 'is-active' if id_ == 'about' else '') + '</li>' for id_, label in NAV)
    # Trusted, author-edited paragraph markup keeps the displayed biography in the profile data.
    intro = ''.join('<p>' + paragraph + '</p>' for paragraph in DATA['profile']['about_html'])
    pubs = '<div class="pubs">' + ''.join(publication(p) for p in DATA['publications'] if p['section'] == 'Publications') + '</div>'
    pubs += '<div class="subsection__head" id="manuscripts"><h3>Manuscripts</h3><p>Submitted, in preparation, and forthcoming</p></div><div class="pubs">' + ''.join(publication(p) for p in DATA['publications'] if p['section'] == 'Manuscripts') + '</div>'
    body = section('about', 'About', intro, cls='intro')
    body += section('education', 'Education', build_education(), panel=True)
    body += section('experience', 'Experience', build_experience(), panel=True)
    body += section('publications', 'Publications', pubs, '* Equal contribution')
    body += section('research', 'Research', build_research())
    body += section('software', 'Software', build_software(), panel=True)
    body += section('teaching', 'Teaching', build_teaching(), panel=True)
    body += section('mentorship', 'Mentorship', build_mentorship(), panel=True)
    html = '''<!doctype html><html lang="en" data-theme="light"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>zeyizhang-berkeley | Zeyi Zhang</title>
<meta name="description" content="Zeyi Zhang is a UC Berkeley chemistry Ph.D. candidate developing electronic-structure methods, GPU simulation software, and AI tools for molecular and materials research.">
<meta name="theme-color" content="#fafaf8"><meta name="color-scheme" content="light dark">
<meta property="og:title" content="zeyizhang-berkeley | Zeyi Zhang"><meta property="og:type" content="website">
<meta property="og:site_name" content="zeyizhang-berkeley"><meta property="og:url" content="https://zeyizhang-berkeley.github.io/homepage/">
<link rel="canonical" href="https://zeyizhang-berkeley.github.io/homepage/">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<script>try{const t=localStorage.getItem('zeyi-theme');document.documentElement.dataset.theme=t==='dark'?'dark':'light';}catch(e){}</script>
<link rel="stylesheet" href="assets/style.css"><script src="assets/site.js" defer></script>
</head><body><a class="skip-link" href="#main">Skip to content</a><div class="shell"><aside class="side" aria-label="Profile and navigation">
<div class="profile"><div class="profile__avatar" role="img" aria-label="Portrait placeholder"></div><div class="profile__identity"><h1 class="profile__name">Zeyi Zhang</h1><p class="profile__tagline">Ph.D. Candidate in Chemistry<br>University of California, Berkeley<br>Lawrence Berkeley National Laboratory</p></div></div>
<p class="profile__location">Berkeley, California</p><ul class="links" aria-label="Contact and academic profiles">''' + social + '</ul>' + link('assets/Zeyi_Zhang_CV.pdf', icon('CV') + 'Download CV', 'cv-link', download=True) + '<nav class="toc" aria-label="On this page"><p class="toc__label">On this page</p><ol class="toc__list">' + nav + '</ol></nav><button class="theme-toggle" type="button" aria-pressed="false" aria-label="Switch to dark theme" hidden>' + icon('Theme') + '<span>Dark theme</span></button></aside><main class="main" id="main">' + body + '<footer class="foot"><span>© 2026 Zeyi Zhang</span><a href="#about">Back to top ↑</a></footer></main></div></body></html>'
    viewer = '<dialog class="figure-viewer" id="figure-lightbox" aria-label="Enlarged publication figure"><div class="figure-viewer__panel"><div class="figure-viewer__toolbar"><button class="figure-viewer__close" type="button" aria-label="Close enlarged figure" autofocus><span aria-hidden="true">×</span> Close</button></div><img class="figure-viewer__image" alt=""></div></dialog>'
    html = html.replace('</body>', viewer + '</body>')
    html = html.replace('href="assets/style.css"', 'href="' + asset_url('assets/style.css') + '"')
    html = html.replace('src="assets/site.js"', 'src="' + asset_url('assets/site.js') + '"')
    (OUT / 'index.html').write_text(html)
    (OUT / '.nojekyll').write_text('')
    (OUT / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: ' + SITE_URL + 'sitemap.xml\n')
    (OUT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>' + SITE_URL + '</loc></url></urlset>')
    aliases = {'q-chem': 'qchem-software', 'real-space': 'parsec-software', 'ecnu': 'nyu-ecnu'}
    for filename, target in [('publications.html', 'publications'), ('research.html', 'research'), ('experience.html', 'experience')]:
        url = 'index.html#' + target
        script = 'const aliases=' + json.dumps(aliases) + ";const old=location.hash.slice(1);location.replace('index.html#'+(aliases[old]||old||'" + target + "'));"
        (OUT / filename).write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="refresh" content="0;url=' + url + '"><title>Continue to Zeyi Zhang’s homepage</title></head><body><p>This page has moved. <a href="' + url + '">Continue to ' + target + '</a>.</p><script>' + script + '</script></body></html>')
    shutil.copytree(ROOT / 'assets', OUT / 'assets', dirs_exist_ok=True)
    print('Built homepage, 3 compatibility redirects, and assets in ' + str(OUT))

if __name__ == '__main__':
    build()
