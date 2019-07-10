import webbrowser
import sys
import time
import json
import os
import argparse


PROGRAM_DESCRIPTION = """
A Small script to open up starting pages when accessing the internet in a
web browser.

See the README.md file for more info.
"""

CONTACT_INFO = """
Author: Wade
Licence: MIT
Contact: wwrwade@gmail.com
"""


def get_arguments() -> argparse.Namespace:
    """
    Get the arguments from the command line and parse them.

    At the moment, the program only takes in a config_file argument, which is
    a JSON file that contains the configuration for things like the type of
    web browser to use and the links to open in that browser.
    """
    parser = argparse.ArgumentParser(
        description=PROGRAM_DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=CONTACT_INFO
    )
    parser.add_argument(
        "config_file", help="The JSON file that contains the web links."
    )
    args = parser.parse_args()
    return args.config_file


def load_config(json_file: str) -> dict:
    """
    Load the configuration settings stored in json_file and return as a
    dictionary with settings.

    This will always look for the JSON file inside the same directory that
    this script is currently in.
    """
    current_dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(current_dir, json_file), "r") as config_file:
        config = json.load(config_file)
    return config


def set_browser(browser_type="default", path="default"):
    """
    Set the type of browser that the user wants to use from their config file.

    If a browser_type and path are given from the config settings, this will
    register that browser as the web browser to use for opening the links and
    return a webbrowser.BackgroundBrowser.

    If browser_type and path were empty strings in the config file,
    or if one of them was empty, this will return a reference to the
    webbrowser module that will be used as "webbrowser.open()" to get the
    system's default webbrowser.
    """
    if browser_type != "default" and path != "default":
        webbrowser.register(browser_type, None,
                            webbrowser.BackgroundBrowser(path))
        browser = webbrowser.get(browser_type)
        return browser
    return webbrowser


def open_links(sites_list: list, browser):
    """
    Open the links in sites_list with the given web browser.

    If a web browser is not currently open, a new window for a web browser
    will be started and the links opened in new tabs. If a web browser is
    currently open, the links will be opened in new tabs in that browser
    window.
    """
    browser.open(sites_list[0])
    if sys.platform == "win32":
        time.sleep(6)
    for link in sites_list[1:]:
        browser.open_new_tab(link)


if __name__ == "__main__":
    config_file = get_arguments()

    config = load_config(config_file)

    browser_type = config["browser"]
    browser_path = config["browser_path"]
    websites_list = config["websites"]

    browser_to_use = set_browser(browser_type, browser_path)

    open_links(websites_list, browser_to_use)
