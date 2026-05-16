#!/bin/bash
# Run this ONCE from your Mac Terminal (or paste into Claude Code).
# Pushes the H2-agentstorefront folder to github.com/lmaniraruta/agentstorefront

set -e

cd "/Users/lfidele/Documents/claude/Projects/A.I C.E.O/hard/H2-agentstorefront"

# Fresh git init
rm -rf .git
git init -b main
git config user.email "lmaniraruta@gmail.com"
git config user.name "Fidele M."

git add -A
git commit -m "feat: AgentStorefront MVP — backend + SDK + landing + distribution

- FastAPI backend with /sellers, /services, /agents, /discover, /subscribe
- SQLite + Stripe Connect (12% platform fee)
- Python SDK 'agentstorefront' v0.1.0 with discover/subscribe/call
- Static landing page (Tailwind, Vercel-ready)
- Full distribution copy (HN, Reddit, X thread, 25 DM targets)
- Backend tests passing 2/2

Built per A.I C.E.O hard/H2-agentstorefront plan."

git remote add origin https://github.com/lmaniraruta/agentstorefront.git
git branch -M main
git push -u origin main

echo ""
echo "✅ Pushed. View at: https://github.com/lmaniraruta/agentstorefront"
