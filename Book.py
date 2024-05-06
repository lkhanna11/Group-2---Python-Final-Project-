# Authors : Alexander Beke , Latika Khanna, Zijie Ma
# Date : May 5, 2024
# Description : This program contains the Book Class for the Media Library


from Media import Media

class Book(Media):
    def __init__(self,bookID,title,authors,average_rating,isbn,isbn13,language,pages,rating_number,publication,publisher):
        super().__init__(bookID,title,average_rating)
        self.__authors = authors
        self.__isbnNum = isbn
        self.__isbn13 = isbn13
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

    def get_isbn13(self):
        return self.__isbn13

    def set_isbn13(self, value):
        self.__isbn13 = value

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





