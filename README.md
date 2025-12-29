# Django Project - Okere

A Django web application for managing content including news, documents, tourist information, and services.

## Features

- User authentication (login/signup)
- Admin dashboard
- News management (images and videos)
- Document upload and management
- Tourist information (images and videos)
- Service listings
- Slideshow management

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/10310229-ai/PROJECT.git
cd PROJECT
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file (copy from `.env.example`):
```bash
cp .env.example .env
```

5. Update `.env` with your settings:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

6. Run migrations:
```bash
cd PROJECT/account
python manage.py migrate
```

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Run the development server:
```bash
python manage.py runserver
```

## Deployment

### Deploy to Render.com (Recommended - Free Tier Available)

1. Go to [Render.com](https://render.com) and sign up/login
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: okere-django-app
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `cd PROJECT/account && gunicorn account.wsgi:application`
5. Add environment variables:
   - `SECRET_KEY`: Generate a new secret key
   - `DEBUG`: False
   - `ALLOWED_HOSTS`: your-app-name.onrender.com
   - `PYTHON_VERSION`: 3.11.0
6. Click "Create Web Service"

### Deploy to Railway.app

1. Go to [Railway.app](https://railway.app) and sign up/login
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Add environment variables in the Variables section:
   - `SECRET_KEY`: Your secret key
   - `DEBUG`: False
   - `ALLOWED_HOSTS`: your-app.railway.app
5. Railway will automatically detect Django and deploy

### Deploy to Heroku

1. Install Heroku CLI
2. Login to Heroku:
```bash
heroku login
```

3. Create a new Heroku app:
```bash
heroku create your-app-name
```

4. Add environment variables:
```bash
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
```

5. Push to Heroku:
```bash
git push heroku main
```

6. Run migrations:
```bash
heroku run python PROJECT/account/manage.py migrate
```

7. Create superuser:
```bash
heroku run python PROJECT/account/manage.py createsuperuser
```

## Project Structure

```
PROJECT/
├── account/               # Django project
│   ├── account/          # Project settings
│   ├── okere/           # Main application
│   ├── media/           # User uploaded files
│   └── manage.py
├── requirements.txt      # Python dependencies
├── Procfile             # Deployment configuration
├── runtime.txt          # Python version
└── .gitignore          # Git ignore rules
```

## Technologies Used

- Django 5.2.8
- SQLite (Development) / PostgreSQL (Production)
- Gunicorn
- WhiteNoise (Static file serving)
- Python 3.11

## License

This project is private and not licensed for public use.
