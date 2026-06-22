# David Park Omer Portfolio

Static portfolio site rendered and deployed through the same legacy Portmason contract as the corporate site. The visual design and public content remain unchanged.

## Canonical structure

```text
www/                    authoritative site source
deploy/prd/             synchronized production workspace
www/collections/        Portmason Collections Foundation objects
www/partials/hooks/     executable static render hooks
```

Development uses `RUNTIME_ADAPTER_CODE=static-local`; production uses `static-github`. Shell `pm-setup` remains the orchestrator. The Portmason Python refactor is not used.

## Apply and verify

```bash
pm-setup
tests/verify-compose-contract
tests/verify-production-entrypoints
tests/verify-portmason-alignment
docker compose --profile tools run --rm --no-deps toolbox \
  python -m unittest discover -s tests -v
```

The development site is available through the shared Traefik installation at `https://david-dev.localtest.me`.

## Foundations

Case studies and targeted resumes use the same shared Collections `_system` runtime as corp-www. Both are noninteractive `catalog` instances using the `card-grid` layout, which preserves the existing David-site markup and CSS classes.

Edit collection data under:

```text
www/collections/case-studies/
www/collections/resumes/
```

Then run `pm-setup`. Do not hand-edit generated PM regions in `www/index.html`.

## Production refresh

```bash
cd deploy/prd
pm-setup --refresh-from-root
```

## Legacy root cleanup

After the GitHub Pages Actions deployment is verified, remove the obsolete root-level mirror repeatably with:

```bash
bin/cleanup-root
```

The full shared contract is documented in `docs/PORTMASON_SITE_ALIGNMENT.md`.
