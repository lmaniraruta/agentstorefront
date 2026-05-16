#!/bin/bash
# Commits any pending Railway config changes + pushes to trigger auto-deploy.
# Safe to re-run.

set -e
cd "/Users/lfidele/Documents/claude/Projects/A.I C.E.O/hard/H2-agentstorefront"

if [ -z "$(git status --porcelain)" ]; then
  echo "No local changes. Forcing redeploy by amending commit..."
  git commit --allow-empty -m "chore: trigger Railway redeploy"
else
  git add -A
  git commit -m "fix(backend): simplify nixpacks — let Railway auto-detect pip"
fi

git push
echo ""
echo "✅ Pushed. Railway will auto-redeploy in ~30 sec."
echo "   Live URL: https://agentstorefront-production.up.railway.app"
