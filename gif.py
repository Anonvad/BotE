from random import choice

_gif_ids_file = open("resources/gif_ids.txt", "r+")
_gif_ids = _gif_ids_file.readlines()


def random_gif_id() -> str:
    return choice(_gif_ids)


def add_gif(gif_id: str):
    _gif_ids_file.write(gif_id + "\n")
    _gif_ids.append(gif_id)