const http = require('http');
const countStudents = require('./3-read_file_async');

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    let dbInfo = 'This is the list of our students\n';
    await countStudents(process.argv[2])
      .then((msg) => {
        dbInfo += msg;
        res.end(dbInfo); // Sending response to the client
      })
      .catch((err) => {
        dbInfo += err.message;
        res.end(dbInfo); // Sending error response to the client
      });
  } else {
    res.statusCode = 404;
    res.end('404 Not Found');
  }
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
