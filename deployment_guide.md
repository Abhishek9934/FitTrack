# Fitness Tracker Deployment Guide

## Overview
Your fitness tracker app uses CSV files for data storage, making it simple to deploy without requiring a separate database server. Here are several deployment options:

## Option 1: Streamlit Cloud (Free & Easy)
**Best for: Quick deployment with minimal setup**

### Requirements:
- GitHub account
- Your code in a GitHub repository

### Setup Steps:
1. **Prepare Repository:**
   - Remove custom port configuration from `.streamlit/config.toml`
   - Use `streamlit_requirements.txt` for dependencies
   - Ensure `app.py` is in the root directory

2. **Deploy:**
   - Push code to GitHub
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect GitHub account
   - Select repository and `app.py`
   - Deploy

### Important Configuration Fix:
Your app was configured for port 5000, but Streamlit Cloud uses the default port 8501. I've updated the configuration to be compatible with both environments.

### Pros:
- Free hosting
- Automatic deployments on code changes
- Built-in SSL certificates
- Easy domain management

### Cons:
- Data stored in temporary storage (resets on app restart)
- Limited to Streamlit Cloud infrastructure

### Data Persistence Note:
For Streamlit Cloud, consider upgrading to a paid plan or use external storage (Google Sheets, GitHub files) for data persistence.

## Option 2: Docker + VPS/Cloud Server
**Best for: Full control and persistent data**

### Requirements:
- VPS or cloud server (DigitalOcean, Linode, AWS EC2, etc.)
- Docker installed

### Setup Files Needed:
1. `Dockerfile`
2. `docker-compose.yml`
3. `requirements.txt`

### Steps:
1. Create Docker container
2. Deploy to your VPS
3. Set up reverse proxy (nginx)
4. Configure SSL certificate

### Pros:
- Full control over server
- Persistent data storage
- Custom domain
- Scalable

### Cons:
- Requires server management
- Monthly hosting costs ($5-20/month)

## Option 3: Railway (Simple Cloud Deployment)
**Best for: Easy deployment with persistent storage**

### Requirements:
- GitHub account
- Railway account

### Steps:
1. Push code to GitHub
2. Connect Railway to your repository
3. Railway auto-detects Streamlit
4. Add volume for data persistence
5. Deploy

### Pros:
- Simple deployment
- Persistent storage
- Automatic SSL
- Custom domains

### Cons:
- Paid service after free tier

## Option 4: Heroku Alternative (Render/Fly.io)
**Best for: Platform-as-a-Service deployment**

Similar to Heroku but with better pricing and performance.

## Recommended Approach for Your App

### NEW: Google Sheets Integration (Recommended for Streamlit Cloud)
Your app now supports **Google Sheets** for data storage! This is perfect for:
- **Streamlit Cloud**: Data persists across app restarts
- **Accessibility**: View/edit data directly in Google Sheets  
- **Backup**: Automatic cloud backup included
- **Mobile**: Access from any device

See `google_sheets_setup.md` for complete setup instructions.

### For Custom Hosting: Docker + VPS
If you prefer full control, **Option 2 (Docker + VPS)** provides:
1. **Data Persistence**: Your files are preserved between restarts
2. **Cost Effective**: $5-10/month for a basic VPS
3. **Full Control**: You can backup, migrate, and manage your data
4. **Scalability**: Can upgrade server resources as needed

## Hybrid Data Storage
Your app now automatically:
- **Uses Google Sheets** when credentials are configured
- **Falls back to CSV files** when Google Sheets isn't available
- **Shows storage status** in the app interface

## Setup Files Created

✅ **Google Sheets Integration:**
- `utils/sheets_manager.py` - Google Sheets data operations
- `utils/hybrid_manager.py` - Automatic fallback system
- `google_sheets_setup.md` - Complete setup guide
- Updated `streamlit_requirements.txt` - Added Google Sheets dependencies

✅ **Docker Deployment:**
- `Dockerfile` - Container configuration  
- `docker-compose.yml` - Service orchestration
- `nginx.conf` - Reverse proxy with SSL
- `deploy.sh` - Automated deployment script

## Next Steps
1. **For Streamlit Cloud**: Follow `google_sheets_setup.md` 
2. **For Custom Hosting**: Use the Docker files provided
3. **For Development**: App works with CSV files by default