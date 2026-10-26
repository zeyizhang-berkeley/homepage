# zeyizhang-berkeley — Zeyi Zhang's academic homepage

A responsive, single-page academic homepage with a sticky profile and a persistent top navigation bar, compact Education/Experience entries, publication rows, research cards, a light/dark theme switch, and a link to view the current CV PDF. The portrait is intentionally a blank white square.

Target canonical URL: <https://zeyizhang-berkeley.github.io/homepage/>.

## Build

```sh
python3 build.py
```

The dependency-free Python build writes `dist/index.html`, assets, and compatibility redirects for the former `publications.html`, `research.html`, and `experience.html` pages. Content and navigation remain available without JavaScript.

## Edit

- Approved CV content: `data/profile.json` (initial extraction on October 23, 2026; summaries and source skills reconciled with the complete current `CV_v2/main.tex` on October 24, 2026).
- Page composition and content rendering: `build.py`.
- Visual styles and responsive layout: `assets/style.css`.
- Local theme preference and section tracking: `assets/site.js`.
- CV PDF: `assets/Zeyi_Zhang_CV.pdf`; replace and rebuild when the CV changes.

Publication order follows the current CV: works 1–7 under Publications and works 8–10 under Manuscripts. Submission and preparation status is explicit. Work 10 is a forthcoming Q-Chem manuscript announcement without an invented title or author list. Publication titles are plain text; links belong to citations or labeled resources. Paper2Bench has no invented demo URL. No private manuscript or Overleaf links are published.

## Design and provenance

About paragraphs are maintained in `profile.about_html`; `research_highlights` holds the cross-project research summaries. Experience and Software use specific, grammatical phrases corresponding to the CV points, with explicit relationships between methods, actions, and applications. Detailed results stay in the source records and CV. Summary review preserves exploratory MLDFT wording, the QH9-orbital/HELM-spectral distinction, and the distinction between MLFF-assisted geometry initialization and DFT molecular dynamics.

Experience entries show the organization, role, dates, and a compact sequence of specific phrases corresponding to the CV points. Research cards synthesize the complete CV into electronic structure and GPU computing, machine learning for quantum chemistry, and AI workflows and scientific reasoning. The “Tools I work with” block is omitted at the owner’s request; skills remain in the source data and CV. Software uses compact rows with the contribution role, project name, explicit [Code]/[Website] links, and a brief description; detailed project records remain in the source data and downloadable CV.

The visual reference is <https://onehfr.github.io/>: off-white background, Inter typography, a 264 px sidebar, 960 px main column, 56 px column gap, understated red accents, section rules, and rounded white cards. No reference-site biography, images, publications, or personal assets are reused. Below 860 px, the sidebar becomes a compact profile; the top navigation remains accessible through horizontal scrolling. The new homepage supersedes the previous separate-page design.

The section navigation follows the persistent top-bar structure of <https://hungqpham.com/> while retaining the homepage's Inter typography and colors. It appears above the profile and content, stays visible during scrolling, and highlights the current section. Navigation jumps directly to each section, and anchor offsets keep destination headings below the bar. The horizontally scrollable menu reveals the active item after page scrolling settles. Navigation and content share this order: About Me, Research Interest, Experience, Education, Software, Publications, Teaching, Mentorship. The former sidebar “On this page” menu is removed. Existing #about and #research links remain compatible.

The “View CV” button links directly to `assets/Zeyi_Zhang_CV.pdf` in a new tab, without an HTML download attribute, so the browser can display the PDF inline.

Inter is requested from Google Fonts with system-font fallbacks. There are no third-party scripts, analytics, or trackers. Theme preference stays in the visitor's browser.

The Education, Experience, and Publications layout follows the structural reference
<https://masterzhou1.github.io/>: institution logos beside the organization name,
degree/role and right-aligned dates underneath, and paper titles, authors, venue,
and resource links in lightly separated rows. The existing colors, sidebar, and
research content are retained. Institution marks are reused from the approved
CV assets, including the symbol-only Berkeley Lab mark. Education, Experience,
Software, Teaching, and Mentorship each place their main heading outside a
separate rounded content panel, matching Publications. Panel borders, background,
radius, and responsive horizontal padding use the same visual treatment;
subheadings and existing entry typography remain inside their panel.

Works 1–7 include concise, original summaries of their core methods or findings,
reviewed against the papers on October 25, 2026. They appear below the venue and inline resource links, following the publication-summary placement at
<https://masterzhou1.github.io/> while retaining this homepage's typography.
Edit each publication's `summary` in `data/profile.json` to revise this text.
Manuscripts 8–10 retain their existing descriptions and status. When a manuscript resource label already appears in its status, that text is linked directly instead of repeating a bracketed link after it.

