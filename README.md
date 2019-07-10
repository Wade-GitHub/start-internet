# start-internet

A small python script to open up starting pages when accessing the internet in a web browser.

Normally with web browsers you can set which pages to open up when the web browser is started.
However, I found it annoying to have that happening every single time I opened my web browser.

With this script you can do just that; it will open a bunch of tabs in a web browser when run,
but you don't have to do that every time you open your web browser. You can run this script
while your web browser is open or run it before the web browser is open, where it will then
open the web browser with the links.

## Usage

The script gets its parameters from a local JSON file. This JSON file must be in the same
directory as the start_python.py script.

The JSON file can be called anything you want; I called mine "config.json", but you can
certainly have multiple JSON files with different groups of related links.

As an example, there could be a JSON file called "entertainment.json" to open links for
youtube and twitch, another JSON file called "social.json" to open links for facebook
and twitter, and another JSON file called "work.json" to open links for emails and
your company web login page, among other things. All you need to do is pass the name of
your JSON file to the program like so:

`$python start_internet.py config.json`

Where "config.json" is the name of the json file you made.

In this repository there is a sample JSON file called "sample_config.json", which gives an
example of the layout for the JSON files:

```json
{
    "browser": "firefox",
    "browser_path": "/usr/bin/firefox",
    "websites": [
        "https://www.google.com",
        "https://www.youtube.com",
        "https://www.facebook.com",
        "https://www.twitter.com",
        "https://www.howtogeek.com"
    ]
}
```

All you need to do is copy & paste this file under a different name (or make a new JSON file and
copy-paste the contents into there, doesn't really matter) then edit the fields for this JSON
file.

The first two fields - "browser" and "browser_path" - are the type of browser to use and where it
is located on your system. This script uses the webbrowser python module, so these fields are
used when registering a web browser. You don't have to fill in these fields; you can leave them
as empty strings and the script will try to find the default web browser on your system.

However, I've found that on my Windows system the webbrowser module will always default to
opening Internet Explorer, even though I've set my default browser to something else.
Registering a web browser using "browser" and "browser_path" is a workaround for this,
but if you aren't having this problem on your system then you can just leave these fields
blank and it will use your default browser.

The last field - "websites" - is a list (or array in JSON) of strings that are your websites.
Replace these links with whatever websites you want. There is no limit for the number of links
that you can store here, but opening a ton of links all at once will probably affect your
browser performance.

## Licence

This script uses the MIT licence. You can do what you want with this script, but just
understand that I'm not responsible for any malicious and/or damaging activity you do with
it.

## To do

- Add error control
