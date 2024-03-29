const userInput = document.querySelector("#user");
const passwordInput = document.querySelector("#password");
const loginButton = document.querySelector("#loginButton");
const forgotPassword = document.querySelector("#forgotPassword");

let user = "";
let password = "";

loginButton.disabled = true;

userInput.addEventListener('change', e => {
    e.preventDefault();
    const { value } = e.target;
    user = value;
});

passwordInput.addEventListener('change', e => {
    e.preventDefault();
    const { value } = e.target;
    password = value;
});

forgotPassword.addEventListener('click', e => {
    e.preventDefault();
    alert('A SENHA É 117698');
});

const saveUserAtStorage = (user) => {
    let storage = localStorage.setItem("user", user);
    return storage;
}

loginButton.addEventListener('click', e => {
    e.preventDefault();
    saveUserAtStorage(user);
    window.location.href = "todoPage.html";
});


window.addEventListener("change", () => {
    if (user != "" && password === "117698") {
        loginButton.disabled = false;
    } else {
        loginButton.disabled = true;
    }
});

