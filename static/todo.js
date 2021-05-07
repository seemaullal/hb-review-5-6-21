document.getElementById("get-todo-list").addEventListener("click", () => {
    // add a loading bar to the page
    fetch("/api/todos") // fetch has an optional 2nd argument used for options
    .then((response) => response.json())
    .then((todoData) => {
        for (const item of todoData) {
            const { title } = item; // const title = item.title
            const el = document.createElement('div');
            el.textContent = title;
            document.querySelector('.container').append(el)
        }
        // remove loading bar to the page
    });
});
// Axios - JS library that is a wrapper to parse
