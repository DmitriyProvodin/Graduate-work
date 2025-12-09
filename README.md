# E-Learning Platform (Django + DRF) — Minimal Working Scaffold

This repository is a minimal scaffold of an e-learning platform built with Django + Django REST Framework,
implementing JWT authentication, roles, courses/sections/materials, tests and admin, PostgreSQL-ready settings,
Swagger (drf-spectacular), CORS and basic pytest tests.

**What's included**
- Django project: `config/`
- Apps: `apps.accounts`, `apps.courses`
- JWT via `djangorestframework-simplejwt`
- API documentation via `drf-spectacular`
- Docker compose and `.env_template`
- Minimal pytest tests

**How to run (local dev)**
1. Create a Python 3.11+ virtualenv and install requirements:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Copy `.env_template` to `.env` and fill values.
3. Run migrations:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Run dev server:
   ```bash
   python manage.py runserver
   ```

**Docker**
A `docker-compose.yml` is provided that launches a Postgres DB and the web service.

**Notes**
- This is a scaffold: adapt and extend before production use.
- Secrets are read from environment variables.

