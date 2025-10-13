// Gestión simple de usuarios en localStorage.
// Estructura en localStorage: key 'users' => JSON.stringify([{username, password}, ...])

function loadUsers() {
  try {
    const raw = localStorage.getItem('users');
    return raw ? JSON.parse(raw) : [];
  } catch (e) {
    return [];
  }
}

function saveUsers(users) {
  localStorage.setItem('users', JSON.stringify(users));
}

function findUser(username) {
  const users = loadUsers();
  return users.find(u => u.username === username) || null;
}

function validateCredentials(username, password) {
  const u = findUser(username);
  return u && u.password === password;
}

function createUser(username, password) {
  const users = loadUsers();
  users.push({ username, password });
  saveUsers(users);
}

// Inicializar con una cuenta admin si no existe
(function ensureDefaultAdmin(){
  if (!findUser('admin')) {
    const users = loadUsers();
    users.push({ username: 'admin', password: '123' });
    saveUsers(users);
  }
})();

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('loginForm');
  const msg = document.getElementById('loginMessage');
  const regForm = document.getElementById('registerForm');
  const regMsg = document.getElementById('regMessage');

  const tabLogin = document.getElementById('tabLogin');
  const tabRegister = document.getElementById('tabRegister');
  const panelLogin = document.getElementById('panelLogin');
  const panelRegister = document.getElementById('panelRegister');

  function showLogin() {
    panelLogin.style.display = '';
    panelRegister.style.display = 'none';
    tabLogin.classList.add('active');
    tabRegister.classList.remove('active');
  }

  function showRegister() {
    panelLogin.style.display = 'none';
    panelRegister.style.display = '';
    tabLogin.classList.remove('active');
    tabRegister.classList.add('active');
  }

  tabLogin.addEventListener('click', showLogin);
  tabRegister.addEventListener('click', showRegister);

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    msg.style.display = 'none';
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value;

    if (!username || !password) {
      msg.style.display = 'block';
      msg.textContent = 'Complete usuario y contraseña.';
      return;
    }

    if (validateCredentials(username, password)) {
      sessionStorage.setItem('loggedUser', username);
      window.location.href = './index.html';
    } else {
      msg.style.display = 'block';
      msg.textContent = 'Usuario o contraseña incorrectos.';
    }
  });

  regForm.addEventListener('submit', (e) => {
    e.preventDefault();
    regMsg.style.display = 'none';
    const username = document.getElementById('regUsername').value.trim();
    const password = document.getElementById('regPassword').value;

    if (!username || !password) {
      regMsg.style.display = 'block';
      regMsg.textContent = 'Complete usuario y contraseña.';
      return;
    }

    if (password.length < 3) {
      regMsg.style.display = 'block';
      regMsg.textContent = 'La contraseña debe tener al menos 3 caracteres.';
      return;
    }

    if (findUser(username)) {
      regMsg.style.display = 'block';
      regMsg.textContent = 'El usuario ya existe.';
      return;
    }

    createUser(username, password);
    // Auto-login y redirigir
    sessionStorage.setItem('loggedUser', username);
    window.location.href = './index.html';
  });

});
