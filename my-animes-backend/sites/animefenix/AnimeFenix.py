from http.client import HTTPException
from urllib import parse

from models.Site import AnimeSite
from sites.fireload.Fireload import Fireload
from sites.yourupload.Yourupload import YourUpload
from . import constants
import requests

from bs4 import BeautifulSoup


def get_tab_id(html: str, player_name: str) -> int:
    """ 
    Get tab id from attribute id='vid#ID' 

    Only supports : 
        -   YourUpload
    """
    soup = BeautifulSoup(html, "lxml")
    tab_id = soup.find("div", {
        "class": "tabs"
    }).find("ul").find("a", {
        "title": player_name
    })["href"].replace("#vid", "")

    return int(tab_id)


def get_tab_url(html, i):
    """ 
        Get tab url only supports : 
        -   YourUpload
        -   Fireload
    """
    soup = BeautifulSoup(html, "lxml")
    s = soup.find("div", {
        "class": "player-container"
    }).find("script").string
    tabs = [tab.strip() for tab in s.strip().split("\n")]
    tabs.pop(0)
    tabs = [tab.split('"')[1] for tab in tabs]

    frames = []
    for tab in tabs:
        if not tab:
            continue
        f_soup = BeautifulSoup(tab, "lxml")
        f = f_soup.find("iframe")["src"]
        frames.append(f)

    return frames[i - 1]


def get_embed_url(anime_slug: str, chapter: int, player_name: str = None) -> str:
    """ 
    Get embed url

    Parameters
    ----------
    anime_slug  (int)   example: overlord
    chapter     (int)   example: 1
    embed_name  (int)   default: YourUpload
    """

    if not player_name:
        player_name = constants.YOUR_UPLOAD

    url = constants.BASE_URL + f"/ver/{anime_slug}-{chapter}"
    req = requests.get(url)
    html = req.text

    tab_id = get_tab_id(html, player_name)
    tab_url = get_tab_url(html, tab_id)

    return tab_url


def get_code_of_embed(embed_url: str) -> str:
    parsed_url = parse.urlsplit(embed_url)
    qs = dict(parse.parse_qs(parsed_url.query))
    return qs["code"][0]


class AnimeFenix(AnimeSite):

    def get_video_url(self, slug: str, chapter: int, player_name: str = None):
        if not player_name:
            player_name = constants.YOUR_UPLOAD
        embed = get_embed_url(slug, chapter, player_name)
        print(f"EMBED URL -> {embed}")
        url = get_code_of_embed(embed)
        print(f"{player_name} VIDEO ID {url}")
        return url
