<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Sheet Data Display</title>
</head>
<body>

<h1>Data from Google Sheet</h1>

<div id="dataDisplay"></div>

<script>
// Replace 'YOUR_GOOGLE_APPS_SCRIPT_URL' with the actual URL of your Google Apps Script
const googleAppsScriptURL = 'https://script.google.com/macros/s/AKfycbx73jqC1FCregFnMNEms92eInBaqPQFkKSIceSfSVfYgPlFW0by_Sg_56AVye98xSph/exec
';

// Function to fetch data from the Google Apps Script
async function fetchData() {
    try {
        const response = await fetch(googleAppsScriptURL);
        const data = await response.json();

        // Display the fetched data on the webpage
        displayData(data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Function to display data on the webpage
function displayData(data) {
    const dataDisplayDiv = document.getElementById('dataDisplay');

    if (data.length === 0) {
        dataDisplayDiv.innerHTML = '<p>No data available.</p>';
        return;
    }

    // Create an HTML table to display the data
    const table = document.createElement('table');
    table.border = '1';

    // Create table header
    const headerRow = table.insertRow(0);
    Object.keys(data[0]).forEach(key => {
        const headerCell = document.createElement('th');
        headerCell.textContent = key;
        headerRow.appendChild(headerCell);
    });

    // Create table rows
    data.forEach(rowData => {
        const row = table.insertRow();
        Object.values(rowData).forEach(value => {
            const cell = row.insertCell();
            cell.textContent = value;
        });
    });

    // Append the table to the dataDisplayDiv
    dataDisplayDiv.appendChild(table);
}

// Call the fetchData function when the page loads
document.addEventListener('DOMContentLoaded', fetchData);
</script>

</body>
</html>
