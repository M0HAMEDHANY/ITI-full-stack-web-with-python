const nameInput = document.getElementById('name');
const ageInput = document.getElementById('age');
const coursesSelect = document.getElementById('courses');
const addBtn = document.getElementById('addBtn');
const deleteAllBtn = document.getElementById('deleteAllBtn');
const dataTable = document.getElementById('dataTable').getElementsByTagName('tbody')[0];

addBtn.addEventListener('click', () => {
    const name = nameInput.value.trim();
    const age = ageInput.value.trim();
    const courses = Array.from(coursesSelect.selectedOptions).map(option => option.value).join(',');

    const nameRegex = /^[a-zA-Z\s]+$/;
    const ageNumber = parseInt(age);

    if (name && age && courses && nameRegex.test(name) && ageNumber >= 18 && ageNumber <= 60) {
        const row = dataTable.insertRow();
        const deleteBtn = document.createElement('button');

        row.insertCell(0).textContent = name;
        row.insertCell(1).textContent = age;
        row.insertCell(2).textContent = courses;

        const deleteCell = row.insertCell(3);
        deleteBtn.textContent = '❌';
        deleteBtn.style.backgroundColor = 'transparent';
        deleteBtn.style.padding = '10px';
        deleteBtn.style.border = 'none';
        deleteBtn.style.cursor = 'pointer';
        deleteCell.appendChild(deleteBtn);


        deleteBtn.addEventListener('click', () => row.remove());

        nameInput.value = '';
        ageInput.value = '';
        coursesSelect.value = '';
    } else {
        showModal('Please enter valid data');
    }
});

deleteAllBtn.addEventListener('click', () => {
    while (dataTable.rows.length) {
        dataTable.deleteRow(0);
    }
});

function showModal(message) {
    var modal = document.getElementById('error-modal');
    var span = document.getElementsByClassName('close-button')[0];
    document.getElementById('error-message').innerText = message;
    modal.style.display = 'block';

    span.onclick = function () {
        modal.style.display = 'none';
    }

    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
}