# Portmason Static Site Contract

David uses the current root-built Portmason static publication contract.

## Source and tooling

- `www/` is the authoritative site source and publication directory.
- `mgt-scripts/setup` is the application setup hook.
- `.portmason-tooling-ref` pins one tested commit from
  `domer6811/ops-and-sops`.
- GitHub Actions checks out only `ops/portmason` at that pinned revision.
- A committed project-local Portmason stage is not a publication dependency.
- `deploy/` is retained only as legacy compatibility state and is not read,
  refreshed, or uploaded by the current GitHub Pages workflow.

## Lifecycle

Local development starts at the repository root:

```bash
cd /home/davidomer/code/david
pm-setup
```

Production is built in GitHub Actions from a clean checkout of the same root.
The workflow:

1. reads and validates `.portmason-tooling-ref`;
2. checks out the pinned Portmason revision;
3. runs `pm-setup` from the project root with the official source commit,
   production environment, and deployment ID;
4. obtains the static publication directory from Portmason's resolved
   `SITE_DIR`;
5. uploads that directory to GitHub Pages;
6. finalizes the public hostname only after Pages reports a successful
   deployment.

Portmason renders managed partials, installs the local consent-gated GTM
capability through the application hook, and finalizes the official static
artifact before upload. The published artifact therefore includes verified
`build-info.json`, `deploy-info.json`, and `artifact-manifest.json` records.

Site content, collection instances, presentation, domains, and the public GTM
container ID remain project-owned configuration.
