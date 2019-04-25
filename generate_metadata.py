from zipfile import ZipFile

import wikipedia
from icrawler.builtin import GoogleImageCrawler


class metadata():

    def __init__(self, language, file_path):
        # self.wikipedia = wikipedia
        wikipedia.set_lang(language)
        self.name = file_path
        self.file_path = file_path

    def get_summary(self):
        return wikipedia.summary(self.name)

    def get_cover_internet(self):
        google_crawler = GoogleImageCrawler(storage={'root_dir': 'your_image_dir'})
        google_crawler.crawl(keyword=self.name, max_num=1)

    def get_cover_path(self):
        with ZipFile(self.file_path, 'r') as myzip:
            for name in myzip.infolist():
                print(name.filename.encode('cp437').decode('cp932'))


# a = metadata('jp', 'test/[あらゐけいいち] 日常 第08巻.zip')
# print(a.get_summary())
# a.get_cover('ONE PIECE')
# print(a.get_cover())
