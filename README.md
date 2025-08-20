# Yeka Research Hub

A Django-based research management and sharing platform.

## Features
- User authentication and admin interface
- Research file upload and management
- Static and media file handling
- PostgreSQL database support

## Quick Start Guide

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd yeka
```

### 2. Set Up Python Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the project root with your PostgreSQL connection string:
```
DATABASE_URL='postgresql://<user>:<password>@<host>:5432/<dbname>?sslmode=require'
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 6. Create Default Admin User
By default, a management command is provided to create an admin user:
```bash
python manage.py create_default_admin
```
- Default credentials:
  - Username: `admin`
  - Password: `admin1234`
  - Email: `admin@example.com`
- You can override these by setting the environment variables `DJANGO_ADMIN_USERNAME`, `DJANGO_ADMIN_PASSWORD`, and `DJANGO_ADMIN_EMAIL` before running the command.

### 7. Populate Demo Data
To fill the system with meaningful demo data for all models (Authors, Departments, Research) and to demo all templates:
```bash
python manage.py populate_demo_data
```
This will:
- Clear existing demo data
- Create 3 departments, 8 authors, and 10 research projects (with sample files)
- Link research to random authors and departments

### 8. Run the Development Server
```bash
python manage.py runserver
```
Visit [http://localhost:8000](http://localhost:8000) in your browser.

## Testing
- To run tests:
```bash
python manage.py test
```

## Notes
- Make sure your PostgreSQL database is running and accessible.
- The static files are collected into the `staticfiles/` directory for production use.
- For production deployment, set `DEBUG=False` and configure `ALLOWED_HOSTS` appropriately in `rhub/settings.py`.
- If you see a warning about the `static` directory not existing, create it at the project root if you need custom static files.
- If you need to reset the admin password, delete the user from the database or change the credentials and rerun the `create_default_admin` command.

---

For further customization, see the Django and project documentation.
