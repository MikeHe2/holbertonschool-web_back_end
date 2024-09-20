const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.set('Content-Type', 'text/plain');
  let dbInfo = 'This is the list of our students\n';

  try {
    const studentsInfo = await countStudents(process.argv[2]);
    dbInfo += studentsInfo;
    res.send(dbInfo);
  } catch (err) {
    dbInfo += 'Cannot load the database';
    res.send(dbInfo);
  }
});

app.listen(port);

module.exports = app;
