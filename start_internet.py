import argparse
import json
import pathlib
import sys
import time
import webbrowser
import yaml


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


def load_config(config_file: str) -> dict:
    """
    Load config from a given file.

    This will always look for the config file inside the same directory that
    this script is currently in.

    Args:
        config_file: A file that contains config. This can be in one of the
            following forms:
            - json
            - yaml

    """
    current_dir = pathlib.Path(__file__).parent
    config_file_path = current_dir / config_file

    config = None
    with open(config_file_path, "r") as f:
        if config_file.endswith(".json"):
            config = json.load(f)
        elif (config_file.endswith(".yml") or config_file.endswith(".yaml")):
            config = yaml.safe_load(f)
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
        webbrowser.register(
            browser_type, None, webbrowser.BackgroundBrowser(path)
        )
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
    first_link = sites_list[0]
    rest = sites_list[1:]

    browser.open(first_link)
    if sys.platform == "win32":
        # Windows has a quirky issue where if the web browser isn't yet open,
        # there's a startup delay that will skip one of the links when looping
        # over them too quickly.
        # The added sleep delay lets the browser "warm up" with the first link,
        # before looping over the rest.
        time.sleep(2)
    for link in rest:
        browser.open(link)


if __name__ == "__main__":
    config_file = get_arguments()

    config = load_config(config_file)

    browser_type = config["browser"]
    browser_path = config["browser_path"]
    websites_list = config["websites"]

    browser_to_use = set_browser(browser_type, browser_path)

    open_links(websites_list, browser_to_use)
