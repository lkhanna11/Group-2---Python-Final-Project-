#
#   LAST UPDATED: THURSDAY 5/2
#   COMMENTS HAVE PLANNED FUNCTIONALITY
#   "x = 1" is just placeholder code so empty functions don't give error messages
#
# To do:
# - Complete minor adjustment to "loadShows" (the duration entry is not just a number)
# - Complete second portion loadAssociations
# - Complete first portion of getMovieStats and getTVStats
# - Test searchTVMovies and searchBooks
#     (I'm not sure what they mean by "columns" in relation to the string, and having each title on top of it)
# - Complete getRecommendations

import os
import tkinter.filedialog
import tkinter.messagebox

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

        booksLines = open(f"{booksFile}", "r")
        for line in booksLines:
            strippedLine = line.strip()
            item = strippedLine.split(",")
            for x in item:
                self.books[item[0]] = Book(item[0], item[1], item[3], item[2], item[4], item[6], item[7], item[3], item[9], item[10])
        booksLines.close()

    def loadShows(self):
        showsFile = tkinter.filedialog.askopenfilename(title="Choose a show file to load from", initialdir=os.getcwd())
        while not os.path.exists(f"{showsFile}"):
            showsFile = tkinter.filedialog.askopenfilename(title="Choose a show file to load from", initialdir=os.getcwd())

        showsLines = open(f"{showsFile}", "r")
        for line in showsLines:
            strippedLine = line.strip()
            item = strippedLine.split(",")
            for x in item:

                # Create a small thing that splits the "Duration" entry into 2 parts
                # Use the first part (the number) for the duration value

                self.shows[item[0]] = Show(item[0], item[2], item[5], item[1], item[3], item[4], item[6],
                                           item[7], item[8], item[9], item[10], item[11], item[12])
        showsLines.close()

    def loadAssociations(self):
        assocFile = tkinter.filedialog.askopenfilename(title="Choose a show file to load from", initialdir=os.getcwd())
        while not os.path.exists(f"{assocFile}"):
            assocFile = tkinter.filedialog.askopenfilename(title="Choose a show file to load from", initialdir=os.getcwd())

        assocLines = open({f"{assocFile}", "r"})
        for line in assocLines:
            strippedLine = line.strip()
            item = strippedLine.split(",")
            for x in item:
                y = 1
                # Using the first ID as a key, determine if there is a dictionary associated with it
                    # If nothing is found, create a new dictionary, add the second ID to the new dictionary
                    # The second ID must be associated with the value 1
                # Otherwise, determine if the second ID is a key in the second dictionary
                    # If it is, increment count associated with it by 1
                    # Otherwise, set the count associated with it to 1
        # Do this again, but this time with
            # The second ID for the outer dictionary
            # The first ID for the inner dictionary
        # Close the file once all the data has been read in

    # GetLists use the same framework
    def getMovieList(self):
        # Returns Title and Runtime for ALL stored movies, such that:
        # Data has the header Title and Movie
        # All of the data is in neat, even columns, whose width is determined
        # based on the length of the entries in the data
        for key in self.shows:
            if self.shows[key][3] == "Movie":
                print(f"{self.shows[key][1]}, {self.shows[key][-3]}")
        return

    def getTVList(self):
        # Returns Title and Seasons for ALL stored shows, such that:
        # Data has the header Title and Seasons
        # All of the data is in neat, even columns, whose width is determined
        # based on the length of the entries in the data
        for key in self.shows:
            if self.shows[key][3] == "TV Show":
                print(f"{self.shows[key][1]}, {self.shows[key][-3]}")
        return

    def getBookList(self):
        # Returns Title and Author(s) for ALL stored books, such that:
        # Data has the header Title and Author(s)
        # All of the data is in neat, even columns, whose width is determined
        # based on the length of the entries in the data
        for key in self.books:
            print(f"{self.books[key][1]}, {self.books[key][3]}")
        return


    # GetStats use the same framework
    def getMovieStats(self):
        # Returns statistics regarding movies, such as:

        # Currently needs to be implemented
        # Rating for movies (G, PG, R, etc…) and the number of times a particular rating appears
            # as a percentage of all of the ratings for movies, with two decimals of precision

        # This is incomplete, refer to Project 2 document
        increment = 0
        for key in self.shows:
            if self.shows[key][3] == "Movie":

                increment += 1

        # Average movie duration in minutes, with two decimals of precision
        durationAccumulator = 0
        durationIncrement = 0
        for key in self.shows:
            if self.shows[key][3] == "Movie":
                durationAccumulator += self.shows[key][-2]
                durationIncrement += 1
        avgMovieDuration = durationAccumulator / durationIncrement
        # Add 2 decimals of precision

        # The director who has directed the most movies
        directorCount = {}
        for key in self.shows:
            if self.shows[key][3] == "Movie":
                if self.shows[key][4] in directorCount:
                    directorCount[f"{self.shows[key][4]}"] += 1
                else:
                    directorCount[f"{self.shows[key][4]}"] = 0
        print(max(directorCount, key=directorCount.get))

        # The actor who has acted in the most movies
        actorCount = {}
        for key in self.shows:
            if self.shows[key][3] == "Movie":
                if self.shows[key][11] in actorCount:
                    actorCount[f"{self.shows[key][11]}"] += 1
                else:
                    actorCount[f"{self.shows[key][11]}"] = 0
        print(max(actorCount, key=actorCount.get))

        # The most frequent movie genre across the movie library
        genreCount = {}
        for key in self.shows:
            if self.shows[key][3] == "Movie":
                if self.shows[key][5] in genreCount:
                    genreCount[f"{self.shows[key][5]}"] += 1
                else:
                    genreCount[f"{self.shows[key][5]}"] = 0
        print(max(genreCount, key=genreCount.get))

        return


    def getTVStats(self):
        # Returns the statistics regarding TV shows, such as:

        # Currently needs to be implemented
        # Rating for TV shows (G, PG, R, etc…) and the number of times a particular rating appears
            # as a percentage of all of the ratings for tv shows, with two decimals of precision

        # Average number of seasons for tv shows, with two decimals of precision
        durationAccumulator = 0
        durationIncrement = 0
        for key in self.shows:
            if self.shows[key][3] == "TV Show":
                durationAccumulator += self.shows[key][-2]
                durationIncrement += 1
        avgMovieDuration = durationAccumulator / durationIncrement
        # Add 2 decimals of precision

        # The actor who has acted in the most tv shows
        actorCount = {}
        for key in self.shows:
            if self.shows[key][3] == "TV Show":
                if self.shows[key][11] in actorCount:
                    actorCount[f"{self.shows[key][11]}"] += 1
                else:
                    actorCount[f"{self.shows[key][11]}"] = 0
        print(max(actorCount, key=actorCount.get))

        # The most frequent tv show genre across the TV show library
        genreCount = {}
        for key in self.shows:
            if self.shows[key][3] == "TV Show":
                if self.shows[key][5] in genreCount:
                    genreCount[f"{self.shows[key][5]}"] += 1
                else:
                    genreCount[f"{self.shows[key][5]}"] = 0
        print(max(genreCount, key=genreCount.get))

        return


    def getBookStats(self):
        # Returns the statistics regarding Books, such as:

        # The average page count, with two decimals of precision
        pageAccumulator = 0
        pageIncrementer = 0
        for key in self.books:
            pageAccumulator += self.books[key][6]
            pageIncrementer += 1
        avgPageCount = pageAccumulator / pageIncrementer
        # Add 2 decimals of precision

        # The author who has written the most books
        authorCount = {}
        for key in self.books:
            if self.books[key][3] in authorCount:
                authorCount[f"{self.books[key][3]}"] += 1
            else:
                authorCount[f"{self.books[key][3]}"] = 0
        print(max(authorCount, key=authorCount.get))

        # The publisher who has published the most books
        publisherCount = {}
        for key in self.books:
            if self.books[key][9] in publisherCount:
                publisherCount[f"{self.books[key][9]}"] += 1
            else:
                publisherCount[f"{self.books[key][9]}"] = 0
        print(max(publisherCount, key=publisherCount.get))

        return

    # Searches use the same framework
    def searchTVMovies(self, choiceMovieTV, title, director, actor, genre):
        # Returns information regarding movies and shows, such that:

        # If the string representing the movie or tv show is neither Movie nor TV Show, spawn a
        # showerror messagebox and inform the user the need to select Movie or TV Show
        # from Type first, and return the string No Results
        if choiceMovieTV is not ("Movie" or "TV Show"):
            tkinter.messagebox.showerror(title="Invalid type", message="Please select either Movie or TV Show!")
            return "No Results"

        # If the strings representing title, director, actor, and genre are all empty, spawn a
        # showerror messagebox and inform the user the need to enter information for the
        # Title, Directory, Actor and/or Genre first, and return the string No Results
        if title == "" and director == "" and actor == "" and genre == "":
            tkinter.messagebox.showerror(title="Invalid entries", message="Please enter category information!")
            return "No Results"

        # Otherwise, search through the dictionary of shows and select all objects that adhere to
        # the user’s data
        movieSearchString = ""
        for key in self.shows:
            if title in self.shows[key][1] and director in self.shows[key][4] and actor in self.shows[key][5] and genre in self.shows[key][11]:
                movieSearchString += f"Title: {self.shows[key][1]}\n"
                movieSearchString += f"Director: {self.shows[key][4]}\n"
                movieSearchString += f"Actor: {self.shows[key][5]}\n"
                movieSearchString += f"Genre: {self.shows[key][11]}\n"
                movieSearchString += "\n"
        # Return a string containing the Title, Director, Actors, and Genre (with those titles at the
        # top) in neat, even columns, whose width is determined based on the length of the
        # entries in the data
        return movieSearchString

    def searchBooks(self, title, author, publisher):
        # Returns information regarding books, such that:

        # If the strings representing title, author, and publisher are all empty, spawn a
        # showerror messagebox and inform the user the need to enter information for the
        # Title, Author, and/or Publisher first, and return the string No Results
        if title == "" and author == "" and publisher == "":
            tkinter.messagebox.showerror(title="Invalid entries", message="Please enter category information!")
            return "No Results"

        # Otherwise, search through the dictionary of books and select all objects that adhere to
        # the user’s data
        bookSearchString = ""
        for key in self.books:
            if title in self.books[key][1] and author in self.books[key][3] and publisher in self.books[key][9]:
                bookSearchString += f"Title: {self.books[key][1]}\n"
                bookSearchString += f"Author(s): {self.books[key][3]}\n"
                bookSearchString += f"Publisher: {self.books[key][9]}\n"
                bookSearchString += "\n"
        # Return a string containing the Title, Author, and Publisher (with those titles at the top)
        # in neat, even columns, whose width is determined based on the length of the entries in the data
        return bookSearchString

    def getReccomendations(self, type, title):
        x = 1
        # returns a string containing recommendations regarding Movies, TV Shows, or Books:

        # If the type is Movie or TV Show, search through the shows dictionary and determine the
        # id associated with that title
            # If the title is not in the dictionary, spawn a showwarning messagebox
            # informing the user that there are no recommendations for that title, and return
            # No results
            # Otherwise, using that movie or tv show id, determine all of the books associated
            # with that id in the association dictionary, and return a string containing all of the
            # information for each book with appropriate titles for each piece of information
        # If the type is Book, search through the books dictionary and determine the id associated
        # with that title
            # If the title is not in the dictionary, spawn a showwarning messagebox
            # informing the user that there are no recommendations for that title, and return
            # No results
            # Otherwise, using that book id, determine all of the movies and tv shows
            # associated with that id in the association dictionary, and return a string
            # containing all of the information for each movie or tv show with appropriate
            # titles for each piece of information
