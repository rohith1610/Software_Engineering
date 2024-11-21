import sqlite3
import random


class MovieBookingSystem:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Create tables if they do not exist."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT,
                                genre TEXT,
                                seats_available INTEGER)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                                booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_name TEXT,
                                movie_id INTEGER,
                                seats_booked INTEGER,
                                FOREIGN KEY (movie_id) REFERENCES movies (id))''')
        self.conn.commit()

    def add_movie(self, title, genre, seats_available):
        """Add a movie to the database."""
        self.cursor.execute("INSERT INTO movies (title, genre, seats_available) VALUES (?, ?, ?)",
                            (title, genre, seats_available))
        self.conn.commit()

    def view_movies(self):
        """Display all movies."""
        self.cursor.execute("SELECT * FROM movies")
        movies = self.cursor.fetchall()
        if not movies:
            print("No movies available.")
        else:
            print("Available Movies:")
            for movie in movies:
                print(f"{movie[0]}. {movie[1]} - Genre: {movie[2]}, Seats Available: {movie[3]}")

    def book_ticket(self, user_name, movie_id, seats):
        """Book a ticket for the movie."""
        self.cursor.execute("SELECT seats_available FROM movies WHERE id = ?", (movie_id,))
        movie = self.cursor.fetchone()
        if movie and movie[0] >= seats:
            self.cursor.execute("UPDATE movies SET seats_available = seats_available - ? WHERE id = ?",
                                (seats, movie_id))
            self.cursor.execute("INSERT INTO bookings (user_name, movie_id, seats_booked) VALUES (?, ?, ?)",
                                (user_name, movie_id, seats))
            self.conn.commit()
            print(f"Ticket booked successfully for {user_name} for {seats} seat(s)!")
        else:
            print("Not enough seats available.")

    def recommend_movie(self):
        """Recommend a random movie."""
        self.cursor.execute("SELECT * FROM movies")
        movies = self.cursor.fetchall()
        if not movies:
            print("No movies available to recommend.")
        else:
            recommended_movie = random.choice(movies)
            print(f"Recommended Movie: {recommended_movie[1]} - Genre: {recommended_movie[2]}")

    def close(self):
        """Close the database connection."""
        self.conn.close()


if __name__ == "__main__":
    system = MovieBookingSystem()

    while True:
        print("\n--- Movie Booking System ---")
        print("1. View Movies")
        print("2. Add Movie")
        print("3. Book Ticket")
        print("4. Recommend Movie")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            system.view_movies()

        elif choice == '2':
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            seats = int(input("Enter number of seats available: "))
            system.add_movie(title, genre, seats)

        elif choice == '3':
            system.view_movies()
            movie_id = int(input("Enter movie ID to book tickets: "))
            user_name = input("Enter your name: ")
            seats = int(input("Enter number of seats to book: "))
            system.book_ticket(user_name, movie_id, seats)

        elif choice == '4':
            system.recommend_movie()

        elif choice == '5':
            system.close()
            print("Thank you for using the Movie Booking System!")
            break

        else:
            print("Invalid choice! Please try again.")
