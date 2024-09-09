const uploadArea = document.getElementById('upload-area');
const fileInput = document.getElementById('file-input');
const fileNameDisplay = document.getElementById('file-name');
const uploadText = document.getElementById('upload-text');
const compressBtn = document.getElementById('compress-btn');
const successMessage = document.getElementById('success-message');

uploadArea.addEventListener('click', () => {
    fileInput.click();
});

uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('dragging');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('dragging');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('dragging');
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        fileInput.files = files;
        displayFileName(files[0].name);
    }
});

fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        displayFileName(fileInput.files[0].name);
    }
});

function displayFileName(name) {
    fileNameDisplay.textContent = name;
    uploadText.style.display = 'none';
    uploadArea.style.border = '2px solid var(--primary-color)';
}

compressBtn.addEventListener('click', (e) => {
    if (fileInput.files.length === 0) {
        e.preventDefault();
        alert('Please select an image first.');
    } else {
        showSuccessMessage();
    }
});

function showSuccessMessage() {
    successMessage.style.display = 'block';
    setTimeout(() => {
        successMessage.style.display = 'none';
    }, 5000);
}