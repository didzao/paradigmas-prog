const userSpan = document.querySelector("#userSpan");

const userText = `Olá, ${localStorage.getItem('user')}`;
const messageGreetings = document.createTextNode(userText);
userSpan.appendChild(messageGreetings);

console.log('>>>>', userText)

