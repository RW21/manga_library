import wikipedia
import google_images_download


class metadata():

    def __init__(self, language, ):
        # self.wikipedia = wikipedia
        wikipedia.set_lang(language)
        
        response = google_images_download.googleimagesdownload()


    def get_summary(self,name):
        return wikipedia.summary(name)

    # def get_cover(self, name):
        






a = metadata('jp')
print(a.get_summary('ONE PIECE'))

