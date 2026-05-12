#!/bin/bash
# setup-auto-deploy.sh - Setup automatic deployment to Render

set -e

echo "🚀 CI/CD Auto-Deployment Setup"
echo "================================"
echo ""

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI not found. Install from: https://cli.github.com"
    exit 1
fi

# Check if git is available
if ! command -v git &> /dev/null; then
    echo "❌ Git not found"
    exit 1
fi

echo "✅ GitHub CLI found"
echo ""

# Get repository info
REPO=$(git config --get remote.origin.url | sed 's/.*[:/]\([^/]*\/[^/]*\)\.git$/\1/')
echo "📦 Repository: $REPO"
echo ""

echo "📋 Setup Instructions:"
echo ""
echo "1️⃣  Create Render Web Service:"
echo "   • Go to https://render.com/dashboard"
echo "   • Click 'New +' → 'Web Service'"
echo "   • Connect GitHub repo: $REPO"
echo "   • Set Build Command: pip install -r requirements.txt"
echo "   • Set Start Command: gunicorn app:app"
echo ""

echo "2️⃣  Get Deploy Hook:"
echo "   • In Render dashboard, click on your service"
echo "   • Go to Settings → Deploy Hook"
echo "   • Copy the webhook URL"
echo ""

read -p "3️⃣  Paste your Render Deploy Hook URL: " DEPLOY_HOOK

if [ -z "$DEPLOY_HOOK" ]; then
    echo "❌ Deploy hook URL cannot be empty"
    exit 1
fi

echo ""
echo "4️⃣  Adding secret to GitHub..."

# Add secret to GitHub
echo "$DEPLOY_HOOK" | gh secret set RENDER_DEPLOY_HOOK --repo "$REPO"

echo "✅ Secret added: RENDER_DEPLOY_HOOK"
echo ""

# Optional: Add app URL
read -p "📱 Enter your Render app URL (optional, press Enter to skip): " APP_URL

if [ ! -z "$APP_URL" ]; then
    echo "$APP_URL" | gh secret set RENDER_APP_URL --repo "$REPO"
    echo "✅ Secret added: RENDER_APP_URL"
    echo ""
fi

echo "🎉 Setup Complete!"
echo ""
echo "Next steps:"
echo "1. Make a change to your code"
echo "2. Commit and push to main branch"
echo "3. Watch GitHub Actions run the pipeline"
echo "4. Your app will auto-deploy to Render!"
echo ""
echo "📊 Monitor deployment:"
echo "   • GitHub: https://github.com/$REPO/actions"
echo "   • Render: https://dashboard.render.com"
echo ""
echo "✨ Happy deploying!"
