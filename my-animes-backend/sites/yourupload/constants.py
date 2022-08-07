import re


BASE_URL = "https://www.yourupload.com"

PROVIDER_NAME = "YourUpload"

EMBED_URL = f"{BASE_URL}/embed"
WATCH_URL = f"{BASE_URL}/watch"

REGEX_EMBED_URL = r"https:\/\/www.yourupload.com\/embed\/(.{12})"
