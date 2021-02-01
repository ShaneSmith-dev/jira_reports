"""
Manages configuration including creation if empty
"""

import os.path # Used to get the home directory for the user
import toml

# Default configuration string
def_config = """
title = "Jira Reports Configuration"

[owner]
name = ""
email = ""

[server]
base_uri = "https://jira.atlassian.com"
api_uri = "https://jira.atlassian.com/rest/api/2"

[users]
# The intent here is to allow custom groups of users to be used in reports

[custom_fields]
# The intent here is to allow custom fields to be used in reports
"""

# TODO: Make this more platform independent
home_dir = os.path.expanduser("~")
default_config_path = os.path.join(home_dir,"AppData","Local","jira_reports","jira_reports_config.toml") 

def load_config(config_file=None):
    if config_file is None:
        config_path = default_config_path
    else:
        config_path = config_file
    try:
        config = toml.load(config_path)
    except:
        config = config_init()
    return config

def config_init():
    config = toml.loads(def_config)
    with open(default_config_path, 'w') as f:
        print("Default configuration file created at:\n" + default_config_path)
        toml.dump(config,f)
    return config