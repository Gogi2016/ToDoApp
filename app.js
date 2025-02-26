// Select DOM elements
const authSection = document.getElementById('authSection');
const taskSection = document.getElementById('taskSection');
const loginForm = document.getElementById('loginForm');
const registerForm = document.getElementById('registerForm');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const taskInput = document.getElementById('taskInput');
const addTaskBtn = document.getElementById('addTaskBtn');
const taskList = document.getElementById('taskList');
const logoutBtn = document.getElementById('logoutBtn');
const forgotPassword = document.getElementById('forgotPassword');

// Local storage keys
const USER_KEY = 'user';
const TASKS_KEY = 'tasks';

// Check if the user is already logged in
function checkUserLogin() {
    const user = JSON.parse(localStorage.getItem(USER_KEY));
    if (user) {
        authSection.style.display = 'none';
        taskSection.style.display = 'block';
        loadTasks();
    }
}

// Login functionality
loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = usernameInput.value;
    const password = passwordInput.value;
    const user = JSON.parse(localStorage.getItem(USER_KEY));

    if (user && user.username === username && user.password === password) {
        authSection.style.display = 'none';
        taskSection.style.display = 'block';
        loadTasks();
    } else {
        document.getElementById('authError').textContent = 'Invalid username or password';
    }
});

// Register functionality
registerForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const newUsername = document.getElementById('newUsername').value;
    const newPassword = document.getElementById('newPassword').value;

    if (newUsername && newPassword) {
        localStorage.setItem(USER_KEY, JSON.stringify({ username: newUsername, password: newPassword }));
        authSection.style.display = 'none';
        taskSection.style.display = 'block';
        loadTasks();
    } else {
        document.getElementById('registerError').textContent = 'Please fill out both fields';
    }
});

// Add new task
addTaskBtn.addEventListener('click', () => {
    const taskDescription = taskInput.value;
    if (taskDescription) {
        const tasks = JSON.parse(localStorage.getItem(TASKS_KEY)) || [];
        tasks.push({ description: taskDescription, status: 'Incomplete' });
        localStorage.setItem(TASKS_KEY, JSON.stringify(tasks));
        taskInput.value = '';
        loadTasks();
    }
});

// Load tasks from local storage
function loadTasks() {
    const tasks = JSON.parse(localStorage.getItem(TASKS_KEY)) || [];
    taskList.innerHTML = '';
    tasks.forEach((task, index) => {
        const li = document.createElement('li');
        li.innerHTML = `
            <span>${task.description}</span> - <span>${task.status}</span>
            <button onclick="updateTaskStatus(${index})">Update Status</button>
            <button onclick="deleteTask(${index})">Delete</button>
        `;
        taskList.appendChild(li);
    });
}

// Update task status
function updateTaskStatus(index) {
    const tasks = JSON.parse(localStorage.getItem(TASKS_KEY));
    tasks[index].status = tasks[index].status === 'Incomplete' ? 'Completed' : 'Incomplete';
    localStorage.setItem(TASKS_KEY, JSON.stringify(tasks));
    loadTasks();
}

// Delete task
function deleteTask(index) {
    const tasks = JSON.parse(localStorage.getItem(TASKS_KEY));
    tasks.splice(index, 1);
    localStorage.setItem(TASKS_KEY, JSON.stringify(tasks));
    loadTasks();
}

// Logout functionality
logoutBtn.addEventListener('click', () => {
    localStorage.removeItem(USER_KEY);
    localStorage.removeItem(TASKS_KEY);
    authSection.style.display = 'block';
    taskSection.style.display = 'none';
});

// Initialize app
checkUserLogin();

