# Portfolio (static site)

This project is plain HTML plus assets under `static/`. Open **`index.html`** or deploy the repository root as a static site (GitHub Pages, Netlify, Cloudflare Pages, S3 + CloudFront, etc.).

## Local preview

Browser security rules can limit some resources when loading pages from `file://`. Serving the folder over HTTP avoids that—for example:

```bash
npx --yes serve .
```

Or use any editor “Live Preview” extension, VS Code Live Server, or another static-file server pointing at this directory.

The published site does not rely on Python, Node.js, or any build step unless you choose a tool purely for preview.
