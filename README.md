# Dr. Henry Okechi — Portfolio (v3.1)

A conversion-engineered, editorial static portfolio showcasing clinical AI training & RLHF evaluation, Web3 growth & account management, full-stack products, and generative cinema.

## Preview Locally
```bash
python -m http.server 8000
```
Then open `http://localhost:8000`.

## Deploy
Zero build step required for hosting—drag and drop the folder or connect the repository directly to **Netlify**, **Cloudflare Pages**, **Vercel**, or **GitHub Pages**. All embedded Azarun `.mp4` clips are under 8.1 MB each (well within Cloudflare Pages' 25 MB single-file limit).

## Updating Content
- Edit `projects.json` for project copy, links, video clips, or gallery frames.
- Edit `TESTIMONIALS` or `EXPERIENCE` in `build.py` to swap in named client/manager references.
- Run `python build.py` to regenerate all static HTML pages.
