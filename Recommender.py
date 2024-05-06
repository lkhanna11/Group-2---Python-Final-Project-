# Authors : Alexander Beke , Latika Khanna, Zijie Ma
# Date : May 5, 2024
# Description : This program contains the functions for navigating and loading data into the Media Library

import os
import tkinter.filedialog
import tkinter.messagebox

import matplotlib.pyplot as plt
from collections import Counter

from Book import Book
from Media import Media
from Show import Show

class Recommender:
    def __init__(self):
        self.books = {} # Book ID is the key, value is the object (1)
        self.shows = {} # Show ID is the key, value is the object (2)
        self.associations = {} # Show or Book ID is the key, value is INNNER DICTIONARY (3)
            # INNER DICTIONARY:
            # key: show/book ID
            # value: number of times the outer ID and inner ID are associated

    # LoadBooks and Shows use the same framework
    def loadBooks(self):
        booksFile = tkinter.filedialog.askopenfilename(title="Choose a book file to load from", initialdir=os.getcwd())
        while not os.path.exists(f"{booksFile}"):
            booksFile = tkinter.filedialog.askopenfilename(title="Choose a book file to load from", initialdir=os.getcwd())

        with open(booksFile,'r') as f:
            lines = f.readlines()[1:]

        for line in lines:
            strippedLine = line.strip()
            item = strippedLine.split(",")
            for x in item:
                self.books[item[0]] = Book(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10])
        return

    def loadShows(self):
        showsFile = tkinter.filedialog.askopenfilename(title="Choose a show file to load from", initialdir=os.getcwd())
        while not os.path.exists(f"{showsFile}"):
            showsFile = tkinter.filedialog.askopenfilename(title="Choose a show file to load from", initialdir=os.getcwd())

        with open(showsFile,'r') as f:
            lines = f.readlines()[1:]
        
        for line in lines:
            strippedLine = line.strip()
            item = strippedLine.split(",")
            for x in item:

                # Create a small thing that splits the "Duration" entry into 2 parts
                # Use the first part (the number) for the duration value
                duration = item[10].split(" ")
                item[10] = duration[0]

                self.shows[item[0]] = Show(item[0], item[1], item[2], item[3], item[4], item[5], item[6],
                                           item[7], item[8], item[9], item[10], item[11], item[12])
        return

    def loadAssociations(self):
        assocFile = tkinter.filedialog.askopenfilename(title="Choose a show file to load from", initialdir=os.getcwd())
        while not os.path.exists(f"{assocFile}"):
            assocFile = tkinter.filedialog.askopenfilename(title="Choose a show file to load from", initialdir=os.getcwd())


        assocLines = open(f"{assocFile}", "r")
        for line in assocLines:
            split_line = line.strip().split(",")
            first_id = split_line[0]
            second_id = split_line[1]

            # Update dictionary for first_id
            if first_id not in self.associations:
                self.associations[first_id] = {second_id: 1}
            else:
                if second_id in self.associations[first_id]:
                    self.associations[first_id][second_id] += 1
                else:
                    self.associations[first_id][second_id] = 1

            # Update dictionary for second_id
            if second_id not in self.associations:
                self.associations[second_id] = {first_id: 1}
            else:
                if first_id in self.associations[second_id]:
                    self.associations[second_id][first_id] += 1
                else:
                    self.associations[second_id][first_id] = 1
        assocLines.close()
        return

    # GetLists use the same framework
    def getMovieList(self):
        # Returns Title and Runtime for ALL stored movies, such that:
        # Data has the header Title and Movie
        # All the data is in neat, even columns, whose width is determined
        # based on the length of the entries in the data
        movies = []
        title_max_length = 0
        for key in self.shows:
            if self.shows[key].get_type() == "Movie":
                title_max_length = max(title_max_length, len(self.shows[key].get_title()))
                movies.append((self.shows[key].get_title(), self.shows[key].get_duration()))
        if not movies:
            return
        else:
            movies_string = format("Title", f"{title_max_length + 2}") + "Duration" + "\n"
            for title, duration in movies:
                movies_string += format(title, f"{title_max_length + 2}")
                movies_string += duration
                movies_string += "\n"

            return movies_string

    def getTVList(self):
        # Returns Title and Seasons for ALL stored shows, such that:
        # Data has the header Title and Seasons
        # All the data is in neat, even columns, whose width is determined
        # based on the length of the entries in the data
        tv_shows = []
        title_max_length = 0
        for key in self.shows:
            if self.shows[key].get_type() == "TV Show":
                title_max_length = max(title_max_length, len(self.shows[key].get_title()))
                tv_shows.append((self.shows[key].get_title(), self.shows[key].get_duration()))
        if not tv_shows:
            return
        else:
            tv_shows_string = format("Title", f"{title_max_length + 2}") + "Seasons" + "\n"
            for title, seasons in tv_shows:
                tv_shows_string += format(title, f"{title_max_length + 2}")
                tv_shows_string += seasons
                tv_shows_string += "\n"

            return tv_shows_string

    def getBookList(self):
        # Returns Title and Author(s) for ALL stored books, such that:
        # Data has the header Title and Author(s)
        # All of the data is in neat, even columns, whose width is determined
        # based on the length of the entries in the data
        books = []
        title_max_length = 0
        for key in self.books:
            title_max_length = max(title_max_length, len(self.books[key].get_title()))
            books.append((self.books[key].get_title(), self.books[key].get_authors()))
        if not books:
            return
        else:
            books_string = format("Title", f"{title_max_length + 2}") + "Authors" + "\n"
            for title, author in books:
                books_string += format(title, f"{title_max_length + 2}")
                books_string += author
                books_string += "\n"

            return books_string

    # GetStats use the same framework
    def getMovieStats(self):
        # Returns statistics regarding movies, such as:

        # Rating for movies (G, PG, R, etc…) and the number of times a particular rating appears
        # as a percentage of all the ratings for movies, with two decimals of precision
   
        movieRatings = {}
        num_of_movies = 0
        for key in self.shows:
            if self.shows[key].get_type() == "Movie":
                if self.shows[key].get_showRating() not in movieRatings:
                    movieRatings[self.shows[key].get_showRating()] = 1
                else:
                    movieRatings[self.shows[key].get_showRating()] += 1
            num_of_movies += 1

        ratings = "Ratings:\n"
        for rating in movieRatings:
            ratingPercent = (movieRatings[rating] / num_of_movies) * 100
            ratings += f"{rating if rating else 'Not rated'} -" +  f"{ratingPercent:.2f}%\n"
            # Add 2 decimals of precision
        

        # Average movie duration in minutes, with two decimals of precision
        durationTotal = 0
        num_of_movies = 0
        for key in self.shows:
            if self.shows[key].get_type() == "Movie":
                durationTotal += int(self.shows[key].get_duration().split(" ")[0])
                num_of_movies += 1
        avgMovieDuration = durationTotal / num_of_movies
        # Add 2 decimals of precision
        
        duration_stats = "\nAverage movie duration:" +  f"{avgMovieDuration:.2f} minutes\n"

        # The director who has directed the most movies
        
        directorCount = {}
        for key in self.shows:
            director = self.shows[key].get_director()
            if director:
                if director not in directorCount:
                    directorCount[director] = 1
                else:
                    directorCount[director] += 1
                
        # get director with highest number of movies
        director_max = max(directorCount, key=directorCount.get)
        director_with_max_movies = f"\n{director_max} is the most prolific director in Movies \n"

        # The actor who has acted in the most movies
        actorCount = {}
        for key in self.shows:
            actor = self.shows[key].get_actor()
            if actor:
                if actor not in actorCount:
                    actorCount[actor] = 1
                else:
                    actorCount[actor] += 1
        
        # get actor with highest number of movies
        actor_max = max(actorCount, key=actorCount.get)
        actor_with_max_movies = f"\n{actor_max} is the most prolific actor in Movies \n"

        # The most frequent movie genre across the movie library
        genreCount = {}
        for key in self.shows:
            genre = self.shows[key].get_genre()
            if genre not in genreCount:
                genreCount[genre] = 1
            else:
                genreCount[genre] += 1
        
        # get genre with highest number of movies
        genre_max = max(genreCount, key=genreCount.get)
        most_freq_genre = f"\nMost frequent genre is {genre_max}"

        return ratings + duration_stats + director_with_max_movies + actor_with_max_movies + most_freq_genre


    def getTVStats(self):
        # Returns the statistics regarding TV shows, such as:
        # Rating for TV shows (G, PG, R, etc…) and the number of times a particular rating appears
        # as a percentage of all the ratings for tv shows, with two decimals of precision
        TV_Ratings = {}
        num_of_TVShows = 0
        for key in self.shows:
            if self.shows[key].get_type() == "TV Show":
                if self.shows[key].get_showRating() not in TV_Ratings:
                    TV_Ratings[self.shows[key].get_showRating()] = 1
                else:
                    TV_Ratings[self.shows[key].get_showRating()] += 1
            num_of_TVShows += 1

        ratings = "Ratings:\n"
        for rating in TV_Ratings:
            ratingPercent = (TV_Ratings[rating] / num_of_TVShows) * 100
            ratings += f"{rating if rating else 'Not rated'} :" + f"{ratingPercent:.2f}%\n"
            # Add 2 decimals of precision

        # Average number of seasons, with two decimals of precision
        durationTotal = 0
        num_of_TVShows = 0
        for key in self.shows:
            if self.shows[key].get_type() == "TV Show":
                durationTotal += int(self.shows[key].get_duration().split(" ")[0])
                num_of_TVShows += 1
        avgSeasons = durationTotal / num_of_TVShows
        # Add 2 decimals of precision

        Season_stats = "\nAverage number of Seasons:" + f"{avgSeasons:.2f} Seasons\n"

        # The actor who has acted in the most TV Shows
        actorCount = {}
        for key in self.shows:
            actor = self.shows[key].get_actor()
            if actor:
                if actor not in actorCount:
                    actorCount[actor] = 1
                else:
                    actorCount[actor] += 1

        # get actor with highest number of movies
        actor_max = max(actorCount, key=actorCount.get)
        actor_with_max_TV_shows = f"\n{actor_max} is the most prolific actor in TV Shows \n"

        # The most frequent TV Show genre across the movie library
        genreCount = {}
        for key in self.shows:
            genre = self.shows[key].get_genre()
            if genre not in genreCount:
                genreCount[genre] = 1
            else:
                genreCount[genre] += 1

        # get genre with highest number of movies
        genre_max = max(genreCount, key=genreCount.get)
        most_freq_genre = f"\nMost frequent genre is {genre_max}"

        return ratings + Season_stats + actor_with_max_TV_shows + most_freq_genre


    def getBookStats(self):
        # Returns the statistics regarding Books, such as:

        # The average page count, with two decimals of precision
        pagesTotal = 0
        num_of_Books = 0
        for key in self.books:
            pagesTotal += int(self.books[key].get_pages())
            num_of_Books += 1
        avgPageCount = pagesTotal / num_of_Books
        # Add 2 decimals of precision

        Books_stats = "\nAverage number of Pages per book:" + f"{avgPageCount:.2f} \n"

        # The author who has written the most books
        authorCount = {}
        for key in self.books:
            author = self.books[key].get_authors()
            if author:
                if author not in authorCount:
                    authorCount[author] = 1
                else:
                    authorCount[author] += 1

        # get author with highest number of books
        author_max = max(authorCount, key=authorCount.get)
        author_with_max_Books = f"\n{author_max} has written most number of books \n"

        # The publisher with most number of books
        published_books_Count = {}
        for key in self.books:
            publisher = self.books[key].get_publisher()
            if publisher not in published_books_Count:
                published_books_Count[publisher] = 1
            else:
                published_books_Count[publisher] += 1

        # get publisher with most number of books
        publisher_max = max(published_books_Count, key=published_books_Count.get)
        most_freq_publisher = f"\n{publisher_max} has published most number of books \n"

        return Books_stats + author_with_max_Books + most_freq_publisher

    # Searches use the same framework
    def searchTVMovies(self, choiceMovieTV, title, director, actor, genre):
        # Returns information regarding movies and shows, such that:

        # If the string representing the movie or tv show is neither Movie nor TV Show, spawn a
        # showerror messagebox and inform the user the need to select Movie or TV Show
        # from Type first, and return the string No Results
        if choiceMovieTV not in ["Movie", "TV Show"]:
            tkinter.messagebox.showerror(title="Invalid type", message="Please select either Movie or TV Show!")
            return "No Results"

        # If the strings representing title, director, actor, and genre are all empty, spawn a
        # showerror messagebox and inform the user the need to enter information for the
        # Title, Directory, Actor and/or Genre first, and return the string No Results
        if title == "" and director == "" and actor == "" and genre == "":
            tkinter.messagebox.showerror(title="Invalid entries", message="Please enter category information!")
            return "No Results"

        if not self.shows:
            return "No Data has been loaded yet"

        # Otherwise, search through the dictionary of shows and select all objects that adhere to
        # the user’s data
        title_list = []
        director_list = []
        actor_list = []
        genre_list = []

        Search_result_string = ""
        title_max_length = 0
        director_max_length = 0
        actor_max_length = 0
        genre_max_length = 0

        for key in self.shows:
            title_max_length = max(title_max_length, len(self.shows[key].get_title()))
            director_max_length = max(director_max_length, len(self.shows[key].get_director()))
            actor_max_length = max(actor_max_length, len(self.shows[key].get_actor()))
            genre_max_length = max(genre_max_length, len(self.shows[key].get_genre()))

            if choiceMovieTV == "Movie" and self.shows[key].get_type() == "Movie":
                if title and title == self.shows[key].get_title():
                    title_list.append(self.shows[key].get_title())
                    director_list.append(self.shows[key].get_director())
                    actor_list.append(self.shows[key].get_actor())
                    genre_list.append(self.shows[key].get_genre())

                if director != "" and director == self.shows[key].get_director():
                    title_list.append(self.shows[key].get_title())
                    director_list.append(self.shows[key].get_director())
                    actor_list.append(self.shows[key].get_actor())
                    genre_list.append(self.shows[key].get_genre())

                if actor != "" and actor in str(self.shows[key].get_actor()):
                    title_list.append(self.shows[key].get_title())
                    director_list.append(self.shows[key].get_director())
                    actor_list.append(self.shows[key].get_actor())
                    genre_list.append(self.shows[key].get_genre())

                if genre != "" and genre in str(self.shows[key].get_genre()):
                    title_list.append(self.shows[key].get_title())
                    director_list.append(self.shows[key].get_director())
                    actor_list.append(self.shows[key].get_actor())
                    genre_list.append(self.shows[key].get_genre())

            elif choiceMovieTV == "TV Show" and self.shows[key].get_type() == "TV Show":
                if title and title == self.shows[key].get_title():
                    title_list.append(self.shows[key].get_title())
                    director_list.append(self.shows[key].get_director())
                    actor_list.append(self.shows[key].get_actor())
                    genre_list.append(self.shows[key].get_genre())

                if director != "" and director == self.shows[key].get_director():
                    title_list.append(self.shows[key].get_title())
                    director_list.append(self.shows[key].get_director())
                    actor_list.append(self.shows[key].get_actor())
                    genre_list.append(self.shows[key].get_genre())

                if actor != "" and actor == self.shows[key].get_actor():
                    title_list.append(self.shows[key].get_title())
                    director_list.append(self.shows[key].get_director())
                    actor_list.append(self.shows[key].get_actor())
                    genre_list.append(self.shows[key].get_genre())

                if genre != "" and genre == self.shows[key].get_genre():
                    title_list.append(self.shows[key].get_title())
                    director_list.append(self.shows[key].get_director())
                    actor_list.append(self.shows[key].get_actor())
                    genre_list.append(self.shows[key].get_genre())

        Search_result_string += format("Title", f"{title_max_length + 2}")
        Search_result_string += format("Director", f"{director_max_length + 2}")
        Search_result_string += format("Actor", f"{actor_max_length + 2}")
        Search_result_string += format("Genre", f"{genre_max_length + 2}")
        Search_result_string += "\n"

        for i in range(len(title_list)):
            Search_result_string += format(title_list[i], f"{title_max_length + 2}")
            Search_result_string += format(director_list[i], f"{director_max_length+ 2}")
            Search_result_string += format(actor_list[i], f"{actor_max_length+2}")
            Search_result_string += format(genre_list[i], f"{genre_max_length+ 2}")
            Search_result_string += "\n"

        return Search_result_string


    def searchBooks(self, title, author, publisher):
        # Returns information regarding books, such that:

        # If the strings representing title, author, and publisher are all empty, spawn a
        # showerror messagebox and inform the user the need to enter information for the
        # Title, Author, and/or Publisher first, and return the string No Results
        if title == "" and author == "" and publisher == "":
            tkinter.messagebox.showerror(title="Invalid entries", message="Please enter category information!")
            return "No Results"

        if not self.books:
            return "No Data has been loaded yet"

        # Otherwise, search through the dictionary of shows and select all objects that adhere to
        # the user’s data
        title_list = []
        author_list = []
        publisher_list = []

        Search_result_string = ""
        title_max_length = 0
        author_max_length = 0
        publisher_max_length = 0

        for key in self.books:
            title_max_length = max(title_max_length, len(self.books[key].get_title()))
            author_max_length = max(author_max_length, len(self.books[key].get_authors()))
            publisher_max_length = max(publisher_max_length, len(self.books[key].get_publisher()))

            if title and title == self.books[key].get_title():
                title_list.append(self.books[key].get_title())
                author_list.append(self.books[key].get_authors())
                publisher_list.append(self.books[key].get_publisher())

            if author and author == self.books[key].get_authors():
                title_list.append(self.books[key].get_title())
                author_list.append(self.books[key].get_authors())
                publisher_list.append(self.books[key].get_publisher())

            if publisher != "" and publisher == self.books[key].get_publisher():
                title_list.append(self.books[key].get_title())
                author_list.append(self.books[key].get_authors())
                publisher_list.append(self.books[key].get_publisher())

        Search_result_string += format("Title", f"{title_max_length + 2}")
        Search_result_string += format("Author", f"{author_max_length + 2}")
        Search_result_string += format("Publisher", f"{publisher_max_length + 2}")
        Search_result_string += "\n"

        for i in range(len(title_list)):
            Search_result_string += format(title_list[i], f"{title_max_length + 2}")
            Search_result_string += format(author_list[i], f"{author_max_length + 2}")
            Search_result_string += format(publisher_list[i], f"{publisher_max_length+2}")
            Search_result_string += "\n"

        return Search_result_string


    def getRecommendations(self, type, title):
        # returns a string containing recommendations regarding Movies, TV Shows, or Books:

        # If the type is Movie or TV Show, search through the shows dictionary and determine the
        # id associated with that title
        recommendationResult = ""
        movie_TV_ID = None
        book_ID = None

        if type == "Movie" or type == "TV Show":
            for key in self.shows:
                if title == self.shows[key].get_title():
                    movie_TV_ID = self.shows[key].get_id()

            if movie_TV_ID == None:
                tkinter.messagebox.showwarning(title="Warning",
                                                       message="There are no recommendations for that title.")
                return "No Results"

            rec_books = self.associations[movie_TV_ID]

            for I_D in rec_books.keys():
                recommendationResult += "Title: " + f"{self.books[I_D].get_title()}\n\n"
                recommendationResult += "Author: " + f"{self.books[I_D].get_authors()}\n\n"
                recommendationResult += "Average Rating: " + f"{self.books[I_D].get_rating()}\n\n"
                recommendationResult += "ISBN: " + f"{self.books[I_D].get_isbnNum()}\n\n"
                recommendationResult += "ISBN 13: " + f"{self.books[I_D].get_isbn13()}\n\n"
                recommendationResult += "Language Code: " + f"{self.books[I_D].get_language()}\n\n"
                recommendationResult += "Number of Pages: " + f"{self.books[I_D].get_pages()}\n\n"
                recommendationResult += "Rating Number: " + f"{self.books[I_D].get_rating_number()}\n\n"
                recommendationResult += "Publication: " + f"{self.books[I_D].get_publication()}\n\n"
                recommendationResult += "Publisher: " + f"{self.books[I_D].get_publisher()}\n\n"
                recommendationResult += "****************************************************\n\n"

            return recommendationResult

        if type == "Book":
            for key in self.books:
                if title == self.books[key].get_title():
                    book_ID = self.books[key].get_id()

            if book_ID == None:
                tkinter.messagebox.showwarning(title="Warning",
                                               message="There are no recommendations for that title.")
                return "No Results"

            rec_shows = self.associations[book_ID]

            for I_D in rec_shows.keys():
                recommendationResult += "Title: " + f"{self.shows[I_D].get_title()}\n\n"
                recommendationResult += "Director: " + f"{self.shows[I_D].get_director()}\n\n"
                recommendationResult += "Actor(s): " + f"{self.shows[I_D].get_actor()}\n\n"
                recommendationResult += "Average Rating: " + f"{self.shows[I_D].get_rating()}\n\n"
                recommendationResult += "Country: " + f"{self.shows[I_D].get_country()}\n\n"
                recommendationResult += "Date Added: " + f"{self.shows[I_D].get_added_date()}\n\n"
                recommendationResult += "Release year: " + f"{self.shows[I_D].get_released_year()}\n\n"
                recommendationResult += "Show Rating: " + f"{self.shows[I_D].get_showRating()}\n\n"
                recommendationResult += "Duration: " + f"{self.shows[I_D].get_duration()}\n\n"
                recommendationResult += "Genre: " + f"{self.shows[I_D].get_genre()}\n\n"
                recommendationResult += "Description: " + f"{self.shows[I_D].get_description()}\n\n"
                recommendationResult += "****************************************************\n\n"

            return recommendationResult
