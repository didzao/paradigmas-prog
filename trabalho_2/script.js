const form = document.querySelector("#form");
const lists = document.querySelector("#lists");
const input = document.querySelector("#input");

class LocalStorage {
    static addTodoStorage(todoList) {
        let storage = localStorage.setItem("todo", JSON.stringify(todoList));
        return storage;
    }

    static getStorage() {
        let storage = localStorage.getItem("todo") === null ? [] : JSON.parse(localStorage.getItem('todo'));
        return storage;
    }
}

let todoList = LocalStorage.getStorage();

class Todo {
    constructor(id, todo) {
        this.id = id;
        this.todo = todo;
    }
}

class DisplayTodo {
    static displayData() {
        let displayData = todoList.map(item => {
            return (
                `
                    <div class="todo">
                        <p>${item.todo}</p>
                        <i class="fa-solid fa-trash-can" id=${item.id}></i>
                    </div>
                `
            );
        });
        lists.innerHTML = (displayData).join(" ");
    }

    static clearInput() {
        input.value = "";
    }

    static removeTodoList(id) {
        todoList = todoList.filter(item => item.id !== +id);
        LocalStorage.addTodoStorage(todoList);
    }

    static removeTodo() {
        lists.addEventListener('click', e => {
            const target = e.target;
            const trashIcon = target.classList.value.includes('trash');
            if (trashIcon) {
                target.parentElement.remove();
            }
            let buttonId = target.id;

            DisplayTodo.removeTodoList(buttonId);
        });
    }
}

form.addEventListener("submit", e => {
    e.preventDefault();

    let id = Math.floor(Math.random() * 100000);

    const todo = new Todo(id, input.value);

    todoList = [...todoList, todo];

    DisplayTodo.displayData();
    DisplayTodo.clearInput();

    LocalStorage.addTodoStorage(todoList);
});

window.addEventListener("DOMContentLoaded", () => {
    DisplayTodo.displayData();
    DisplayTodo.removeTodo();
})





