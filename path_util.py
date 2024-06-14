import os


def get_path(*paths: str) -> str:
    return os.path.join(PROJECT_DIR, *paths)


def join(base: str, *paths: str):
    return os.path.join(base, *paths)


PROJECT_DIR: str = os.path.dirname(__file__)
GRAPHICS_DIRECTORY: str = get_path("graphics/")
