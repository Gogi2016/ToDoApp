// Show the page based on the current view
function navigateTo(page) {
    document.querySelectorAll('.page').forEach((pageElement) => {
      pageElement.style.display = 'none';
    });
  
    // Clear input fields when navigating to Register or Login page
    if (page === 'register') {
      document.getElementById('register-form').reset(); // Clear the register form
    } else if (page === 'login') {
      document.getElementById('login-form').reset(); // Clear the login form
    }
  
    // Hide the welcome page when navigating to Task Management
    if (page === 'task') {
      document.getElementById('welcome-page').style.display = 'none';
    }
  
    document.getElementById(`${page}-page`).style.display = 'block';
  }
  
  // Initial page load: show the welcome page
  document.addEventListener("DOMContentLoaded", function() {
    navigateTo('welcome');
  });
  
  // Register a new user (only allow registration if user doesn't already exist)
  document.getElementById('register-form')?.addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
  
    if (name && email && password) {
      const users = JSON.parse(localStorage.getItem('users')) || [];
      if (users.some(user => user.email === email)) {
        alert('User already exists!');
        return;
      }
  
      const newUser = { name, email, password };
      users.push(newUser);
      localStorage.setItem('users', JSON.stringify(users));
      alert('Registration successful!');
      navigateTo('login');
    } else {
      alert('Please fill in all fields!');
    }
  });
  
  // Login user
  document.getElementById('login-form')?.addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
  
    const users = JSON.parse(localStorage.getItem('users')) || [];
    const user = users.find(u => u.email === email && u.password === password);
  
    if (user) {
      localStorage.setItem('loggedIn', JSON.stringify(user));
      alert('Login successful!');
      navigateTo('task');
      loadTasks(user.email);
    } else {
      alert('Invalid email or password!');
    }
  });

  // Function to recover password
function recoverPassword() {
  // Ask for the email
  const email = prompt("Enter your registered email address:");

  if (email) {
    const users = JSON.parse(localStorage.getItem('users')) || [];
    const user = users.find(u => u.email === email);

    if (user) {
      // Generate a new password (for simplicity, we are generating a random password)
      const newPassword = generateRandomPassword();
      user.password = newPassword;

      // Save the updated user details in local storage
      localStorage.setItem('users', JSON.stringify(users));

      // Alert the user with the new password
      alert(`Your new password is: ${newPassword}`);
    } else {
      alert('Email not found!');
    }
  } else {
    alert('Please enter a valid email!');
  }
}

// Function to generate a random password
function generateRandomPassword() {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let password = '';
  for (let i = 0; i < 8; i++) {  // You can change the length as needed
    const randomIndex = Math.floor(Math.random() * chars.length);
    password += chars[randomIndex];
  }
  return password;
}
  
  // Task Management
  function showTaskForm() {
    document.getElementById('task-form').style.display = 'block';
  }
  
  function addTask() {
    const taskName = document.getElementById('task-name').value;
    const taskDesc = document.getElementById('task-desc').value;
  
    if (taskName && taskDesc) {
      const loggedInUser = JSON.parse(localStorage.getItem('loggedIn'));
      const userTasks = JSON.parse(localStorage.getItem(loggedInUser.email)) || [];
      userTasks.push({ name: taskName, description: taskDesc, status: 'incomplete' });
      localStorage.setItem(loggedInUser.email, JSON.stringify(userTasks));
      loadTasks(loggedInUser.email);
      document.getElementById('task-form').style.display = 'none';
    } else {
      alert('Please fill in all task details!');
    }
  }
  
  // Load tasks when logged in
  function loadTasks(email) {
    const loggedInUser = JSON.parse(localStorage.getItem('loggedIn'));
    document.getElementById('user-name').textContent = loggedInUser.name;
    const tasks = JSON.parse(localStorage.getItem(email)) || [];
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = '';
  
    tasks.forEach((task, index) => {
      const li = document.createElement('li');
      li.classList.add(task.status === 'incomplete' ? 'incomplete' : 'complete');
      li.innerHTML = `
        ${task.name} - ${task.status} 
        <button onclick="updateTaskStatus(${index}, '${email}')">Update Status</button> 
        <button onclick="editTask(${index}, '${email}')">Edit</button>
        <button class="delete" onclick="deleteTask(${index}, '${email}')">Delete</button>
      `;
      taskList.appendChild(li);
    });
  }
  
  // Update task status (completed/incomplete)
  function updateTaskStatus(index, email) {
    const tasks = JSON.parse(localStorage.getItem(email));
    const task = tasks[index];
    task.status = task.status === 'completed' ? 'incomplete' : 'completed';
    localStorage.setItem(email, JSON.stringify(tasks));
    loadTasks(email);
  }
  
  // Edit task
  function editTask(index, email) {
    const tasks = JSON.parse(localStorage.getItem(email));
    const task = tasks[index];
    const newName = prompt('Edit task name', task.name);
    const newDesc = prompt('Edit task description', task.description);
  
    if (newName && newDesc) {
      task.name = newName;
      task.description = newDesc;
      localStorage.setItem(email, JSON.stringify(tasks));
      loadTasks(email);
    }
  }
  
  // Delete task
  function deleteTask(index, email) {
    const tasks = JSON.parse(localStorage.getItem(email));
    tasks.splice(index, 1); // Remove the task from the array
    localStorage.setItem(email, JSON.stringify(tasks));
    loadTasks(email);
  }
  
  // Logout user
  function logout() {
    localStorage.removeItem('loggedIn');
    document.getElementById('login-form').reset();  // Clear login inputs on logout
    navigateTo('login');
  }
  
  // Initialize app (check if user is logged in)
  if (localStorage.getItem('loggedIn')) {
    const loggedInUser = JSON.parse(localStorage.getItem('loggedIn'));
    navigateTo('task');
    loadTasks(loggedInUser.email);
  } else {
    navigateTo('login');
  }
  