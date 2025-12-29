# GitHub-Powered Deployment Guide

Your Django app is configured for **automatic deployment via GitHub** using GitHub Actions + Render.

## 🚀 Quick Deploy (One-Time Setup)

### Step 1: Deploy to Render via GitHub

1. **Go to Render**: https://render.com/
2. **Sign up/Login** using your GitHub account
3. Click **"New +"** → **"Web Service"**
4. **Connect your GitHub repository**: `10310229-ai/PROJECT`
5. Render will auto-detect the `render.yaml` configuration
6. Click **"Create Web Service"**
7. Your app will deploy automatically! 🎉

### Step 2: Get Your App URL

After deployment completes (2-3 minutes):
- Your app will be live at: `https://okere-django-app.onrender.com`
- Update the `ALLOWED_HOSTS` environment variable in Render with your actual URL

### Step 3: Enable Auto-Deploy from GitHub (Optional but Recommended)

To automatically deploy when you push to GitHub:

1. In Render dashboard, go to your web service
2. Go to **Settings** → **Deploy Hook**
3. Copy the Deploy Hook URL
4. Go to your GitHub repo: https://github.com/10310229-ai/PROJECT
5. Go to **Settings** → **Secrets and variables** → **Actions**
6. Click **"New repository secret"**
7. Name: `RENDER_DEPLOY_HOOK`
8. Value: Paste the Deploy Hook URL from Render
9. Click **"Add secret"**

Now every push to `main` branch will automatically deploy! 🔄

## 🔧 Configure Environment Variables in Render

1. Go to your web service in Render
2. Navigate to **Environment** section
3. Add/Update these variables:
   - `ALLOWED_HOSTS` = your-app-name.onrender.com
   - `SECRET_KEY` = (auto-generated, leave as is)
   - `DEBUG` = False

## 📦 How It Works

### Automatic Deployment Flow:
```
1. You push code to GitHub (main branch)
   ↓
2. GitHub Actions runs tests automatically
   ↓
3. If tests pass, triggers Render deployment
   ↓
4. Render pulls latest code and deploys
   ↓
5. Your app is live with latest changes! ✅
```

### Files That Make This Work:
- `.github/workflows/deploy.yml` - GitHub Actions workflow
- `render.yaml` - Render configuration
- `requirements.txt` - Python dependencies
- `Procfile` - Deployment commands
- `runtime.txt` - Python version

## 🎯 Common Tasks

### Push Updates
```bash
git add .
git commit -m "Your update message"
git push origin main
```
→ App auto-deploys in 2-3 minutes

### View Deployment Status
- GitHub: Go to **Actions** tab
- Render: Check **Logs** section

### Run Migrations After Deploy
In Render dashboard:
1. Go to **Shell** tab
2. Run: `cd PROJECT/account && python manage.py migrate`

### Create Superuser
In Render Shell:
```bash
cd PROJECT/account
python manage.py createsuperuser
```

## 🆓 Free Tier Limits

Render Free Tier includes:
- ✅ 750 hours/month (enough for 24/7 uptime)
- ✅ Auto-sleep after 15 min of inactivity
- ✅ Automatic SSL certificate
- ✅ GitHub integration
- ⚠️ App spins down when inactive (takes 30-50s to wake up)

## 🔍 Troubleshooting

### App not deploying?
- Check GitHub Actions tab for errors
- Verify `RENDER_DEPLOY_HOOK` secret is set correctly
- Check Render logs for error messages

### Static files not loading?
Run in Render Shell:
```bash
cd PROJECT/account
python manage.py collectstatic --noinput
```

### Database issues?
- Free tier uses SQLite (file-based)
- For production, upgrade to Render's PostgreSQL
- Add DATABASE_URL env variable

## 📚 Alternative: Manual Deployment

Without GitHub Actions, Render still auto-deploys when you push to GitHub if you set up the integration. The GitHub Action just adds automated testing.

## 🔗 Useful Links

- Your GitHub Repo: https://github.com/10310229-ai/PROJECT
- Render Dashboard: https://dashboard.render.com/
- GitHub Actions: https://github.com/10310229-ai/PROJECT/actions

## 📝 Next Steps

1. ✅ Deploy to Render (follow Step 1 above)
2. ✅ Get your app URL
3. ✅ Update ALLOWED_HOSTS
4. ✅ Set up Deploy Hook for auto-deploy
5. ✅ Run migrations in Render Shell
6. ✅ Create superuser
7. ✅ Test your live app!

---

**Need help?** Check Render docs: https://render.com/docs
