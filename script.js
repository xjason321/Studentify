var signupForm = document.querySelector('form');

signupForm.addEventListener('submit', function(event) {
  event.preventDefault();

  var newUsername = document.getElementById('new-username').value;
  var newPassword = document.getElementById('new-password').value;

  var data = {
    username: newUsername,
    password: newPassword
  };

  fetch('/signup', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
    .then(response => response.text())
    .then(result => {
      console.log(result);
      signupForm.reset();
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
