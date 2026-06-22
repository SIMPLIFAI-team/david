# David Park Omer Portfolio — Static CMS Version

This version keeps GitHub Pages hosting simple while making the portfolio case studies editable like a lightweight CMS.

## Files

- `index.html` — main resume / portfolio page
- `content/case-studies.json` — homepage portfolio card content
- `case-studies/*.html` — static detail pages for each case study
- `.env` — operator-side Portmason configuration for the selected environment
- `.env.example` — safe development example
- `.env.generated` — rendered dotenv output generated from `.env`
- `config.generated.json` — browser-safe generated config consumed by the static site
- `assets/js/site-config.js` — loads browser-safe config and installs analytics when configured

## Configuration workflow

The website should not read `.env` directly in the browser. Portmason owns the environment-specific workflow:

```text
selected env file
  ↓
pm-setup
  ↓
environment-specific runtime adapter
  ↓
config.generated.json
  ↓
static website
```

Adapters are environment-specific. For example, DEV, QAS, and PRD may use different `RUNTIME_ADAPTER_CODE` values in their own env files. `pm-setup` should run the appropriate provision, deploy, configure, and related workflow for the selected environment.

For this GitHub Pages static deployment, the production `.env` uses:

```env
RUNTIME_ADAPTER_CODE=static-github
```

Analytics values such as `GTM_CONTAINER_ID` are rendered into `config.generated.json`. They are intentionally not hard-coded in the HTML.

## Editing workflow

1. Edit `content/case-studies.json` to change titles, summaries, tags, card bullets, or URLs.
2. Edit the matching file in `case-studies/` when a full case-study page needs richer content.
3. Update the environment file when configuration changes are needed.
4. Run Portmason setup/deploy for the selected environment.
5. Commit and push to GitHub.
6. GitHub Pages serves the updated static site.

## Local preview

Because the homepage uses `fetch()` to load JSON files, preview through a local web server instead of double-clicking the file.

```bash
python3 -m http.server 8080
```

Then open:

```text
http://localhost:8080
```

## Verification

After Portmason renders configuration, confirm these files exist and contain expected non-secret values:

```bash
test -f .env.generated
test -f config.generated.json
python3 -m json.tool config.generated.json >/dev/null
```

Then preview locally and confirm the page loads without console errors.

## Privacy note

All case studies are generalized and anonymized. Do not add proprietary code, client data, screenshots, confidential architecture diagrams, or implementation details.

## Portmason static partials

This site uses Portmason-managed static partial regions for repeated HTML.

- `partials/home-header.html` renders the home page navigation.
- `partials/case-header.html` renders case-study navigation.
- `partials/footer.html` renders the shared footer.
- Pages keep managed regions with `<!-- PM:NAME -->` and `<!-- /PM:NAME -->` markers.
- `portmason/pm-deploy-static` refreshes those regions before the static GitHub Pages deployment path runs.

Do not hand-edit rendered content inside a PM marker block. Edit the matching file in `partials/` and run `portmason/pm-setup`.

## Fixed Footer Behavior

The shared footer is rendered from `partials/footer.html` and is kept visible with CSS in:

- `assets/css/styles.css`
- `assets/css/case-study.css`

The footer uses `position: fixed` with `--footer-h` and matching bottom padding on the document so page content does not sit underneath it.
