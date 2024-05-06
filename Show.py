# Authors : Alexander Beke , Latika Khanna, Zijie Ma
# Date : May 5, 2024
# Description : This program contains the Show Class for the Media Library


from Media import Media

class Show(Media):
    def __init__(self, show_id,type,title,director,actor,average_rating,country,added_date,released_year,showRating,duration,genre,description):
        super().__init__(show_id, title, average_rating)
        self.__type = type
        self.__director = director
        self.__actor = actor
        self.__country = country
        self.__added_date = added_date
        self.__released_year = released_year
        self.__duration = duration
        self.__description = description
        self.__showRating = showRating
        self.__genre = genre

    def get_type(self):
        return self.__type

    def set_type(self, value):
        self.__type = value

    def get_director(self):
        return self.__director

    def set_director(self, value):
        self.__director = value

    def get_actor(self):
        return self.__actor

    def set_actor(self, value):
        self.__actor = value

    def get_country(self):
        return self.__country

    def set_country(self, value):
        self.__country = value

    def get_added_date(self):
        return self.__added_date

    def set_added_date(self, value):
        self.__added_date = value

    def get_released_year(self):
        return self.__released_year

    def set_released_year(self, value):
        self.__released_year = value

    def get_duration(self):
        return self.__duration

    def set_duration(self, value):
        self.__duration = value

    def get_description(self):
        return self.__description

    def set_description(self, value):
        self.__description = value

    def get_showRating(self):
        return self.__showRating

    def set_showRating(self, value):
        self.__showRating = value

    def get_genre(self):
        return self.__genre

    def set_genre(self, value):
        self.__genre = value
