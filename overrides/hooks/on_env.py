import logging
import os
import shutil
import urllib.parse
from datetime import datetime
from pathlib import Path

import obsidiantools.api as otools
from babel.dates import format_date
from dateutil import parser
from pyvis.network import Network


def obsidian_graph():
    """Generates a graph of the Obsidian vault."""
    log = logging.getLogger("mkdocs.plugins." + __name__)
    log.info("[OBSIDIAN GRAPH] Generating graph...")
    vault = otools.Vault(os.getcwd()).connect().gather()
    graph = vault.graph
    net = Network(height="750px", width="750px", font_color="#7c7c7c", bgcolor="transparent")
    net.from_nx(graph)
    try:
        net.save_graph(str(Path.cwd() / "docs" / "assets" / "graph.html"))
    except OSError:
        pass
    shutil.rmtree(Path.cwd() / "lib")
    log.info("[OBSIDIAN GRAPH] Graph generated!")
    return ""


obsidian_graph()


def log(text):
    """Prints text to the console, in case you need to debug something.

    Using mainly in the template files.
    Parameters:
        text (str): The text to print.
    Returns:
        str: An empty string.
    """
    print(text)
    return ""


def time_time(time):
    """Converts a time string to a human-readable format.

    Parameters:
        time (any): The time string to convert.
    Returns:
        str|datetime:  The converted time.
    """
    time = time.replace("-", "/")
    time = parser.parse(time).isoformat()
    try:
        time = datetime.fromisoformat(time)
        return datetime.strftime(time, "%d %B %Y")
    except AttributeError:
        return datetime.strftime(str(time), "%d %B %Y")
    except ValueError:
        print("value error!")
        return time


def to_local_time(time, locale):
    """Convert to local time.

    Args:
        time (any): the time to convert
        locale (any): the locale to use

    Returns:
        str: the converted time
    """
    date = time.replace("-", "/")
    date = parser.parse(date)
    return format_date(date, locale=locale)


def time_todatetime(time):
    """convert time to datetime.

    Args:
        time (any): time to convert

    Returns:
        datetime: the converted time
    """
    return parser.parse(time)


def time_to_iso(time):
    """Convert time to ISO format.

    Args:
        time (any): Time to convert

    Returns:
        any|str: convert time or the original time if error
    """
    time = time.replace("-", "/")

    try:
        return parser.parse(time).isoformat()
    except AttributeError:
        return time


def page_exists(page):
    """Check if a page exists.

    Args:
        page (any): The page to check

    Returns:
        bool: true if exists
    """
    return Path(page).exists()


def url_decode(url):
    """decode an url in a template.

    Args:
        url (any): THE URL

    Returns:
        str : the decoded url
    """
    return urllib.parse.unquote(url)


def on_env(env, config, files, **kwargs):
    env.filters["convert_time"] = time_time
    env.filters["iso_time"] = time_to_iso
    env.filters["time_todatetime"] = time_todatetime
    env.filters["page_exists"] = page_exists
    env.filters["url_decode"] = url_decode
    env.filters["log"] = log
    env.filters["to_local_time"] = to_local_time
    return env
