import os
import shutil
from pathlib import PurePath

from manga_helper import scan_folder, is_image, is_archive


def import_folder_mixed(path, export_directory):
    for file in os.listdir(path):
        print(file)
        if os.path.isdir(file):
            scan_folder(file).move_collection(export_directory)

        if get_collection_type(path) == 'manga':
            print('a')


def get_collection_type(file) -> str:
    if not os.path.isdir(file):
        # check if file is single manga archive
        if is_archive(file):
            return 'manga'

    else:
        # check if manga folder with image or archives
        # doesn't check if both
        for _file in os.listdir(file):
            if is_image(_file):
                return 'image folder'

            if is_archive(_file):
                return 'archive folder'


def make_archive(file):
    shutil.make_archive(file, 'zip', file)
    # todo safely delete file after compression?

    return get_different_format(file, '.zip')


def get_different_format(file, format) -> PurePath:
    file_: PurePath

    if type(file) == 'PurePath':
        base_file_name = os.path.splitext(os.path.basename(file))[-1]
        file_ = file.parent().joinpath(base_file_name.join(format))

        return format

    else:
        raise NotPurePath


class NotCollection(Exception):
    """When the file is not a collection"""


class NotPurePath(Exception):
    pass


get_different_format()
