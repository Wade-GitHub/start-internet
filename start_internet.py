"""
start_internet.py
A Small script to open up starting pages when accessing the internet in a web browser.

Author: Wade
Licence: MIT
Contact: wwrwade@gmail.com

TODO: add error control
TODO: make program use command line arguments
TODO: add comments to functions
"""

import webbrowser
import sys
import time
import json
import os


def load_config(json_file):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(current_dir, json_file), "r") as config_file:
        config = json.load(config_file)
    return config


def set_browser(browser_type="default", path="default"):
    if browser_type != "default" and path != "default":
        webbrowser.register(browser_type, None, webbrowser.BackgroundBrowser(path))
        browser = webbrowser.get(browser_type)
        return browser
    return webbrowser


def open_links(sites_list, browser):
    browser.open(sites_list[0])
    if sys.platform == "win32":
        time.sleep(6)
    for link in sites_list[1:]:
        browser.open_new_tab(link)


if __name__ == "__main__":
    config = load_config("config.json")

    browser_type = config["browser"]
    browser_path = config["browser_path"]
    websites_list = config["websites"]

    browser_to_use = set_browser(browser_type, browser_path)

    open_links(websites_list, browser_to_use)
