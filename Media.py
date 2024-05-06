# Authors : Alexander Beke , Latika Khanna, Zijie Ma
# Date : May 5, 2024
# Description : This program contains the Media Class for the Media Library


class Media:
    def __init__(self,id,title,rating):
        self._id = id
        self._title = title
        self._rating = rating

    def get_id(self):
        return self._id

    def set_id(self,value):
        self._id =value

    def get_title(self):
        return self._title

    def set_tiltle(self,value):
        self._title = value

    def get_rating(self,):
        return self._rating

    def set_rating(self,value):
        self._rating = value

