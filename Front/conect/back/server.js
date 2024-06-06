const express = require('express');
const mysql = require('mysql');
const cors = require('cors');

const app = express();
app.use(cors());

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'aps',
    password: '7654321',
    database: 'aps_qualidade_agua'
});

connection.connect(err => {
    if (err) {
        console.error('Erro ao conectar ao banco de dados:', err);
        return;
    }
    console.log('Conectado ao banco de dados MySQL');
});

app.get('/sensores', (req, res) => {
    connection.query('SELECT * FROM sensores', (error, results) => {
        if (error) {
            return res.status(500).send('Erro ao buscar dados');
        }
        res.json(results);
    });
});

const PORT = 3306;
app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});
