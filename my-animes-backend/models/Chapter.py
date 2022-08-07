from pydantic import BaseModel


class Chapter(BaseModel):
    id: int
    image: str
    title: str
    video_path: str
