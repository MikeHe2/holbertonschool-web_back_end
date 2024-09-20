const fs = require('fs');

async function countStudents(path) {
  try {
    const listCS = [];
    const listSWE = [];

    const file = await fs.promises.readFile(path, 'utf8');
    const rows = file.trim().split('\n');

    // Verifica si el archivo tiene datos después de la primera línea
    if (rows.length <= 1) {
      return 'No students found';
    }

    for (let i = 1; i < rows.length; i += 1) {
      const row = rows[i].split(',');

      if (row[3] === 'CS') listCS.push(row[0]);
      else if (row[3] === 'SWE') listSWE.push(row[0]);
    }

    const studentSummary = [
      `Number of students: ${rows.length - 1}`,
      `Number of students in CS: ${listCS.length}. List: ${listCS.join(', ')}`,
      `Number of students in SWE: ${listSWE.length}. List: ${listSWE.join(', ')}`,
    ].join('\n');

    return studentSummary;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
