# Run from galaxy root with
# PYTHONPATH=lib GALAXY_CONFIG_FILE=config/galaxy.yml \
# python manage_bootstrap_user.py
import argparse
import os

from galaxy.celery import get_galaxy_app
from galaxy.managers.api_keys import ApiKeyManager

from scripts.db_shell import config


email = "tooladmin@galaxy.org"
name = "tooladmin"
password = "artbio2024"

os.environ["GALAXY_CONFIG_FILE"] = os.environ.get(
    "GALAXY_CONFIG_FILE", config["config_file"])
app = get_galaxy_app()
user = app.user_manager.by_email(email) or \
    app.user_manager.create(email=email, username=name,
                            password=password)
key = ApiKeyManager(app).get_or_create_api_key(user)
print(key)