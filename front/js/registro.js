function validarNombre(nombre) {
    return nombre.trim().length >= 3;
}

function validarEmail(email) {
    const re = /^[\w\.-]+@[\w\.-]+\.\w+$/;
    return re.test(email);
}

function validarContrasena(password) {
    const mayuscula = /[A-Z]/.test(password);
    const minuscula = /[a-z]/.test(password);
    const numero = /[0-9]/.test(password);
    const especial = /[^A-Za-z0-9]/.test(password);
    return password.length >= 8 && mayuscula && minuscula && numero && especial;
}

document.getElementById("registerForm").addEventListener("submit", function(e){
    e.preventDefault();
    const nombre = document.getElementById("inputNombre").value;
    const email = document.getElementById("inputEmail").value;
    const password = document.getElementById("inputPassword").value;
    const mensaje = document.getElementById("registerMessage");

    if(!validarNombre(nombre)){
    mensaje.textContent = "❌ El nombre debe tener al menos 3 letras.";
    mensaje.className = "text-danger fw-bold mt-3";
    return;
    }

    if(!validarEmail(email)){
    mensaje.textContent = "❌ Email inválido.";
    mensaje.className = "text-danger fw-bold mt-3";
    return;
    }

    if(!validarContrasena(password)){
    mensaje.textContent = "❌ La contraseña debe tener al menos 8 caracteres, incluyendo mayúscula, minúscula, número y carácter especial.";
    mensaje.className = "text-danger fw-bold mt-3";
    return;
    }

    // Simulación de registro exitoso
    mensaje.textContent = "✅ Registro válido. ¡Cuenta creada con éxito!";
    mensaje.className = "text-success fw-bold mt-3";
    this.reset();
});