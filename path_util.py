import os


def get_path(*paths: str) -> str:
    return os.path.join(PROJECT_DIR, *paths)


def join(base: str, *paths: str):
    return os.path.join(base, *paths)


def iterate_files(directory: str) -> list[str]:
    """
    returns all files from directory  sorted on name
    """
    return [join(directory, file) for file in sorted(os.listdir(directory))]


PROJECT_DIR: str = os.path.dirname(__file__)
GRAPHICS_DIRECTORY: str = get_path("graphics/")
