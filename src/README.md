# Database Reset API - Deployment Ready

This folder contains all files needed to deploy the database reset application to Render.

## Files Included

- `web.py` - Flask web application with HTTP endpoints
- `clear_db.py` - Database clearing logic
- `requirements.txt` - Python dependencies
- `Procfile` - Render process configuration
- `.env.example` - Environment variables template

## API Endpoints

- `GET /` - API information
- `POST /clear` - Clear the database table
- `GET /health` - Health check endpoint

## Render Deployment Steps

### 1. Prepare Your Repository

1. Create a new GitHub repository
2. Copy all files from this `deploy` folder to your repository root
3. Push the repository to GitHub

### 2. Set Up Render

1. Sign up/log in to [Render](https://render.com)
2. Click "New+" → "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `db-reset-api` (or your preferred name)
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python web.py`
   - **Instance Type**: Free (to start)

### 3. Configure Environment Variables

In your Render service settings, add these environment variables:

1. Go to your service → "Environment" tab
2. Add the following variables:
   ```
   DATABASE_URL=postgresql://neondb_owner:npg_Po0cHtO9wyIx@ep-spring-frost-a1475bv7-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
   TABLE_NAME=people
   PORT=5000
   ```

**Important**: Replace the `DATABASE_URL` with your actual database URL.

### 4. Deploy

1. Click "Create Web Service"
2. Render will automatically build and deploy your application
3. Wait for the deployment to complete (green status)

### 5. Test Your API

Once deployed, you can test your API:

```bash
# Health check
curl https://your-service-name.onrender.com/health

# Clear the database table
curl -X POST https://your-service-name.onrender.com/clear
```

## Local Testing

To test locally before deployment:

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables (copy .env.example to .env and fill in values)
cp .env.example .env

# Run the application
python web.py
```

The API will be available at `http://localhost:5000`

## Security Notes

- Never commit your actual `.env` file to version control
- Use Render's environment variables for sensitive data
- Consider adding authentication for production use
- The `/clear` endpoint is powerful - protect it appropriately
