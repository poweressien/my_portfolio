document.getElementById("contact-form").addEventListener("submit", function(event) {
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let subject = document.getElementById("subject").value;
    let message = document.getElementById("message").value;
    if (name && email && subject && message) {
        if (confirm(`Thanks, ${name}! Your message from ${email} about ${subject} has been sent! Send another?`)) {
            document.getElementById("contact-form").reset();
        }
    } else {
        alert("Please fill out all fields!");
        event.preventDefault();
    }
});

function showMessage() {
    alert("Yo, welcome to my site! Keep coding!");
}

function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
    // Save preference to localStorage
    if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("theme", "dark");
    } else {
        localStorage.setItem("theme", "light");
    }
}

// Apply saved theme on page load
if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-mode");
}