# Google Sheets Setup Guide

Your fitness tracker now supports Google Sheets for persistent data storage! This is perfect for Streamlit Cloud deployment where data persists across app restarts.

## Quick Setup Steps

### 1. Create Google Service Account
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the Google Sheets API and Google Drive API
4. Go to "Credentials" → "Create Credentials" → "Service Account"
5. Fill in service account details and create
6. Click on the created service account
7. Go to "Keys" tab → "Add Key" → "Create New Key" → Choose "JSON"
8. Download the JSON key file

### 2. Prepare Google Sheets
1. Create a new Google Spreadsheet
2. Copy the spreadsheet URL
3. Share the spreadsheet with your service account email (from the JSON file)
4. Give it "Editor" permissions

### 3. Configure Streamlit Secrets

#### For Streamlit Cloud:
1. Go to your Streamlit Cloud app settings
2. In "Secrets" section, add:

```toml
[google_sheets]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "-----BEGIN PRIVATE KEY-----\nYOUR-PRIVATE-KEY\n-----END PRIVATE KEY-----\n"
client_email = "your-service-account@your-project.iam.gserviceaccount.com"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "your-cert-url"

spreadsheet_url = "https://docs.google.com/spreadsheets/d/your-spreadsheet-id/edit"
```

#### For Local Development:
Create `.streamlit/secrets.toml` file:

```toml
[google_sheets]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "-----BEGIN PRIVATE KEY-----\nYOUR-PRIVATE-KEY\n-----END PRIVATE KEY-----\n"
client_email = "your-service-account@your-project.iam.gserviceaccount.com"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "your-cert-url"

spreadsheet_url = "https://docs.google.com/spreadsheets/d/your-spreadsheet-id/edit"
```

**Important:** Never commit the secrets.toml file to version control!

### 4. How It Works

The app now uses a hybrid approach:
- **With Google Sheets configured:** All data is saved to and loaded from Google Sheets
- **Without Google Sheets:** Falls back to local CSV files

### 5. Benefits

✅ **Persistent Data**: Your fitness data survives app restarts on Streamlit Cloud
✅ **Accessible Anywhere**: View and edit your data directly in Google Sheets
✅ **Backup Included**: Google Sheets provides automatic backups
✅ **Collaborative**: Share your progress with trainers or family
✅ **Mobile Friendly**: Access data from any device

### 6. Google Sheets Structure

The app automatically creates these worksheets:
- **body_metrics**: Weight, body measurements, body fat percentage
- **workout_data**: Exercise completion, duration, intensity
- **diet_data**: Meal adherence, calorie tracking

### 7. Security Notes

- Service account keys provide programmatic access to your spreadsheet
- Only the specific spreadsheet you share will be accessible
- Keep your service account JSON file secure
- Consider using environment variables for production deployments

### 8. Troubleshooting

**Connection Failed?**
- Check if APIs are enabled in Google Cloud Console
- Verify service account has access to the spreadsheet
- Ensure all credentials are correctly copied to secrets

**Permission Denied?**
- Make sure you shared the spreadsheet with the service account email
- Grant "Editor" permissions to the service account

**Data Not Syncing?**
- Check internet connection
- Verify spreadsheet URL is correct
- Look for error messages in the app

## Next Steps

1. Set up your Google Sheets credentials
2. Deploy to Streamlit Cloud
3. Start tracking your fitness journey with persistent data!

Your data will automatically sync between the app and Google Sheets, giving you the best of both worlds: a beautiful mobile interface and powerful spreadsheet capabilities.