#!/bin/bash
# Commits the Railway config files + redeploys.
# Run after PUSH_TO_GITHUB.sh has been run at least once.

set -e
cd "/Users/lfidele/Documents/claude/Projects/A.I C.E.O/hard/H2-agentstorefront"
git add -A
git commit -m "fix(backend): Railway deploy config — Procfile + nixpacks + email-validator"
git push
echo ""
echo "✅ Pushed. Railway will auto-redeploy in ~30 sec."
