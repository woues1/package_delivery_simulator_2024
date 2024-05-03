document.getElementById('login_submit').addEventListener('submit', function() {
    event.preventDefault();
    // Get the values from the form
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    // Create an object with username and password
    const loginData = {
        username: username,
        password: password
    };

    // Send a POST request with JSON data to the Flask endpoint
    fetch('http://127.0.0.1:3000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(loginData)
    })
    .then(response => {
        if (response.ok) {
            // If the response is successful, display a message
            alert('Login successful');
        } else {
            // If the response is not successful, handle the error
            return response.json().then(data => {
                alert(data.error);
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
    });
});