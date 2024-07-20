export class HolbertonCourse {
  constructor(name, lenght, students) {
    this._name = name;
    this._lenght = lenght;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName !== 'string') {
      throw new TypeError('Name should be a string');
    }
    this._name = newName;
  }

  get lenght() {
    return this.lenght;
  }

  set lenght(newLengght) {
    if (typeof newLengght !== 'number') {
      throw new TypeError('Lenght should be a number');
    }
    this._lenght = newLengght;
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (Array.isArray(newStudents)) {
      throw new TypeError('Students should be an array');
    }
    this._students = newStudents;
  }
}
