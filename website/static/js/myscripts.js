document.querySelector('.fas.fa-user').addEventListener('click', function (e) {
    e.preventDefault();
    const dropdown = document.getElementById('profileDropdown');
    dropdown.classList.toggle('show');
});

// Close the dropdown if clicked outside
document.addEventListener('click', function (e) {
    const dropdown = document.getElementById('profileDropdown');
    if (!dropdown.contains(e.target)) {
        dropdown.classList.remove('show');
    }
});
