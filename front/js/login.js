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

  // referencias a inputs para validaciones HTML5
  const usernameInput = document.getElementById('username');
  const passwordInput = document.getElementById('password');
  const regUsernameInput = document.getElementById('regUsername');
  const regPasswordInput = document.getElementById('regPassword');

  // defensiva: salir si elementos no existen
  if (!form || !regForm || !tabLogin || !tabRegister || !panelLogin || !panelRegister) return;

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
    if (msg) msg.style.display = 'none';

    // limpiar mensajes previos
    if (usernameInput) usernameInput.setCustomValidity('');
    if (passwordInput) passwordInput.setCustomValidity('');

    const username = usernameInput ? usernameInput.value.trim() : '';
    const password = passwordInput ? passwordInput.value : '';

    // Validación HTML5 antes de procesar
    if ((usernameInput && !usernameInput.checkValidity()) || (passwordInput && !passwordInput.checkValidity())) {
      if (usernameInput && !username) usernameInput.setCustomValidity('Ingrese su usuario.');
      if (passwordInput && !password) passwordInput.setCustomValidity('Ingrese su contraseña.');
      usernameInput && usernameInput.reportValidity();
      passwordInput && passwordInput.reportValidity();
      return;
    }

    if (validateCredentials(username, password)) {
      sessionStorage.setItem('loggedUser', username);
      window.location.replace('./index.html');
    } else {
      if (msg) {
        msg.style.display = 'block';
        msg.textContent = 'Usuario o contraseña incorrectos.';
      }
      // opcional: marcar password como inválido para que el usuario lo note
      if (passwordInput) {
        passwordInput.setCustomValidity(' ');
        passwordInput.reportValidity();
        passwordInput.setCustomValidity('');
      }
    }
  });

  regForm.addEventListener('submit', (e) => {
    e.preventDefault();
    if (regMsg) regMsg.style.display = 'none';

    // limpiar previos
    if (regUsernameInput) regUsernameInput.setCustomValidity('');
    if (regPasswordInput) regPasswordInput.setCustomValidity('');

    const username = regUsernameInput ? regUsernameInput.value.trim() : '';
    const password = regPasswordInput ? regPasswordInput.value : '';

    // Validación HTML5
    if ((regUsernameInput && !regUsernameInput.checkValidity()) || (regPasswordInput && !regPasswordInput.checkValidity())) {
      if (regUsernameInput && !username) regUsernameInput.setCustomValidity('Ingrese un usuario.');
      if (regPasswordInput && !password) regPasswordInput.setCustomValidity('Ingrese una contraseña.');
      regUsernameInput && regUsernameInput.reportValidity();
      regPasswordInput && regPasswordInput.reportValidity();
      return;
    }

    if (password.length < 3) {
      if (regMsg) {
        regMsg.style.display = 'block';
        regMsg.textContent = 'La contraseña debe tener al menos 3 caracteres.';
      }
      if (regPasswordInput) {
        regPasswordInput.setCustomValidity('La contraseña debe tener al menos 3 caracteres.');
        regPasswordInput.reportValidity();
      }
      return;
    }

    if (findUser(username)) {
      if (regMsg) {
        regMsg.style.display = 'block';
        regMsg.textContent = 'El usuario ya existe.';
      }
      if (regUsernameInput) {
        regUsernameInput.setCustomValidity('El usuario ya existe.');
        regUsernameInput.reportValidity();
      }
      return;
    }

    createUser(username, password);
    // Auto-login y redirigir
    sessionStorage.setItem('loggedUser', username);
    window.location.replace('./index.html');
  });

});
