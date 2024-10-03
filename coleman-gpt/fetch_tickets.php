<?php
$servername = "localhost";
$username = "username"; // Update with your database username
$password = "password"; // Update with your database password
$dbname = "movie_tickets"; // Update with your database name

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT movie, showtime, seats FROM tickets";
$result = $conn->query($sql);

$tickets = array();
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $tickets[] = $row;
    }
}

echo json_encode($tickets);

$conn->close();
?>
