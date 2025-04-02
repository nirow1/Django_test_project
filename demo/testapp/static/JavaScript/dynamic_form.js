document.addEventListener("DOMContentLoaded", function () {
    // Select the "+" button and its parent container
    const addButton = document.getElementById("add-item-btn");
    const formContainer = document.getElementById("list-item"); // Target the existing inputs container

    // Add click event listener to the "+" button
    addButton.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent button's default behavior

        // Create a new input field for the item name
        const newInput = document.createElement("input");
        newInput.type = "text";
        newInput.classList.add("form-control");
        newInput.name = "name"; // Ensure proper name for input fields
        newInput.placeholder = "Enter item";
        newInput.style.margin = "5px"; // Add spacing

        // Insert the new input field before the "+" button's container
        formContainer.appendChild(newInput);
    });
});

