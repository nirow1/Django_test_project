document.getElementById('datetimeForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent normal form submission

    // Get the value from the datetime-local input
    const datetimeInput = document.getElementById('datetime').value;

    if (datetimeInput) {
        // Parse the input into a JavaScript Date object
        const date = new Date(datetimeInput);

        // Reformat the Date object to DD/MM/YYYY HH:mm
        const formattedDate = `${String(date.getDate()).padStart(2, '0')}/${String(date.getMonth() + 1).padStart(2, '0')}/${date.getFullYear()} ${String(date.getHours()).padStart(2, '0')}:${String(date.getMinutes()).padStart(2, '0')}`;

        console.log("Formatted Date:", formattedDate); // Debugging in console

        // Display the formatted date or process it further
        alert(`You entered: ${formattedDate}`);
    } else {
        alert("Please enter a valid date and time.");
    }
});