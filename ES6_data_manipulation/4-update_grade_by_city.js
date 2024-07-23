export default function updateStudentGradeByCity(listStudents, city, newGrades) {
  return listStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const actGrades = newGrades.find((grade) => grade.studentId === student.id);
      const grade = actGrades ? actGrades.grade : 'N/A';
      return { ...student, grade };
    });
}
