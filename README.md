# David Park Omer Portfolio

Static portfolio site rendered and deployed through the same legacy Portmason contract as the corporate site. The visual design and public content remain unchanged.

## Canonical structure

```text
www/                    authoritative site source
deploy/prd/             synchronized production workspace
portmason/              full native stage created by pm-setup
www/collections/        Portmason Collections Foundation objects
www/partials/hooks/     executable static render hooks
```

Development uses `RUNTIME_ADAPTER_CODE=static-local`; production uses `static-github`. Shell `pm-setup` remains the orchestrator. Its existing unconditional `stage_portmason` call stages the full legacy share before runtime and adapter work. No project-specific staging implementation is used, and the Portmason Python refactor is not used.

## Apply and verify

```bash
bin/reconcile-portmason-stage
pm-setup

bash tests/verify-compose-contract
bash tests/verify-production-entrypoints
bash tests/verify-portmason-alignment
bash tests/verify-portmason-shared-contract

docker compose --profile tools run --rm --no-deps toolbox \
  python -m unittest discover -s tests -v
```

The development site is available through the shared Traefik installation at `https://david-dev.localtest.me`.

## Foundations

Case studies and targeted resumes use the same shared Collections `_system` runtime as corp-www. Both are noninteractive `catalog` instances using the `card-grid` layout, preserving the existing markup and CSS classes.

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
cd ../..
```

The native setup refreshes the repository-root `portmason/` stage. GitHub Actions mounts and consumes that committed full share.

## GitHub Pages root compatibility

`www/` remains authoritative. Until the repository is confirmed to be served exclusively from the Pages Actions artifact, refresh the repository-root compatibility mirror before syncing:

```bash
bin/sync-pages-root
```

The mirror prevents a branch-based Pages configuration from serving stale HTML without its CSS, Collections assets, or current CSP. The standard Pages workflow still publishes `deploy/prd/www`.
