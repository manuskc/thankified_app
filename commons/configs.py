import os
import logging

class Config(object):
    app_name = "Thankified"
    app_context = "/thankified"
    log_level = logging.DEBUG
    db_connection = "sqlite+pysqlite:///:memory:"
    slack_client_id = "" # Works on prod only
    slack_token = "" # Works on prod only
    slack_client_secret = "" # Works on prod only
    app_domain = "" # Works on prod only

env = os.environ.get('THANKIFIED_ENV') # Define this on host boxes
if env == 'prod':
    Config.log_level = logging.INFO
    Config.db_connection = "sqlite+pysqlite:////path/to/sqlite3.db" # Replace with your path or other db connection
    Config.slack_client_id = os.environ.get('SLACK_CLIENT_ID') # Define the keys on host boxes
    Config.slack_client_secret = os.environ.get('SLACK_CLIENT_SECRET') # Define the keys on host boxes
    Config.slack_token = os.environ.get('SLACK_TOKEN') # Define the keys on host boxes
    Config.app_domain = "api.yourhost.com" # Replace with your host