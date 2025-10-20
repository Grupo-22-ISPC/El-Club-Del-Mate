// Usuario definido para pruebas
const usuarioDefinido = {
email: "usuario@correo.com",
password: "123456"
};

document.getElementById("loginForm").addEventListener("submit", function(e) {
e.preventDefault();

const email = document.getElementById("inputEmail").value;
const password = document.getElementById("inputPassword").value;
const mensaje = document.getElementById("loginMessage");

if(email === usuarioDefinido.email && password === usuarioDefinido.password){
    mensaje.textContent = "✅ Acceso correcto. ¡Bienvenido!";
    mensaje.className = "text-success fw-bold mt-3";
} else {
    mensaje.textContent = "❌ Acceso incorrecto. Verifica tu correo o contraseña.";
    mensaje.className = "text-danger fw-bold mt-3";
}
});