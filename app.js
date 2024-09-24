const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const app = express();

// Middleware
app.use(bodyParser.json());
app.use(express.static('public'));

// MySQL connection
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    database: 'movie_ticketing'
});

db.connect(err => {
    if (err) throw err;
    console.log('MySQL connected...');
});

// Fetch movies
app.get('/api/movies', (req, res) => {
    let sql = 'SELECT * FROM movies';
    db.query(sql, (err, results) => {
        if (err) throw err;
        res.json(results);
    });
});

// Book a ticket
app.post('/api/book', (req, res) => {
    const { movieId, name, seats } = req.body;
    
    let sql = `INSERT INTO bookings (movie_id, name, seats) VALUES (${movieId}, '${name}', ${seats})`;
    db.query(sql, (err, result) => {
        if (err) {
            res.json({ success: false });
        } else {
            res.json({ success: true });
        }
    });
});

// Start server
app.listen(3000, () => {
    console.log('Server started on port 3000...');
});
