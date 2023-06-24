// JavaScript code to dynamically clone subject fields
const subjectsContainer = document.querySelector('.Subjects');
const subjectTemplate = subjectsContainer.querySelector('li');

let subjectCounter = 1;

subjectTemplate.querySelector('input[name="learning_subjects"]').addEventListener('input', () => {
    const newSubject = subjectTemplate.cloneNode(true);
    newSubject.querySelector('input[name="learning_subjects"]').name = `learning_subjects_${++subjectCounter}`;
    newSubject.querySelector('input[name="proficiency"]').name = `proficiency_${subjectCounter}`;
    subjectsContainer.appendChild(newSubject);
});