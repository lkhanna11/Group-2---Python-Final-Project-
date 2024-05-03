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

