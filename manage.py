#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todolist_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# This Django project was created with this command:
# >>> django-admin startproject todolist_project

# To start the development server, execute this command:
# >>> python manage.py runserver
# Press Ctrl-C to stop the server

# To create an application on this project, execute this command:
# >>> python manage.py startapp <app_name>

# Create a super user account with this command in order to access to the admin page.
# >>> python manage.py createsuperuser  (yigit / django123456)
# Then, go to this URL: http://localhost:8000/admin/