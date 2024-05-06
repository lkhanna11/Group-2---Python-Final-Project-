# Authors : Alexander Beke , Latika Khanna, Zijie Ma
# Date : May 5, 2024
# Description : This program contains the GUI functionality for the Media Library


# Importing the required libraries
import tkinter
from tkinter import ttk
import Recommender as rec
import tkinter.messagebox as messagebox

# Class Definition
class RecommenderGUI:

    # Constructor function
    def __init__(self):
        self.recommender_object = rec.Recommender()
        self._main_window = tkinter.Tk()
        self._main_window.title("Media Recommender")
        self._main_window.geometry("1200x800")

        # Specifying notebook and its tabs
        self._media_nb = ttk.Notebook(self._main_window)
        self._media_nb.pack(expand = 1, fill = tkinter.BOTH)

        ## Movies Tab
        self._movies_tab = tkinter.Frame(self._media_nb)
        self._media_nb.add(self._movies_tab, text="Movies")

        # Creating an inner frame for scrollable movies list
        self._movies_inner_frame = tkinter.Frame(self._movies_tab)
        self._movies_inner_frame.pack()

        # Loading movie lists and run time in the frame in non-editable manner
        self._movies_text_area = tkinter.Text(self._movies_inner_frame, wrap=tkinter.WORD)
        self._movies_stats_text = tkinter.Text(self._movies_tab, wrap=tkinter.WORD)
        self._movies_data = self.recommender_object.getMovieList()

        # Using if-else block to display the default message instead of text boxes.
        if not self._movies_data:
            self._movies_text_area.insert(1.0, "No movies have been loaded yet, use 'Load Shows' button to do that")
        else:
            self._movies_text_area.insert(1.0, f"{self._movies_data}")
            self._movies_text_area.configure(state= tkinter.DISABLED)

            # Including a vertical scroll bar
            self._movies_scrollbar = tkinter.Scrollbar(self._movies_inner_frame, orient=tkinter.VERTICAL)
            self._movies_scrollbar.pack(side="right")
            self._movies_scrollbar.configure(command=self._movies_text_area.yview)

            # Loading movie stats in the frame in non-editable manner
            self._movies_stats_data = self.recommender_object.getMovieStats()
            self._movies_stats_text.insert(1.0, f"{self._movies_stats_data}")
            self._movies_stats_text.configure(state=tkinter.DISABLED)

        self._movies_text_area.pack(side = "left")
        self._movies_stats_text.pack(side = tkinter.BOTTOM)

        ## TV Shows Tab
        self._TV_tab = tkinter.Frame(self._media_nb)
        self._media_nb.add(self._TV_tab, text="TV Shows")

        # Creating an inner frame for scrollable TV list
        self._TV_inner_frame = tkinter.Frame(self._TV_tab)
        self._TV_inner_frame.pack()

        # Loading TV Shows lists and seasons in the frame in non-editable manner
        self._TV_text_area = tkinter.Text(self._TV_inner_frame, wrap=tkinter.WORD)
        self._TV_stats_text = tkinter.Text(self._TV_tab, wrap=tkinter.WORD)
        self._TV_data = self.recommender_object.getTVList()

        # Using if-else block to display the default message instead of text boxes.
        if not self._TV_data:
            self._TV_text_area.insert(1.0, "No shows have been loaded yet, use 'Load Shows' button to do that")
        else:
            self._TV_text_area.insert(1.0, f"{self._TV_data}")
            self._TV_text_area.configure(state=tkinter.DISABLED)

            # Including a vertical scroll bar
            self._TV_scrollbar = tkinter.Scrollbar(self._TV_inner_frame, orient=tkinter.VERTICAL)
            self._TV_scrollbar.pack(side="right")
            self._TV_scrollbar.configure(command=self._TV_text_area.yview)

            # Loading TV Shows stats in the frame in non-editable manner
            self._TV_stats_data = self.recommender_object.getTVStats()
            self._TV_stats_text.insert(1.0, f"{self._TV_stats_data}")
            self._TV_stats_text.configure(state=tkinter.DISABLED)

        self._TV_text_area.pack(side="left")
        self._TV_stats_text.pack(side=tkinter.BOTTOM)

        ## Book Tab
        self._Book_tab = tkinter.Frame(self._media_nb)
        self._media_nb.add(self._Book_tab, text="Books")

        # Creating an inner frame for scrollable Book list
        self._Book_inner_frame = tkinter.Frame(self._Book_tab)
        self._Book_inner_frame.pack()

        # Loading Book lists and authors in the frame in non-editable manner
        self._Book_text_area = tkinter.Text(self._Book_inner_frame, wrap=tkinter.WORD)
        self._Book_stats_text = tkinter.Text(self._Book_tab, wrap=tkinter.WORD)
        self._Book_data = self.recommender_object.getBookList()

        # Using if-else block to display the default message instead of text boxes
        if not self._Book_data:
            self._Book_text_area.insert(1.0, "No books have been loaded yet, use 'Load Books' button to do that")
        else:
            self._Book_text_area.delete(1.0, tkinter.END)
            self._Book_text_area.insert(1.0, f"{self._Book_data}")
            self._Book_text_area.configure(state=tkinter.DISABLED)

            # Including a vertical scroll bar
            self._Book_scrollbar = tkinter.Scrollbar(self._Book_inner_frame, orient=tkinter.VERTICAL)
            self._Book_scrollbar.pack(side="right")
            self._Book_scrollbar.configure(command=self._Book_text_area.yview)

            # Loading Book stats in the frame in non-editable manner
            self._Book_stats_data = self.recommender_object.getBookStats()
            self._Book_stats_text.insert(1.0, f"{self._Book_stats_data}")
            self._Book_stats_text.configure(state=tkinter.DISABLED)

        self._Book_text_area.pack(side="left")
        self._Book_stats_text.pack(side=tkinter.BOTTOM)

        ## Search Movies / TV Tab
        self._Movies_TV_tab = tkinter.Frame(self._media_nb)
        self._media_nb.add(self._Movies_TV_tab, text="Search Movies / TV")

        # Adding a combobox widget for choice of options
        self._CB_Frame = tkinter.Frame(self._Movies_TV_tab)
        self._CB_Label = tkinter.Label(self._CB_Frame, text="Type of Media: ")
        self._CB_Label.pack(padx = 10, pady = 10, side = tkinter.LEFT)
        self._Movies_TV_options = ["Movie", "TV Show"]
        self._Movies_TV_CB = ttk.Combobox(self._CB_Frame, values = self._Movies_TV_options)
        self._Movies_TV_CB.pack(padx = 10, pady = 10, side = tkinter.LEFT)
        self._CB_Frame.pack()

        # Adding label and entry widgets for user inputs
        self._Movies_TV_title_frame = tkinter.Frame(self._Movies_TV_tab)
        self._Movies_TV_Title_label = tkinter.Label(self._Movies_TV_title_frame, text = "Title: ")
        self._Movies_TV_Title_Entry = tkinter.Entry(self._Movies_TV_title_frame, width = 50)
        self._Movies_TV_Title_label.pack(padx = 10, pady = 10, side = tkinter.LEFT)
        self._Movies_TV_Title_Entry.pack(padx = 10, pady = 10, side = tkinter.LEFT)
        self._Movies_TV_title_frame.pack()

        self._Director_frame = tkinter.Frame(self._Movies_TV_tab)
        self._Director_label = tkinter.Label(self._Director_frame, text="Director: ")
        self._Director_Entry = tkinter.Entry(self._Director_frame, width=50)
        self._Director_label.pack(padx = 10, pady = 10, side = tkinter.LEFT)
        self._Director_Entry.pack(padx = 10, pady = 10, side = tkinter.LEFT)
        self._Director_frame.pack()

        self._Actor_frame = tkinter.Frame(self._Movies_TV_tab)
        self._Actor_label = tkinter.Label(self._Actor_frame, text="Actor: ")
        self._Actor_Entry = tkinter.Entry(self._Actor_frame, width=50)
        self._Actor_label.pack(padx = 10, pady = 10, side = tkinter.LEFT)
        self._Actor_Entry.pack(padx = 10, pady = 10, side = tkinter.LEFT)
        self._Actor_frame.pack()

        self._Genre_frame = tkinter.Frame(self._Movies_TV_tab)
        self._Genre_label = tkinter.Label(self._Genre_frame, text = "Genre: ")
        self._Genre_entry = tkinter.Entry(self._Genre_frame, width=50)
        self._Genre_label.pack(padx = 10, pady = 10, side = tkinter.LEFT)
        self._Genre_entry.pack(padx = 10, pady = 10, side = tkinter.LEFT)
        self._Genre_frame.pack()

        # Adding a text frame for displaying search result
        self._Movies_TV_text_Frame = tkinter.Frame(self._Movies_TV_tab)
        self._Movies_TV_text_Frame.configure(width=1000)
        self._Movies_TV_text_area = tkinter.Text(self._Movies_TV_text_Frame, wrap= tkinter.WORD)
        self._Movies_TV_text_area.insert(1.0, "No Searches have been performed yet")
        self._Movies_TV_text_area.configure(width=1000)
        self._Movies_TV_text_area.pack(padx = 10, pady = 10, side = tkinter.LEFT)
        self._Movies_TV_text_Frame.pack()

        # Adding a search button
        self._Movies_TV_Search_button_frame = tkinter.Frame(self._Movies_TV_tab)
        self._Movies_TV_Search_button = tkinter.Button(self._Movies_TV_Search_button_frame,
                                                        text= "Search Movies / TV Shows", command= self.searchShows)
        self._Movies_TV_Search_button.pack(padx = 10, pady = 10, side = tkinter.LEFT)
        self._Movies_TV_Search_button_frame.pack()

        # Adding a vertical scroll bar for text area
        self._Movies_TV_scrollbar = tkinter.Scrollbar(self._Movies_TV_text_Frame, orient=tkinter.VERTICAL)
        self._Movies_TV_scrollbar.pack(side="right")
        self._Movies_TV_scrollbar.configure(command=self._Movies_TV_text_area.yview)

        ## Search Books Tab
        self._Search_books_tab = tkinter.Frame(self._media_nb)
        self._media_nb.add(self._Search_books_tab, text="Search Books")

        # Adding label and entry widgets for user inputs
        self._Books_title_frame = tkinter.Frame(self._Search_books_tab)
        self._Books_Title_label = tkinter.Label(self._Books_title_frame, text="Title: ")
        self._Books_Title_Entry = tkinter.Entry(self._Books_title_frame, width=50)
        self._Books_Title_label.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._Books_Title_Entry.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._Books_title_frame.pack()

        self._Author_frame = tkinter.Frame(self._Search_books_tab)
        self._Author_label = tkinter.Label(self._Author_frame, text="Author: ")
        self._Author_Entry = tkinter.Entry(self._Author_frame, width=50)
        self._Author_label.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._Author_Entry.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._Author_frame.pack()

        self._Publisher_frame = tkinter.Frame(self._Search_books_tab)
        self._Publisher_label = tkinter.Label(self._Publisher_frame, text="Publisher: ")
        self._Publisher_Entry = tkinter.Entry(self._Publisher_frame, width=50)
        self._Publisher_label.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._Publisher_Entry.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._Publisher_frame.pack()

        # Adding a text frame for displaying search result
        self._Search_Books_text_Frame = tkinter.Frame(self._Search_books_tab)
        self._Search_Books_text_Frame.configure(width=1000)
        self._Search_Books_text_area = tkinter.Text(self._Search_Books_text_Frame, wrap=tkinter.WORD)
        self._Search_Books_text_area.insert(1.0, "No Searches have been performed yet / No data has been loaded yet")
        self._Search_Books_text_area.configure(width=1000)
        self._Search_Books_text_area.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._Search_Books_text_Frame.pack()

        # Adding a search button
        self._Books_Search_button_frame = tkinter.Frame(self._Search_books_tab)
        self._Books_Search_button = tkinter.Button(self._Books_Search_button_frame,
                                                       text="Search Books", command=self.searchBooks)
        self._Books_Search_button.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._Books_Search_button_frame.pack()

        # Adding a vertical scroll bar for text area
        self._Search_Books_scrollbar = tkinter.Scrollbar(self._Search_Books_text_Frame, orient=tkinter.VERTICAL)
        self._Search_Books_scrollbar.pack(side="right")
        self._Search_Books_scrollbar.configure(command=self._Search_Books_text_area.yview)

        ## Recommendations Tab
        self._Recommendations_tab = tkinter.Frame(self._media_nb)
        self._media_nb.add(self._Recommendations_tab, text="Recommendations")

        # Adding a combobox widget for choice of options
        self._RCB_Frame = tkinter.Frame(self._Recommendations_tab)
        self._RCB_Label = tkinter.Label(self._RCB_Frame, text="Type of Media: ")
        self._RCB_Label.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._RCB_Options = ["Movie", "TV Show", "Book"]
        self._Recommendations_CB = ttk.Combobox(self._RCB_Frame, values=self._RCB_Options)
        self._Recommendations_CB.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._RCB_Frame.pack()

        # Adding label and entry widgets for user inputs
        self._Recs_title_frame = tkinter.Frame(self._Recommendations_tab)
        self._Recs_Title_label = tkinter.Label(self._Recs_title_frame, text="Title: ")
        self._Recs_Title_Entry = tkinter.Entry(self._Recs_title_frame, width=50)
        self._Recs_Title_label.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._Recs_Title_Entry.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._Recs_title_frame.pack()

        # Adding a Get Recommendations button
        self._Recs_button_frame = tkinter.Frame(self._Recommendations_tab)
        self._Recs_button = tkinter.Button(self._Recs_button_frame,
                                                   text="Get Recommendations", command=self.getRecommendations)
        self._Recs_button.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._Recs_button_frame.pack()

        # Adding a text frame for displaying search result
        self._Recs_text_Frame = tkinter.Frame(self._Recommendations_tab)
        self._Recs_text_Frame.configure(width=1000)
        self._Recs_text_area = tkinter.Text(self._Recs_text_Frame, wrap=tkinter.WORD)
        self._Recs_text_area.insert(1.0, "No Searches have been performed yet / No data has been loaded yet")
        self._Recs_text_area.configure(width=1000)
        self._Recs_text_area.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._Recs_text_Frame.pack()

        # Adding a vertical scroll bar for text area
        self._Recommendations_scrollbar = tkinter.Scrollbar(self._Recs_text_Frame, orient=tkinter.VERTICAL)
        self._Recommendations_scrollbar.pack(side="right")
        self._Recommendations_scrollbar.configure(command=self._Recs_text_area.yview)

        ## Notebook Buttons
        self._NB_buttons_frame = tkinter.Frame(self._media_nb)
        self._NB_button_1 = tkinter.Button(self._NB_buttons_frame, text="Load Shows", command=self.loadShows)
        self._NB_button_2 = tkinter.Button(self._NB_buttons_frame, text="Load Books", command=self.loadBooks)
        self._NB_button_3 = tkinter.Button(self._NB_buttons_frame, text="Load Associations", command=self.loadAssociations)
        self._NB_button_4 = tkinter.Button(self._NB_buttons_frame, text="Information", command=self.creditInfoBox)
        self._NB_button_5 = tkinter.Button(self._NB_buttons_frame, text= "Quit", command=self._main_window.destroy)

        self._NB_button_1.pack(padx=35, side = tkinter.LEFT)
        self._NB_button_2.pack(padx=35, side=tkinter.LEFT)
        self._NB_button_3.pack(padx=35, side=tkinter.LEFT)
        self._NB_button_4.pack(padx=35, side=tkinter.LEFT)
        self._NB_button_5.pack(padx=35, side=tkinter.LEFT)
        self._NB_buttons_frame.pack(side=tkinter.BOTTOM)
        self._media_nb.pack()

    # Defining functions for the class
    def loadShows(self):
        self.recommender_object.loadShows()
        # Loading all the movies using functions of recommender_object and updating text area
        movie_list = self.recommender_object.getMovieList()
        self._movies_text_area.delete(1.0, tkinter.END)
        self._movies_text_area.insert(1.0, f"{movie_list}")
        self._movies_text_area.configure(state=tkinter.DISABLED)

        # Loading the Movie stats
        movie_Stats = self.recommender_object.getMovieStats()
        self._movies_stats_text.insert(1.0, f"{movie_Stats}")
        self._movies_stats_text.configure(state=tkinter.DISABLED)

        # Loading all the TV Shows using functions of recommender_object and updating text area
        TV_list = self.recommender_object.getTVList()
        self._TV_text_area.delete(1.0, tkinter.END)
        self._TV_text_area.insert(1.0, f"{TV_list}")
        self._TV_text_area.configure(state=tkinter.DISABLED)

        # Loading the TV Stats
        TV_Stats = self.recommender_object.getTVStats()
        self._TV_stats_text.insert(1.0, f"{TV_Stats}")
        self._TV_stats_text.configure(state = tkinter.DISABLED)

    def loadBooks(self):
        # Loading all the Books using functions of recommender_object and updating text area
        self.recommender_object.loadBooks()
        books_list = self.recommender_object.getBookList()
        self._Book_text_area.insert(1.0, f"{books_list}")
        self._Book_text_area.configure(state=tkinter.DISABLED)

        # Loading the Books Stats
        books_stats = self.recommender_object.getBookStats()
        self._Book_stats_text.insert(1.0, f"{books_stats}")
        self._Book_stats_text.configure(state=tkinter.DISABLED)

    def loadAssociations(self):
        # Loading all the associations using functions of recommender_object and updating the text area
        self.recommender_object.loadAssociations()

    def creditInfoBox(self):
        # Spawns a messagebox with names of the team members
        messagebox.showinfo(title="Group Project Details", message="Completed on May 5, 2024 by: \n "
                                                                   "Alexander Beke \n "
                                                                   "Latika Khanna \n "
                                                                   "Zijie Ma \n")

    def searchShows(self):
        # Extracting data from the combobox and entry widgets
        CB_choice = self._Movies_TV_CB.get()
        Title = self._Movies_TV_Title_Entry.get()
        Director = self._Director_Entry.get()
        Actor = self._Actor_Entry.get()
        Genre = self._Genre_entry.get()

        # Calling the function on recommender object and storing it
        search_result = self.recommender_object.searchTVMovies(CB_choice, Title, Director, Actor, Genre)

        # Updating the text area
        self._Movies_TV_text_area.configure(state=tkinter.NORMAL)
        self._Movies_TV_text_area.delete(1.0, tkinter.END)
        self._Movies_TV_text_area.insert(1.0, f"{search_result}")
        self._Movies_TV_text_area.configure(state= tkinter.DISABLED)

    def searchBooks(self):
        # Extracting data from the entry widgets
        Title = self._Books_Title_Entry.get()
        Author = self._Author_Entry.get()
        Publisher = self._Publisher_Entry.get()

        # Calling the function on recommender object and storing it
        search_result = self.recommender_object.searchBooks(Title, Author, Publisher)

        # Updating the text area
        self._Movies_TV_text_area.configure(state=tkinter.NORMAL)
        self._Search_Books_text_area.delete(1.0, tkinter.END)
        self._Search_Books_text_area.insert(1.0, f"{search_result}")
        self._Search_Books_text_area.configure(state=tkinter.DISABLED)

    def getRecommendations(self):
        # Extracting data from combobox and entry widgets
        CB_choice = self._Recommendations_CB.get()
        Title = self._Recs_Title_Entry.get()

        # Calling the function on recommender object and storing it
        get_rec_result = self.recommender_object.getRecommendations(CB_choice, Title)

        # Updating the text area
        self._Recs_text_area.configure(state=tkinter.NORMAL)
        self._Recs_text_area.delete(1.0, tkinter.END)
        self._Recs_text_area.insert(1.0, f"{get_rec_result}")
        self._Recs_text_area.configure(state=tkinter.DISABLED)


# Function definition
def main():
    # Instantiating an object of the RecommenderGUI class
    GUI_object = RecommenderGUI()
    tkinter.mainloop()

# Function call
main()
