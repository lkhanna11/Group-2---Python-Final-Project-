from Media import Media

class Show(Media):
    def __init__(self, id, title, rating, type, director, actor, country, added_date, released_year,duration,description):
        super().__init__(id, title, rating)
        self.__type = type
        self.__director = director
        self.__actor = actor
        self.__country = country
        self.__added_date = added_date
        self.__released_year = released_year
        self.__duration = duration
        self.__description = description

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