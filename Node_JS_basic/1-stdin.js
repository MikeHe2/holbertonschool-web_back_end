process.stdout.write('Welcome to Holberton School, what is your name?\r\n');

process.stdin.on('readable', () => {
  const input = process.stdin.read();
  if (input !== null) {
    const name = input.toString().trim();
    console.log(`Your name is: ${name}\r`);
    process.stdin.end();
  }
});

process.stdin.on('end', () => {
  console.log('This important software is now closing\r');
});
