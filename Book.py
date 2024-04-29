from Media import Media

class Book(Media):
    def __init__(self,id,title,rating,authors,isbnNum, language, pages, rating_number, publication, publisher):
        super().__init__(id,title,rating)
        self.__authors = authors
        self.__isbnNum = isbnNum
        self.__language = language
        self.__pages = pages
        self.__rating_number = rating_number
        self.__publication = publication
        self.__publisher = publisher


    def get_authors(self):
        return self.__authors

    def set_authors(self,value):
        self.__authors =value

    def get_isbnNum(self):
        return self.__isbnNum

    def set_isbnNum(self, value):
        self.__isbnNum = value

    def get_language(self):
        return self.__language

    def set_language(self, value):
        self.__language = value

    def get_pages(self):
        return self.__pages

    def set_pages(self, value):
        self.__pages = value

    def get_rating_number(self):
        return self.__rating_number

    def set_rating_number(self, value):
        self.__rating_number = value

    def get_publication(self):
        return self.__publication

    def set_publication(self, value):
        self.__publication = value

    def get_publisher(self):
        return self.__publisher

    def set_publisher(self, value):
        self.__publisher = value





