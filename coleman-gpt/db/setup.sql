CREATE DATABASE movie_tickets;

USE movie_tickets;

CREATE TABLE tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie VARCHAR(255) NOT NULL,
    showtime DATETIME NOT NULL,
    seats INT NOT NULL
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
