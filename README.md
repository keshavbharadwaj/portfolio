# Portfolio (static site)

HTML lives under **`templates/`**. Images, PDFs, and other assets are in **`static/`** at the repo root (sibling of `templates/`), so pages use **`../static/…`** URLs.

### Entry URL

First page: **`templates/index.html`**.

A minimal **`index.html`** at the repository root redirects there so `/` works when you serve the whole project.

### Local preview

Serve the **repository root** (not only `templates/`), otherwise `../static/…` will not resolve correctly.

```bash
npx --yes serve .
```

Then open [http://127.0.0.1:3000/templates/](http://127.0.0.1:3000/templates/) or [http://127.0.0.1:3000/](http://127.0.0.1:3000/).

### Hosting

Publish the entire repository content (both `templates/` and `static/`), keeping that layout.

The published site does not require a build step.

### YouTube embeds (Patents page)

Embedded players need a normal **`http:` / `https:`** URL (don’t rely on **`file://`**) because YouTube validates the **`Referer`** / **`origin`** request. **`templates/patents.html`** sets this up automatically; **`_headers`** (used by **[Netlify](https://docs.netlify.com/routing/headers/)**) forces **`Referrer-Policy: strict-origin-when-cross-origin`**.  

On **GitHub Pages**, omitting referrer-blocking headers usually works out of the box. If embeds still show **Error 153**, check **[YouTube embedding settings](https://support.google.com/youtube/answer/171780)** on each video or any CDN (**Cloudflare** etc.) that might override **`Referrer-Policy`** to **`same-origin`**.
