# David Park Omer Portfolio

Static portfolio site rendered and deployed through legacy Portmason at the same operational level as the corporate site. The visual design and public content are intentionally unchanged.

## Quick start

From `/home/davidomer/code/david`:

```bash
pm-setup
```

The development site is served from `www/` through the shared Traefik installation at:

```text
https://david-dev.localtest.me
```

## Rendering model

```text
.env
  -> legacy pm-setup
  -> pm-deploy-static
  -> www/
```

The production snapshot uses `deploy/prd/.env` with `RUNTIME_ADAPTER_CODE=static-github` and is published by GitHub Pages from `deploy/prd/www`.

No Portmason Python-refactor orchestration is used. `pm-setup` remains the legacy shell orchestrator. Python utilities inside the static toolbox are limited to deterministic rendering and tests, matching the current corporate-site implementation pattern.

## Portmason Foundations

Two page areas are now backed by Portmason Collections™ Foundation objects:

```text
www/collections/case-studies/
www/collections/resumes/
```

Each collection owns its manifest, item registry, visibility, order, labels, links, and section presentation. Executable hooks under `www/partials/hooks/` render the Foundation data into the existing HTML classes.

The visible inventory remains unchanged:

- three published case-study cards;
- three published resume cards.

Additional existing case studies and resume files are registered with `published: false` so they are governed without appearing publicly.

## Editing

To change a case-study card, edit:

```text
www/collections/case-studies/items.json
```

To change a resume card or its visibility, edit:

```text
www/collections/resumes/items.json
```

Then run:

```bash
pm-setup
```

Do not hand-edit rendered HTML inside these marker regions:

```text
PM:COLLECTION-STYLES
PM:COLLECTION-CASE-STUDIES
PM:COLLECTION-RESUMES
```

## Tests

Tests run in the project toolbox container:

```bash
docker compose --profile tools run --rm --no-deps toolbox \
  python -m unittest discover -s tests -v
```

They verify Foundation integrity, referenced files, public inventory, collection rendering markers, and byte-identical legacy stylesheets.

## Production refresh

After local verification:

```bash
cd deploy/prd
pm-setup --refresh-from-root
```

This refreshes the production snapshot from the authoritative root and runs the legacy static GitHub adapter workflow.

## GitHub Pages cutover safety

The legacy root-level site files remain in the repository as a compatibility mirror during the Pages cutover. The active Portmason source and deployment artifact are `www/` and `deploy/prd/www/`; the new workflow publishes the latter through GitHub Pages Actions. This prevents the existing site from going blank before the repository's Pages source is switched to GitHub Actions.
