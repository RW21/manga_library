import os
from pathlib import PurePath

import manage
from collection import Collection


def scan_folder(file: os.path) -> Collection:
    """
    Checks if the folder is a collection or a manga.
    :param file:
    :return: Collection
    """
    if is_supported_filename(file):
        return Collection(file, manage.get_last_index(file))


def is_supported_filename(file: os.path) -> bool:
    """
    Check if filename is supported.
    :param file: file path
    :return:
    """
    if '[' and ']' in os.path.basename(file):
        for file_ in os.listdir(os.path):
            if not os.path.isdir(file_):
                if is_image(file_):
                    return True



    else:
        return False


def is_image(file):
    path = PurePath(file)
    file_format = PurePath.suffix(path)[1:]
    supported_filetype = ['.jpg', '.png']

    for type_ in supported_filetype:
        if type_ == file_format:
            return True
    else:
        return False


def is_archive(file):
    path = PurePath(file)
    file_format = PurePath.suffix(path)[1:]
    supported_filetype = ['.zip', '.rar', '.7zip']

    for type_ in supported_filetype:
        if type_ == file_format:
            return True
    else:
        return False


