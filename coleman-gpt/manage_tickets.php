<?php
$servername = "localhost";
$username = "username"; // Update with your database username
$password = "password"; // Update with your database password
$dbname = "movie_tickets"; // Update with your database name

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $movie = $conn->real_escape_string($_POST['movie']);
    $showtime = $conn->real_escape_string($_POST['showtime']);
    $seats = (int)$_POST['seats'];

    $sql = "INSERT INTO tickets (movie, showtime, seats) VALUES ('$movie', '$showtime', $seats)";
    
    if ($conn->query($sql) === TRUE) {
        echo "New ticket booked successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

$conn->close();
?>
