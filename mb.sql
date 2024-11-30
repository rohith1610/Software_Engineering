CREATE DATABASE movie_ticketing;

USE movie_ticketing;

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    duration INT NOT NULL
);

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    name VARCHAR(255),
    seats INT,
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);

-- Insert some sample movies
INSERT INTO movies (title, duration) VALUES ('The Matrix', 120), ('Inception', 148), ('Interstellar', 169);
