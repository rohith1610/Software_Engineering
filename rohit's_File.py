

"edited by Sheetal
def SearchMovieData(Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="",
                    Rating=""):
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM book WHERE Movie_ID=? OR Movie_Name=? OR Release_Date=? OR Director=? OR Cast=? OR Budget=? OR Duration=? OR Rating=?",
        (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))
    rows = cur.fetchall()
    con.close()
    return rows


def UpdateMovieData(id, Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="",
                    Rating=""):
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute(
        "UPDATE book SET Movie_ID=?,Movie_Name=?,Release_Date=?,Director=?,Cast=?,Budget=?,Duration=?,Rating=?, WHERE id=?",
        (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))
    con.commit()
    con.close()

