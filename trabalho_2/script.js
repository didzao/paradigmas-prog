const form = document.querySelector("#form");
const lists = document.querySelector("#lists");
const input = document.querySelector("#input");
const saveButton = document.querySelector("#saveButton");
const removeAllButton = document.querySelector('#removeAll');

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
                <div class="todoContainer">
                    <p class="todo">${item.todo}</p>
                    <div class="iconContainer">
                        <i class="fa-solid fa-trash" id=${item.id}></i>
                        <i class="fa-solid fa-pen" id=${item.id}></i>
                    </div>
                </div>
                `
            );
        });
        lists.innerHTML = (displayData).join(" ");
    }

    static disableSaveButton(isDisabled = true) {
        saveButton.disabled = isDisabled;
    }

    static clearInput() {
        input.value = "";
        DisplayTodo.disableSaveButton();
    }

    static removeButton() {
        if (todoList.length <= 1) {
            removeAllButton.style.display = "none";
        } else {
            removeAllButton.style.display = "flex";
        }
    }

    static removeAllTodo() {
        removeAllButton.addEventListener('click', () => {
            todoList.length = 0;
            localStorage.clear();
            DisplayTodo.displayData();
            DisplayTodo.removeButton();
        })
    }

    static removeTodoList(id) {
        todoList = todoList.filter(item => item.id !== Number(id));
        LocalStorage.addTodoStorage(todoList);
    }

    static removeTodo() {
        lists.addEventListener('click', e => {
            const target = e.target;
            const trashIcon = target.classList.value.includes('trash');
            if (trashIcon) {
                target.parentElement.parentElement.remove();
                let buttonId = target.id;
                DisplayTodo.removeTodoList(buttonId);
                DisplayTodo.removeButton();
            }
        });
    }

    static editTodo() {
        let iconChange = true;
        const editClass = ['pen', 'check'];

        lists.addEventListener('click', e => {
            console.log('KKKKKKKK')
            const target = e.target;

            const editIcon = editClass.some(element => target.classList.value.includes(element));

            if (editIcon) {
                let todoText = target.parentElement.parentElement.firstElementChild;

                let id = Number(target.id);

                if (iconChange) {
                    todoText.setAttribute("contenteditable", "true");
                    todoText.focus();
                    target.classList.replace("fa-pen", "fa-check");
                    todoText.style.color = "blue";
                } else {
                    target.classList.replace("fa-check", "fa-pen");
                    todoText.style.color = "black"
                    todoText.removeAttribute("contenteditable");

                    const newTodoList = todoList.findIndex(item => item.id === id);
                    todoList[newTodoList].todo = todoText.textContent;
                    LocalStorage.addTodoStorage(todoList);
                }
            }
            iconChange = !iconChange;
        });
    }

    static saveButton(value) {
        if (value === "") {
            DisplayTodo.disableSaveButton();
        } else {
            DisplayTodo.disableSaveButton(false);
        }
    }
}

form.addEventListener("submit", e => {
    e.preventDefault();
    DisplayTodo.saveButton(input.value)
    let id = Math.floor(Math.random() * 100000);

    const todo = new Todo(id, input.value);

    todoList = [...todoList, todo];

    DisplayTodo.displayData();
    DisplayTodo.clearInput();

    LocalStorage.addTodoStorage(todoList);
    DisplayTodo.removeButton();

    console.log(todoList)
});

window.addEventListener("DOMContentLoaded", () => {
    DisplayTodo.disableSaveButton();
    DisplayTodo.displayData();
    DisplayTodo.removeTodo();
    DisplayTodo.editTodo();
    DisplayTodo.removeAllTodo();
    DisplayTodo.removeButton();
})



{/* <div class="todoContainer">
                    <div class="todo">
                        <input type="checkbox" id=${item.id} class="checkbox>
                        <p class="item">${item.todo}</p>
                    </div>
                    <div class="iconContainer">
                        <i class="fa-solid fa-trash-can" id=${item.id}></i>
                        <i class="fa-solid fa-pen" id=${item.id}></i>
                    </div>
                </div> */}




