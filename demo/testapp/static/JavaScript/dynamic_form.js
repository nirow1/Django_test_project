document.addEventListener("DOMContentLoaded", function () {
    // Select the "+" button and its parent container
    const addButton = document.getElementById("add-item-btn");
    const formContainer = document.getElementById("list-item"); 

    // Add click event listener to the "+" button
    addButton.addEventListener("click", function (event) {
        event.preventDefault(); 

        // Create a new input field for the item name
        const newInput = document.createElement("input");
        newInput.type = "text";
        newInput.classList.add("form-control");
        newInput.classList.add("add_list_item");
        console.log(newInput.classList)
        newInput.name = "name";
        newInput.placeholder = "Enter item";
        formContainer.appendChild(newInput);
    });
});

