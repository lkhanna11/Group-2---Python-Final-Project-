#
#   LAST UPDATED: FRIDAY 5/4
# To do:
# - Test all functions

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

        booksLines = open(f"{booksFile}", "r")
        for line in booksLines:
            strippedLine = line.strip()
            item = strippedLine.split(",")
            for x in item:
                self.books[item[0]] = Book(item[0], item[1], item[3], item[2], item[4], item[6], item[7], item[3], item[9], item[10])
        booksLines.close()
        return

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
                duration = item[10].split(" ")
                item[10] = duration[0]

                self.shows[item[0]] = Show(item[0], item[2], item[5], item[1], item[3], item[4], item[6],
                                           item[7], item[8], item[9], item[10], item[11], item[12])
        showsLines.close()
        return

    def loadAssociations(self):
        assocFile = tkinter.filedialog.askopenfilename(title="Choose a show file to load from", initialdir=os.getcwd())
        while not os.path.exists(f"{assocFile}"):
            assocFile = tkinter.filedialog.askopenfilename(title="Choose a show file to load from", initialdir=os.getcwd())

        assocLines = open(f"{assocFile}", "r")
        for line in assocLines:
            if line.strip():  # Checking if line is not empty
                first_id, second_id = line.strip().split()

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
        for key in self.shows:
            if self.shows[key][3] == "Movie":
                print(f"{self.shows[key][1]}, {self.shows[key][-3]}")
        return

    def getTVList(self):
        # Returns Title and Seasons for ALL stored shows, such that:
        # Data has the header Title and Seasons
        # All the data is in neat, even columns, whose width is determined
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

        # Rating for movies (G, PG, R, etc…) and the number of times a particular rating appears
        # as a percentage of all the ratings for movies, with two decimals of precision
        movieRatingTotal = 0
        movieRatings = {}
        for key in self.shows:
            if self.shows[key][3] == "Movie":
                if self.shows[key][9] in movieRatings:
                    movieRatings[f"{self.shows[key][9]}"] += 1
                else:
                    movieRatings[f"{self.shows[key][9]}"] = 0
                movieRatingTotal += 1
        for key in movieRatings:
            ratingPercent = movieRatings[key] / movieRatingTotal
            print(f"Rated {key}: {movieRatings[key]} movies ({ratingPercent} of all movies)")
            # Add 2 decimals of precision

        # Average movie duration in minutes, with two decimals of precision
        durationAccumulator = 0
        durationTotal = 0
        for key in self.shows:
            if self.shows[key][3] == "Movie":
                durationAccumulator += self.shows[key][-2]
                durationTotal += 1
        avgMovieDuration = durationAccumulator / durationTotal
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

        # Rating for TV shows (G, PG, R, etc…) and the number of times a particular rating appears
        # as a percentage of all the ratings for tv shows, with two decimals of precision
        showRatingTotal = 0
        showRatings = {}
        for key in self.shows:
            if self.shows[key][3] == "TV Show":
                if self.shows[key][9] in showRatings:
                    showRatings[f"{self.shows[key][9]}"] += 1
                else:
                    showRatings[f"{self.shows[key][9]}"] = 0
                showRatingTotal += 1
        for key in showRatings:
            ratingPercent = showRatings[key] / showRatingTotal
            print(f"Rated {key}: {showRatings[key]} movies ({ratingPercent} of all shows)")
            # Add 2 decimals of precision

        # Average number of seasons for tv shows, with two decimals of precision
        durationAccumulator = 0
        durationTotal = 0
        for key in self.shows:
            if self.shows[key][3] == "TV Show":
                durationAccumulator += self.shows[key][-2]
                durationTotal += 1
        avgMovieDuration = durationAccumulator / durationTotal
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
        pageTotal = 0
        for key in self.books:
            pageAccumulator += self.books[key][6]
            pageTotal += 1
        avgPageCount = pageAccumulator / pageTotal
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
            # add to If statement: If choiceMovieTV is in self.shows[key][2],
            # since we are only taking the selected media type (TV or Movie)
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
        # returns a string containing recommendations regarding Movies, TV Shows, or Books:

        # If the type is Movie or TV Show, search through the shows dictionary and determine the
        # id associated with that title
        recommendationResult = ""
        if type == "Movie" or type == "TV Show":
            for key in self.shows:
                if title in self.shows[key][1]:
                    if self.shows[key][0] in self.associations:
                        associated_id = self.associations[self.shows[key][0]]
                        for i in range(11):
                            recommendationResult += f"{self.books[associated_id][i]}\n"
                        return recommendationResult
                    else:
                        tkinter.messagebox.showwarning(title="Warning", message="There are no recommendations for that title.")
                        return "No Results"
        # If the type is Book, search through the books dictionary and determine the id associated
        # with that title
        if type == "Book":
            for key in self.books:
                if title in self.books[key][1]:
                    if self.books[key][0] in self.associations:
                        associated_id = self.associations[self.books[key][0]]
                        for i in range(14):
                            recommendationResult += f"{self.shows[associated_id][i]}\n"
                        return recommendationResult
                    else:
                        tkinter.messagebox.showwarning(title="Warning", message="There are no recommendations for that title.")
                        return "No Results"

    #Notebook function
    def noteBook(self):
        moive_showRating = []
        moive_showRating_times = {}
        tvShow_showRating = []
        tvShow_showRating_times = {}

        for value in self.shows:
            if self.shows[value][3] == "Movie":
                moive_showRating.append(value[-4])

            elif self.shows[value][3] == "TV Show":
                tvShow_showRating.append(value[-4])

        moive_showRating_times = Counter(moive_showRating)

        tvShow_showRating_times = Counter(tvShow_showRating)

        labels1 = list(moive_showRating_times.keys())
        sizes1 = list(moive_showRating_times.values())

        labels2 = list(tvShow_showRating_times.keys())
        sizes2 = list(tvShow_showRating_times.values())

        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.pie(sizes1, labels=labels1, autopct='%1.1f%%', startangle=140)
        plt.title('Movie Rating and their percentage')

        plt.subplot(1, 2, 2)
        plt.pie(sizes2, labels=labels2, autopct='%1.1f%%', startangle=140)
        plt.title('TV Show Rating and their percentage')
