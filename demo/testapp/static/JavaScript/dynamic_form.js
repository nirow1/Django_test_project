document.addEventListener("DOMContentLoaded", function () {
    // Select the "+" button and its parent container
    const addButton = document.getElementById("add-item-btn");
    const formContainer = document.getElementById("list-item"); 

    // Add click event listener to the "+" button
    addButton.addEventListener("click", function (event) {
        event.preventDefault(); 

        const itemBox = document.createElement("div");
        itemBox.classList.add("mt-4");
        itemBox.classList.add("list_item_box");
        itemBox.id = "list-item";

        const itemNameLbl = document.createElement("label");
        itemNameLbl.textContent = "Item Name:";
        itemNameLbl.classList.add("list_item_name");
        itemNameLbl.setAttribute("for", "name");

        const itemQuantityLbl = document.createElement("label");
        itemQuantityLbl.textContent = "Quantity:";
        itemQuantityLbl.setAttribute("for", "quantity");

        const itemUnitLbl = document.createElement("label");
        itemUnitLbl.textContent = "Unit:";
        itemUnitLbl.setAttribute("for", "unit");

        // Creating new input fields for the item
        const newInputName = document.createElement("input");
        newInputName.type = "text";
        newInputName.classList.add("form-control");
        newInputName.classList.add("add_list_item");
        newInputName.name = "name";
        newInputName.placeholder = "Enter item";

        const newInputQuantity = document.createElement("input");
        newInputQuantity.type = "number";
        newInputQuantity.classList.add("form-control");
        newInputQuantity.id = "quantity";
        newInputQuantity.name = "quantity";
        newInputQuantity.min = "1";
        newInputQuantity.value = "1";
        newInputQuantity.required = true;

        const newInputUnit = document.createElement("select");
        newInputUnit.classList.add("form-control");
        newInputUnit.id = "unit";
        newInputUnit.name = "unit";

        const options = [
            { value: "g", text: "g" },
            { value: "ml", text: "ml" },
            { value: "pcs", text: "pcs" }
        ];
        options.forEach(({ value, text }) => {
            newInputUnit.appendChild(new Option(text, value));
        });
        itemBox.appendChild(itemNameLbl)
        itemBox.appendChild(newInputName)
        itemBox.appendChild(itemQuantityLbl)
        itemBox.appendChild(newInputQuantity)
        itemBox.appendChild(itemUnitLbl)
        itemBox.appendChild(newInputUnit)

        formContainer.appendChild(itemBox);
    });
});

