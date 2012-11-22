#!/usr/bin/env python
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
LOCAL_FILE = lambda *path: os.path.join(PROJECT_ROOT, *path)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

    from django.core.management import execute_from_command_line
    sys.path.insert(0, LOCAL_FILE('{{ project_name }}'))

    execute_from_command_line(sys.argv)
