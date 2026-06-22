# Legacy Static Site Alignment Contract

Both the corporate and David sites use the same Portmason legacy static-site implementation.

## Common contract

- Shell `pm-setup` remains the orchestrator.
- The existing `stage_portmason` call inside `pm-setup` remains unconditional and authoritative.
- Project code does not introduce another staging command, staging policy, allowlist, or reduced runtime package.
- The native stage is the full Portmason share after the exclusions already supplied by `pm-setup`: `archive`, `cagent`, `*cosign*`, and `*log`.
- The native stage is written to the repository-root `portmason/` directory.
- Managed hosts invoke `pm-setup` from `PATH`; running it refreshes the full staged share before adapter and runtime setup/deployment.
- Isolated contexts such as GitHub Actions consume the committed repository-root stage because they do not inherit the managed host's Portmason installation or context.
- Containers receive the same staged share at `${CONTAINER_ROOT}/portmason` through an explicit bind mount.
- `RUNTIME_ADAPTER_CODE=static-local` is used for development.
- `RUNTIME_ADAPTER_CODE=static-github` is used for production.
- `www/` is the authoritative site source.
- `deploy/prd/` is the synchronized production workspace.
- `pm-sync-deploy-from-root` owns production snapshot refresh and drift detection.
- Static PM regions are rendered through the legacy static workflow and executable hooks.
- Portmason Collections uses the shared `_system` runtime, schemas, profiles, and renderer.
- Development uses shared Traefik ingress; production publishes `deploy/prd/www` to GitHub Pages.
- Compose bind mounts use long syntax so container targets never retain literal quote characters.
- The `solutions.etal.*` EPC label namespace is authoritative.

## Staging lifecycle

From a managed host:

```bash
bin/reconcile-portmason-stage
pm-setup
cd deploy/prd
pm-setup --refresh-from-root
cd ../..
```

`bin/reconcile-portmason-stage` only removes retired project-specific staging locations from the alignment work. It does not stage Portmason. The following `pm-setup` invocation performs staging through Portmason's existing native implementation.

Before synchronization, the repository-root `portmason/` stage is committed with the project so isolated runners receive the same share that the managed host staged.

No conditional staging rule is introduced at this time. That decision may be revisited with the Portmason Python refactor, but it is outside this legacy alignment.

Site-specific content, collection instances, CSS, domains, analytics identifiers, and scheduled content behavior remain intentional extension points.
