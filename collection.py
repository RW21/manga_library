import json
import os

import manga_manage
from generate_metadata import metadata


def scan_book(file_path):
    return [file for file in os.listdir(file_path)]


class Collection:

    def __init__(self, file_path, index):
        index: int

        self.book_list = scan_book(file_path)
        self.file_path = file_path
        self.collection_name = os.path.basename(file_path)
        self.index = index

        self.author = self.collection_name[self.collection_name.find("[") + 1:
                                           self.collection_name.find("]")]

        if ('(' and ')') in self.collection_name:
            self.category = self.collection_name[self.collection_name.find("(") + 1:
                                                 self.collection_name.find(")")]
        else:
            self.category = ''

        self.name = self.collection_name.split(']')[1]

        # todo Change language from settings.
        self.metadata = metadata('JP', file_path)

        # self.summary = metadata('')

    def __getitem__(self, item):
        return self.book_list[item]

    def __len__(self):
        return len(self.book_list)

    def __str__(self):
        return self.collection_name

    def update_json(self):
        # todo Only works when there is existing data in json.

        json_dic = self.export_dict()
        with open('data.json') as f:
            data = json.load(f)

        data[self.index] = json_dic

        with open('data.json', 'w') as f:
            json.dump(data, f)

    # def import_from_json(self):

    def export_dict(self) -> dict:
        return {
            "collection name": self.collection_name,
            "name": self.name,
            "author": self.author,
            "book list": self.book_list,
            "category": self.category,
            "summary": self.metadata.get_summary()
        }

    def move_collection(self, destination):
        os.rename(self.file_path, destination)

        # update file destination and update json
        self.file_path = destination
        self.update_json()

        # todo error handling, is file open?

    def import_manga(self, file, auto_archive = True):
        # move file
        collection_type = manga_manage.get_collection_type(file)

        if collection_type == 'image folder':
            new_file_name = manga_manage.make_archive(file)

            os.rename(new_file_name, self.file_path)
            self.book_list.append(os.path.basename(str(new_file_name)))

        elif collection_type == 'manga':
            os.rename(file, self.file_path)
            self.book_list.append()

        elif collection_type == 'archive folder':
            for file_ in os.listdir(file):
                os.rename(file_, self.file_path)
                self.book_list.append()







# a = Collection(r'C:\Users\RW\Desktop\code\manga_library\test\[あらゐけいいち] 日常', 1)
# print(a.author)
# print(a.name)
# a.update_json()
#
# b = Collection(r'C:\Users\RW\Desktop\code\manga_library\test\[あばば] 非日常', 2)
# b.update_json()