The Software list follows the layout of <https://hungqpham.com/#software>: role in the left column, project name with explicit [Code] or [Website] links and a short description on the right, and thin dividers between rows. Typography retains this homepage’s original Inter font, heading weights, and body text styles; the reference is used for layout only. Entries come from this profile’s existing projects, grouped into Scientific packages and AI4Science. DTCS-v.02 is listed among Scientific packages. RSI for Science replaces Paper2Bench in the visible list, with the Contributor role and a link to its project website. Developer/Contributor labels reflect the existing CV and the owner’s explicit instructions; no leadership claim is inferred. Project names are plain text; resource labels carry the hyperlinks. DTCS-v.02 keeps [v.01 Code] and [v.01 Paper] beside its name, clearly identifying them as v.01 resources. Detailed Paper2Bench source records remain available for future use but are not displayed on the homepage.

Experience and Software were reconciled against the complete current CV on October 25, 2026. At the owner's request, each CV point has a specific short phrase on the homepage rather than a broad category label: for example, THC methods, AFQMC reference data, and exploratory MLDFT training remain distinct. Experience phrases follow the CV order, including nested research points; Software descriptions identify each project's relevant methods or purpose. Numerical results, hardware/model names, and procedural detail remain in the CV. All eleven Software entries, roles, project order, and explicit resource links are retained. Paper2Bench remains unnamed on the homepage as previously requested; its scientific-benchmark work is summarized without exposing the project name.

Publication figures follow the owner's selections on October 25, 2026. They appear
beside each paper and enlarge in an on-page modal when clicked, with intrinsic dimensions,
accessible descriptions, lazy loading, and responsive stacking on small screens.
Publication rows retain the original Inter family, font weights, and line heights. Font sizes are compacted: titles are 16 px and authors, citations, summaries, and resource links are 12.8 px, following the reference site's smaller supporting text.
The image viewer closes with its Close button, Escape, or a backdrop click. It
keeps keyboard focus inside while open, locks background scrolling, and restores
the original reading position and thumbnail focus on close. CSS and JavaScript
URLs include content hashes so updates do not reuse stale browser assets.
The main column is widened to 960 px. Publication figures occupy 36% of each two-column row, with a 280 px height limit and their original aspect ratios. Small screens stack figures above text, with previews up to 360 px wide. Paper and related links follow the venue or submission status inline, separated by 12 px, and wrap naturally when needed. Previews remain in the publication list. The modal loads each available
vector or higher-resolution original only when opened. MolP2SBench and OPSD use
SVGs that preserve vector text and geometry (with source raster artwork or
converted gradient fragments where necessary). The three Visual Abstracts and
the review composition use higher-resolution publisher originals; these remain
raster artwork. The JACS Figure 1 is already the original 1500 × 883 raster from
the published PDF. Quality details are recorded alongside each source entry.

| Work | Selected image |
| --- | --- |
| MolP2SBench | Figure 1 from the original arXiv HTML asset |
| On Policy Self Distillation | Figure 1 from the supplied manuscript PDF |
| PARSEC.py | Publisher Visual Abstract from the Real-space KS-DFT review |
| Ionization-Driven Oxygen–Oxygen Bond Formation | Figure 1 from the published PDF |
| ROKS-EDA | Publisher Visual Abstract |
| Improved Charge-transfer Guess | Publisher Visual Abstract |
| Real-space KS-DFT review | Figures 6, 8 and 9, arranged together in one SVG |

Original scientific content is preserved. The review composition embeds the
unchanged source JPEGs with white spacing and no visible figure-number labels. All three Visual Abstracts are the actual publisher PNG assets, downloaded and
visually checked through the article pages. As explicitly requested, PARSEC.py
uses the review's Visual Abstract; the review itself uses Figures 6, 8 and 9.
Source URLs, extraction details, figure licenses where documented, and hashes
are recorded in `assets/papers/sources.json`. Manuscripts 8–10 have no images.

## GitHub Pages

Repository: `zeyizhang-berkeley/homepage`.

In Settings → Pages → Build and deployment → Source, select **GitHub Actions**.
The generated homepage is served at <https://zeyizhang-berkeley.github.io/homepage/>.

### Edit in the browser

1. Open <https://vscode.dev/github/zeyizhang-berkeley/homepage>.
2. Edit `data/profile.json` and save. Use `profile.about_html` for About Me and
   `research_highlights` for the Research Interest cards. Update the source
   fields rather than generated `docs/index.html`.
3. In Source Control, commit and push to `main`.
4. Open the repository's **Actions** tab and wait for **Build and deploy homepage**
   to finish successfully, then refresh the homepage.

`.github/workflows/pages.yml` builds the current source and deploys `dist/` on
every push to `main`. Changes to content, styles, images, and the CV are included.
The workflow also supports **Run workflow** from the Actions tab. Saving in
vscode.dev without committing and pushing does not publish the change.

### Local preview and optional generated snapshot

Run `python3 build.py` and open `dist/index.html` for a local preview.
To also refresh the optional `docs/` snapshot, run:

```sh
python3 publish.py
```

Commit the source changes and push `main`; the workflow generates the deployed
HTML automatically. `docs/` is a retained snapshot, not the live publishing source.
No external Python dependencies, personal access tokens, or paid hosting are needed.
