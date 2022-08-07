from abc import abstractmethod
import os
from typing import List
from tqdm import tqdm

from requests import Response


class Downloader:
    def __init__(self, dir: str, filename: str):
        if not os.path.exists(dir):
            os.mkdir(dir)
        self.dir = dir
        self.filename = filename

        self.video_dir = os.path.join(dir, filename)

    @staticmethod
    def process_video(res: Response, video_dir: str):
        with open(video_dir, "wb") as f:
            size = int(res.headers.get("content-length", 0))
            progress_bar = tqdm(
                total=size,
                unit="iB",
                unit_scale=True,
                desc="Downloading",
                ascii=True
            )
            for chunk in res.iter_content(chunk_size=1024*1024):
                progress_bar.update(len(chunk))
                if chunk:
                    f.write(chunk)
            progress_bar.close()

    @abstractmethod
    def get_code(self):
        pass

    @abstractmethod
    def download(self, video_id: str):
        pass


class AnimeSite:

    def __init__(self, dw: Downloader) -> None:
        self.dw = dw

    def get_video_url(self, slug: str, chapter: int, player_name: str = None) -> str:
        pass

    def download_chapter(self, slug: str, chapter: int, player_name: str = None) -> None:
        """ Download and save video """
        url = self.get_video_url(slug, chapter, player_name)
        self.dw.download(url)

    def download(self, slug: str, dir: str):
        """ Download videos """
