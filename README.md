# zeyizhang-berkeley — Zeyi Zhang's academic homepage

A responsive, single-page academic homepage with a sticky profile and section navigation, compact Education/Experience entries, publication rows, research cards, a light/dark theme switch, and the current CV download. The portrait is intentionally a blank white square.

Target canonical URL: <https://zeyizhang-berkeley.github.io/>.

## Build

```sh
python3 build.py
```

The dependency-free Python build writes `dist/index.html`, assets, and compatibility redirects for the former `publications.html`, `research.html`, and `experience.html` pages. Content and navigation remain available without JavaScript.

## Edit

- Approved CV content: `data/profile.json` (extracted from `CV_v2/main.tex` on October 23, 2026).
- Page composition and content rendering: `build.py`.
- Visual styles and responsive layout: `assets/style.css`.
- Local theme preference and section tracking: `assets/site.js`.
- Downloadable CV: `assets/Zeyi_Zhang_CV.pdf`; replace and rebuild when the CV changes.

Publication order follows the current CV: works 1–7 under Publications and works 8–10 under Manuscripts. Submission and preparation status is explicit. Work 10 is a forthcoming Q-Chem manuscript announcement without an invented title or author list. Publication titles are plain text; links belong to citations or labeled resources. Paper2Bench has no invented demo URL. No private manuscript or Overleaf links are published.

## Design and provenance

The visual reference is <https://onehfr.github.io/>: off-white background, Inter typography, a 264 px sidebar, 760 px main column, 56 px column gap, understated red accents, section rules, and rounded white cards. No reference-site biography, images, publications, or personal assets are reused. Below 860 px, the sidebar becomes a compact profile with a sticky, horizontally scrollable section menu. The new homepage supersedes the previous separate-page design.

Inter is requested from Google Fonts with system-font fallbacks. There are no third-party scripts, analytics, or trackers. Theme preference stays in the visitor's browser.

The Education, Experience, and Publications layout follows the structural reference
<https://masterzhou1.github.io/>: institution logos beside the organization name,
degree/role and right-aligned dates underneath, and paper titles, authors, venue,
and resource links in lightly separated rows. The existing colors, sidebar, and
research content are retained. Institution marks are reused from the approved
CV assets, including the symbol-only Berkeley Lab mark.

Publication figures are intentionally deferred until the owner selects the exact
figure from each paper. A publication may then receive an `image` object in
`data/profile.json`, for example `{"src":"assets/papers/selected-figure.png",
"alt":"Description of the selected figure"}`. This enables the left-image,
right-text layout automatically. No speculative or placeholder paper image is
displayed in the meantime.

## GitHub Pages

Repository: `zeyizhang-berkeley/zeyizhang-berkeley.github.io`.

In Settings → Pages, select **Deploy from a branch**, **main**, **/docs**.
The generated homepage is served at <https://zeyizhang-berkeley.github.io/>.

After editing content, styles, figures, or the CV, run:

```sh
python3 publish.py
```

Commit the source changes and updated `docs/` together, then push `main`.
No external build dependencies, secrets, or paid hosting are needed.
