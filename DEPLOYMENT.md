# Deployment Guide

## Vercel (Recommended)

### One-time Setup
1. Install Vercel CLI: `npm install -g vercel`
2. Login: `vercel login`
3. Link project: `vercel link`

### Deploy
```bash
# Preview deployment
vercel

# Production deployment
vercel --prod
```

## Manual GitHub Pages
```bash
# Copy web/index.html to root for GitHub Pages
cp web/index.html index.html
git add index.html
git commit -m "Add GitHub Pages deployment"
git push

# Enable GitHub Pages in repo settings → Pages → main branch
```

## Netlify
1. Connect GitHub repo in Netlify dashboard
2. Set build settings:
   - Base directory: `web`
   - Publish directory: `web`
3. Deploy

## Quick Deploy Checklist
- [ ] Test calculator locally (open web/index.html)
- [ ] Commit all changes
- [ ] Push to GitHub
- [ ] Deploy to Vercel/Netlify
- [ ] Test live site
- [ ] Share URL!

## Current Status
- ✅ Enhanced creator professions (7 new roles)
- ✅ Dynamic copy variations (4x each scenario)
- ✅ Profession-specific pro tips
- ✅ Deployment config ready
