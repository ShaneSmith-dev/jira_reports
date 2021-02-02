"""
Test for config.py
"""

import os
from jira_reports.config import load_config

references = os.path.join(os.path.dirname(os.path.abspath(__file__)), "references")
example_config = os.path.join(references, "example_config.toml")

def test_load_config():
    cfg = load_config(example_config)
    assert "title" in cfg.keys()

    assert "owner" in cfg.keys()
    assert "name" in cfg["owner"].keys()
    assert "email" in cfg["owner"].keys()

    assert "server" in cfg.keys()
    assert "base_uri" in cfg["server"].keys()
    assert "api_uri" in cfg["server"].keys()

    assert "users" in cfg.keys()
    assert "myself" in cfg["users"].keys()
    assert "ship_crew" in cfg["users"].keys()
    assert "employees" in cfg["users"].keys()

    assert "custom_fields" in cfg.keys()