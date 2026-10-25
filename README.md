# zeyizhang-berkeley — Zeyi Zhang's academic homepage

A responsive, single-page academic homepage with a sticky profile and section navigation, compact Education/Experience entries, publication rows, research cards, a light/dark theme switch, and the current CV download. The portrait is intentionally a blank white square.

Target canonical URL: <https://zeyizhang-berkeley.github.io/homepage/>.

## Build

```sh
python3 build.py
```

The dependency-free Python build writes `dist/index.html`, assets, and compatibility redirects for the former `publications.html`, `research.html`, and `experience.html` pages. Content and navigation remain available without JavaScript.

## Edit

- Approved CV content: `data/profile.json` (initial extraction on October 23, 2026; summaries and toolkit reconciled with the complete current `CV_v2/main.tex` on October 24, 2026).
- Page composition and content rendering: `build.py`.
- Visual styles and responsive layout: `assets/style.css`.
- Local theme preference and section tracking: `assets/site.js`.
- Downloadable CV: `assets/Zeyi_Zhang_CV.pdf`; replace and rebuild when the CV changes.

Publication order follows the current CV: works 1–7 under Publications and works 8–10 under Manuscripts. Submission and preparation status is explicit. Work 10 is a forthcoming Q-Chem manuscript announcement without an invented title or author list. Publication titles are plain text; links belong to citations or labeled resources. Paper2Bench has no invented demo URL. No private manuscript or Overleaf links are published.

## Design and provenance

About paragraphs are maintained in `profile.about_html`; `research_highlights` holds the cross-project research summaries. Experience and Software keep one short summary per entry. Detailed results stay in the source records and CV. Summary review preserves exploratory MLDFT wording, the QH9-orbital/HELM-spectral distinction, and the distinction between MLFF-assisted geometry initialization and DFT molecular dynamics.

Experience entries show the organization, role, dates, and one sentence about the work. Research cards synthesize the complete CV into electronic structure and GPU computing, machine learning for quantum chemistry, and AI workflows and scientific reasoning. Software uses compact rows with the contribution role, linked project name, and one-line description; detailed project records remain in the source data and downloadable CV.

The visual reference is <https://onehfr.github.io/>: off-white background, Inter typography, a 264 px sidebar, 960 px main column, 56 px column gap, understated red accents, section rules, and rounded white cards. No reference-site biography, images, publications, or personal assets are reused. Below 860 px, the sidebar becomes a compact profile with a sticky, horizontally scrollable section menu. The new homepage supersedes the previous separate-page design.

Inter is requested from Google Fonts with system-font fallbacks. There are no third-party scripts, analytics, or trackers. Theme preference stays in the visitor's browser.

The Education, Experience, and Publications layout follows the structural reference
<https://masterzhou1.github.io/>: institution logos beside the organization name,
degree/role and right-aligned dates underneath, and paper titles, authors, venue,
and resource links in lightly separated rows. The existing colors, sidebar, and
research content are retained. Institution marks are reused from the approved
CV assets, including the symbol-only Berkeley Lab mark.

Works 1–7 include concise, original summaries of their core methods or findings,
reviewed against the papers on October 25, 2026. They appear below the venue and inline resource links, following the publication-summary placement at
<https://masterzhou1.github.io/> while retaining this homepage's typography.
Edit each publication's `summary` in `data/profile.json` to revise this text.
Manuscripts 8–10 retain their existing descriptions and status.

The Software list follows the layout of <https://hungqpham.com/#software>: role in the left column, project name and short description on the right, and thin dividers between rows. Typography retains this homepage’s original Inter font, heading weights, and body text styles; the reference is used for layout only. Entries come from this profile’s existing projects, grouped into Scientific packages and AI tools & benchmarks. Developer/Contributor labels reflect the existing CV; no leadership claim is inferred. DTCS-v.02 links are explicitly labeled as v.01 resources, and Paper2Bench has no invented public link.

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

In Settings → Pages, select **Deploy from a branch**, **main**, **/docs**.
The generated homepage is served at <https://zeyizhang-berkeley.github.io/homepage/>.

After editing content, styles, figures, or the CV, run:

```sh
python3 publish.py
```

Commit the source changes and updated `docs/` together, then push `main`.
No external build dependencies, secrets, or paid hosting are needed.
