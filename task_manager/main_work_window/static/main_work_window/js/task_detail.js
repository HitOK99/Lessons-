let modal = document.getElementById("confirmModal");
let taskNameSpan = document.getElementById("taskName");
let confirmDeleteButton = document.getElementById("confirmDelete");
let formToSubmit;

function confirmDeletion(taskName, button) {
    taskNameSpan.textContent = taskName;
    formToSubmit = button.closest("form");
    modal.style.display = "flex";
}

document.getElementById("cancelDelete").onclick = function() {
    modal.style.display = "none";
};

confirmDeleteButton.onclick = function() {
    modal.style.display = "none";
    formToSubmit.submit();
};
function openModal(taskTitle, taskDescription) {
    document.getElementById('modalTitle').textContent = taskTitle;
    document.getElementById('modalDescription').textContent = taskDescription;
    document.getElementById('taskModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('taskModal').style.display = 'none';
}

document.querySelectorAll('.task-title, .subtask-title').forEach(element => {
    element.addEventListener('click', function() {
        const taskTitle = this.textContent;
        const taskDescription = this.dataset.description;
        openModal(taskTitle, taskDescription);
    });
});

