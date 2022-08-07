from abc import ABC, abstractmethod
import os
from typing import List
from tqdm import tqdm

from requests import Response


class Downloader(ABC):
    def __init__(self, dir: str, extension: str = None):
        """
        Params:
        -
        -   dir         (str)   Directory where save files
        -   extension   (str)   Extension of file -> default : .mp4
        """
        if not os.path.exists(dir):
            os.mkdir(dir)
        if not extension:
            self.extension = ".mp4"
        self.dir = dir

    def compose_video_dir(self, filename: str) -> str:
        if not self.extension in filename:
            filename += self.extension
        return os.path.join(self.dir, filename)

    @staticmethod
    def process_video(res: Response, video_dir: str):
        """ Process and save video """
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
    def download(self, video_id: str, filename: str):
        pass


class AnimeSite:

    def __init__(self, dw: Downloader) -> None:
        self.dw = dw

    def get_video_url(self, slug: str, chapter: int, player_name: str = None) -> str:
        pass

    def download_chapter(self, slug: str, chapter: int, player_name: str = None) -> None:
        """ Download and save video """
        url = self.get_video_url(slug, chapter, player_name)
        self.dw.download(url, f"cap-{chapter}")

    def download(self, slug: str, dir: str):
        """ Download videos """
