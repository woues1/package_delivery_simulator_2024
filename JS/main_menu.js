
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    // Get the values from the form
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Create an object with the login data
    const loginData = {
        username: username,
        password: password
    };

    // Send a POST request to the Flask endpoint
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(loginData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Handle the response from the server
        console.log(data);
        // Redirect or perform any other action based on the response
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
});


document.getElementById('log_in_button').addEventListener('click', function() {
    // Get the values from the form
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Create a hidden form element
    const hiddenForm = document.createElement('form');
    hiddenForm.method = 'post';
    hiddenForm.action = '/login';

    // Create hidden input fields for username and password
    const usernameInput = document.createElement('input');
    usernameInput.type = 'hidden';
    usernameInput.name = 'username';
    usernameInput.value = username;
    hiddenForm.appendChild(usernameInput);

    const passwordInput = document.createElement('input');
    passwordInput.type = 'hidden';
    passwordInput.name = 'password';
    passwordInput.value = password;
    hiddenForm.appendChild(passwordInput);

    // Append the form to the document body and submit it
    document.body.appendChild(hiddenForm);
    hiddenForm.submit();
});
