import pathlib


def _get_files(folder: str) -> list[str]:
    return [str(f).replace("\\", "/") for f in pathlib.Path(folder).iterdir() if f.is_file()]


photo_path: str = "photo"
photo_list: list[str] = _get_files(photo_path)
photof_paht: str = "photof"
photof_list: list[str] = _get_files(photof_paht)
