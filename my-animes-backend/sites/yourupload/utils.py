import re
from . import constants


def get_download_file_url(file_id: str):
    return f"{constants.BASE_URL}/download?file={file_id}"


def get_watch_url(payload: str) -> str:
    """ Get watch url from html with regex """
    video_id = re.findall(constants.REGEX_EMBED_URL, payload)
    url = constants.WATCH_URL + "/" + video_id[0]
    return url
