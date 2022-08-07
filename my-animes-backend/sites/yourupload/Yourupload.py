from http.client import HTTPException
import os
import requests

from models.Site import Downloader
from . import constants
from bs4 import BeautifulSoup


def get_watch_page(video_id: str) -> str:
    url = constants.WATCH_URL + f"/{video_id}"
    res = requests.get(url)
    html = res.text

    soup = BeautifulSoup(html, "lxml")
    dw_url = soup.find("a", {
        "class": "btn btn-success"
    })["href"]

    return constants.BASE_URL + dw_url


def get_download_url(video_id: str) -> str:
    url = get_watch_page(video_id)

    print("Getting download page")
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, "lxml")
    dw_url = soup.find("a", {
        "class": "btn btn-success"
    })["data-url"]
    print("Download url getted !!")
    return constants.BASE_URL + dw_url


class YourUpload(Downloader):
    def download(self, video_id: str):
        print("Fetching download url ...")
        url = get_download_url(video_id)
        print("Download url fetched !!")

        print("Downloading video ...")
        print(f"Download video url -> {url}")
        res = requests.get(url, stream=True, headers={
            "Referer": "https://www.yourupload.com/"
        })

        if res.status_code == 404:
            raise HTTPException({
                "code": res.status_code,
                "message": "Cannot found video"
            })
        self.process_video(res, self.video_dir)
        print(f"Downloaded {self.filename} !!")
