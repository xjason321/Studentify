let users = [];

function register(event) {
  event.preventDefault();

  const newUsernameInput = document.getElementById('new-username');
  const newPasswordInput = document.getElementById('new-password');

  // Create a new user object
  const newUser = {
    username: newUsernameInput.value,
    password: newPasswordInput.value
  };

  // Add the new user to the array
  users.push(newUser);

  // Clear the input fields
  newUsernameInput.value = '';
  newPasswordInput.value = '';

  alert('Registration successful! Please log in with your new credentials.');
}

function login(event) {
  event.preventDefault();

  const usernameInput = document.getElementById('username');
  const passwordInput = document.getElementById('password');

  // Check if the provided username and password match any user in the array
  const user = users.find(u => u.username === usernameInput.value && u.password === passwordInput.value);

  if (user) {
    alert('Login successful!');
    window.location.href = 'main.html';
  } else {
    alert('Invalid username or password. Please try again.');
  }

  // Clear the input fields
  usernameInput.value = '';
  passwordInput.value = '';
}

function logout(event) {
  event.preventDefault();

  // Redirect back to the login page
  window.location.href = 'index.html';
}