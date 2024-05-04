# Importing the required libraries
import tkinter
import tkinter.messagebox as messagebox

# Class Definition
class RecommenderGUI:

    # Constructor function
    def __init__(self):
        ####
        recommender_object = rec.Recommender()
        ####
        self.__main_window = tkinter.Tk()
        self.__main_window.title("Media Recommender")
        self.__main_window.geometry("1200x800")

        # Specifying notebook and its tabs
        self.__media_nb = ttk.Notebook(self.__main_window)
        self.__media_nb.pack(expand = 1, fill = tkinter.BOTH)

        ## Movies Tab
        self.__movies_tab = tkinter.Frame(self.__media_nb)
        self.__media_nb.add(self.__movies_tab, text="Movies")

        # Creating an inner frame for scrollable movies list
        self.__movies_inner_frame = tkinter.Frame(self.__movies_tab)
        self.__movies_inner_frame.pack()

        #### Using if-else block to display the default message instead of text boxes.

        # Loading movie lists and run time in the frame in non-editable manner
        ####
        self.__movies_data = recommender_object.getMovieList()
        ####
        self.__movies_text_area = tkinter.Text(self.__movies_inner_frame, wrap = tkinter.WORD)
        self.__movies_text_area.insert(1.0, f"{self.__movies_data}")
        self.__movies_text_area.configure(state= tkinter.DISABLED)
        self.__movies_text_area.pack(side = "left")

        # Including a vertical scroll bar
        self.__movies_scrollbar = tkinter.Scrollbar(self.__movies_inner_frame, orient= tkinter.VERTICAL)
        self.__movies_scrollbar.pack(side = "right")
        self.__movies_scrollbar.configure(command=self.__movies_text_area.yview)

        # Loading movie stats in the frame in non-editable manner
        ####
        self.__movies_stats_data = recommender_object.getMovieStats()
        ####
        self.__movies_stats_text = tkinter.Text(self.__movies_tab, wrap= tkinter.WORD)
        self.__movies_stats_text.insert(1.0, f"{self.__movies_stats_data}")
        self.__movies_stats_text.configure(state= tkinter.DISABLED)
        self.__movies_stats_text.pack(side = tkinter.BOTTOM)

        ## TV Shows Tab
        self.__TV_tab = tkinter.Frame(self.__media_nb)
        self.__media_nb.add(self.__TV_tab, text="TV Shows")

        # Creating an inner frame for scrollable TV list
        self.__TV_inner_frame = tkinter.Frame(self.__TV_tab)
        self.__TV_inner_frame.pack()

        #### Using if-else block to display the default message instead of text boxes.

        # Loading TV Shows lists and seasons in the frame in non-editable manner
        ####
        self.__TV_data = recommender_object.getTVList()
        ####
        self.__TV_text_area = tkinter.Text(self.__TV_inner_frame, wrap=tkinter.WORD)
        self.__TV_text_area.insert(1.0, f"{self.__TV_data}")
        self.__TV_text_area.configure(state=tkinter.DISABLED)
        self.__TV_text_area.pack(side="left")

        # Including a vertical scroll bar
        self.__TV_scrollbar = tkinter.Scrollbar(self.__TV_inner_frame, orient=tkinter.VERTICAL)
        self.__TV_scrollbar.pack(side="right")
        self.__TV_scrollbar.configure(command=self.__TV_text_area.yview)

        # Loading TV Shows stats in the frame in non-editable manner
        ####
        self.__TV_stats_data = recommender_object.getTVStats()
        ####
        self.__TV_stats_text = tkinter.Text(self.__TV_tab, wrap=tkinter.WORD)
        self.__TV_stats_text.insert(1.0, f"{self.__TV_stats_data}")
        self.__TV_stats_text.configure(state=tkinter.DISABLED)
        self.__TV_stats_text.pack(side=tkinter.BOTTOM)

        ## Book Tab
        self.__Book_tab = tkinter.Frame(self.__media_nb)
        self.__media_nb.add(self.__Book_tab, text="Books")

        # Creating an inner frame for scrollable Book list
        self.__Book_inner_frame = tkinter.Frame(self.__Book_tab)
        self.__Book_inner_frame.pack()

        #### Using if-else block to display the default message instead of text boxes.

        # Loading Book lists and authors in the frame in non-editable manner
        ####
        self.__Book_data = recommender_object.getBookList()
        ####
        self.__Book_text_area = tkinter.Text(self.__Book_inner_frame, wrap=tkinter.WORD)
        self.__Book_text_area.insert(1.0, f"{self.__Book_data}")
        self.__Book_text_area.configure(state=tkinter.DISABLED)
        self.__Book_text_area.pack(side="left")

        # Including a vertical scroll bar
        self.__Book_scrollbar = tkinter.Scrollbar(self.__Book_inner_frame, orient=tkinter.VERTICAL)
        self.__Book_scrollbar.pack(side="right")
        self.__Book_scrollbar.configure(command=self.__Book_text_area.yview)

        # Loading Book stats in the frame in non-editable manner
        ####
        self.__Book_stats_data = recommender_object.getBookStats()
        ####
        self.__Book_stats_text = tkinter.Text(self.__Book_tab, wrap=tkinter.WORD)
        self.__Book_stats_text.insert(1.0, f"{self.__Book_stats_data}")
        self.__Book_stats_text.configure(state=tkinter.DISABLED)
        self.__Book_stats_text.pack(side=tkinter.BOTTOM)

                ## Search Movies / TV Tab
        self._Movies_TV_tab = tkinter.Frame(self._media_nb)
        self._media_nb.add(self._Movies_TV_tab, text="Search Movies / TV")

        # Adding a combobox widget for choice of options
        self._CB_Frame = tkinter.Frame(self._Movies_TV_tab)
        self._CB_Label = tkinter.Label(self._CB_Frame, text="Type of Media: ")
        self._CB_Label.pack(padx = 10, pady = 10, side = tkinter.LEFT)
        self._Movies_TV_options = ["Movies", "TV Shows"]
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

        # Adding a search button
        self._Movies_TV_Search_button_frame = tkinter.Frame(self._Movies_TV_tab)
        ####
        self._Movies_TV_Search_button = tkinter.Button(self._Movies_TV_Search_button_frame,
                                                        text= "Search Movies / TV Shows", command= rec.searchTVMovies)
        ####
        self._Movies_TV_Search_button.pack(padx = 10, pady = 10, side = tkinter.LEFT)
        self._Movies_TV_Search_button_frame.pack()

        # Adding a text frame for displaying search result
        self._Movies_TV_text_Frame = tkinter.Frame(self._Movies_TV_tab)
        self._Movies_TV_text_area = tkinter.Text(self._Movies_TV_text_Frame, wrap= tkinter.WORD)
        ####
        #### Add the entry.get functions in Recommender.py to link these together
        ####
        #### if no searches have been performed yet, display default messsage ####
        #### User should not be able to edit data
        self._Movies_TV_text_area.pack(padx = 10, pady = 10, side = tkinter.LEFT)

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

        # Adding a search button
        self._Books_Search_button_frame = tkinter.Frame(self._Search_books_tab)
        ####
        self._Books_Search_button = tkinter.Button(self._Books_Search_button_frame,
                                                       text="Search Books", command=rec.searchBooks)
        ####
        self._Books_Search_button.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._Books_Search_button_frame.pack()

        # Adding a text frame for displaying search result
        self._Search_Books_text_Frame = tkinter.Frame(self._Search_books_tab)
        self._Search_Books_text_area = tkinter.Text(self._Search_Books_text_Frame, wrap=tkinter.WORD)
        ####
        #### Add the entry.get functions in Recommender.py to link these together
        ####
        #### if no searches have been performed yet, display default messsage ####
        #### User should not be able to edit data
        self._Search_Books_text_area.pack(padx=10, pady=10, side=tkinter.LEFT)

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
        ####
        self._Recs_button = tkinter.Button(self._Recs_button_frame,
                                                   text="Get Recommendations", command=rec.getRecommendations)
        ####
        self._Recs_button.pack(padx=10, pady=10, side=tkinter.LEFT)
        self._Recs_button_frame.pack()

        # Adding a text frame for displaying search result
        self._Recs_text_Frame = tkinter.Frame(self._Recommendations_tab)
        self._Recs_text_area = tkinter.Text(self._Recs_text_Frame, wrap=tkinter.WORD)
        ####
        #### Add the entry.get functions in Recommender.py to link these together
        ####
        #### if no searches have been performed yet, display default messsage ####
        #### User should not be able to edit data
        self._Recs_text_area.pack(padx=10, pady=10, side=tkinter.LEFT)

        # Adding a vertical scroll bar for text area
        self._Recommendations_scrollbar = tkinter.Scrollbar(self._Recs_text_Frame, orient=tkinter.VERTICAL)
        self._Recommendations_scrollbar.pack(side="right")
        self._Recommendations_scrollbar.configure(command=self._Recs_text_area.yview)

        

