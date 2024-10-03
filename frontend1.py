from tkinter import *
import tkinter.messagebox
import MiniProject_Backend
 
#David
 
class Movie:
    def __init__(self, root):
        self.root=root
        self.root.title("Online Movie Ticket Booking System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="black")
 
        Movie_Name=StringVar()
        Movie_ID=StringVar()
        Release_Date=StringVar()
        Director=StringVar()
        Cast=StringVar()
        Budget=StringVar()
        Duration=StringVar()
        Rating=StringVar()
 
        #Fuctions
        def iExit():
            iExit=tkinter.messagebox.askyesno("Online Movie Ticket Booking System", "Are you sure???")
            if iExit>0:
                root.destroy()
            return
 
        def clcdata():
            self.txtMovie_ID.delete(0,END)
            self.txtMovie_Name.delete(0,END)
            self.txtRelease_Date.delete(0,END)
            self.txtDirector.delete(0,END)
            self.txtCast.delete(0,END)
            self.txtBudget.delete(0,END)
            self.txtRating.delete(0,END)
            self.txtDuration.delete(0,END)
 
        def adddata():
            if(len(Movie_ID.get())!=0):
                MiniProject_Backend.AddMovieRec(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Director.get(),Cast.get(),Budget.get(),Duration.get(),Rating.get())
                MovieList.delete(0,END)
                MovieList.insert(END,(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Director.get(),Cast.get(),Budget.get(),Duration.get(),Rating.get()))
 
        def disdata():
            MovieList.delete(0,END)
            for row in MiniProject_Backend.ViewMovieData():
                MovieList.insert(END, row, str(""))
 
        def movierec(event):
            global sd
            searchmovie=MovieList.curselection()[0]
            sd=MovieList.get(searchmovie)
 
            self.txtMovie_ID.delete(0,END)
            self.txtMovie_ID.insert(END,sd[1])
            self.txtMovie_Name.delete(0,END)
            self.txtMovie_Name.insert(END,sd[2])
            self.txtRelease_Date.delete(0,END)
            self.txtRelease_Date.insert(END,sd[3])
            self.txtDirector.delete(0,END)
            self.txtDirector.insert(END,sd[4])
            self.txtCast.delete(0,END)
            self.txtCast.insert(END,sd[5])
            self.txtBudget.delete(0,END)
            self.txtBudget.insert(END,sd[6])
            self.txtDuration.delete(0,END)
            self.txtDuration.insert(END,sd[7])
            self.txtRating.delete(0,END)
            self.txtRating.insert(END,sd[8])
 
        def deldata():
            if(len(Movie_ID.get())!=0):
                MiniProject_Backend.DeleteMovieRec(sd[0])
                clcdata()
                disdata()
 
        def searchdb():
            MovieList.delete(0,END)
            for row in MiniProject_Backend.SearchMovieData(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Director.get(),Cast.get(),Budget.get(),Duration.get(),Rating.get()):
                MovieList.insert(END, row, str(""))