<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Display</title>
    <!-- Add Bootstrap CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous">
    <style>
        body {
            text-align: center;
            background-color: #f0f0f0;
            display: flex;
            justify-content: space-between;
            padding: 20px;
        }

        #left-image-container {
            width: 30%;
            transform: rotate(-5deg); /* Rotate the image slightly */
            overflow: hidden;
        }

        #left-image-container img {
            width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        #data-container {
            width: 60%;
            margin-left: 20px;
        }

        .data-box {
            margin-bottom: 20px;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .date-box {
            background-color: #ffcccb; /* Light red */
        }

        .time-box {
            background-color: #b3e0ff; /* Light blue */
        }

        .meter-box {
            background-color: #c2f0c2; /* Light green */
        }

        .kwh-box {
            background-color: #fcd5ce; /* Light orange */
        }
    </style>
</head>
<body>
    <div id="left-image-container">
        <a href="https://imgbb.com/"><img src="https://i.ibb.co/J3hLKbL/depositphotos-496163538-stock-illustration-poster-energy-saving-image-electric.webp" alt="depositphotos-496163538-stock-illustration-poster-energy-saving-image-electric" border="0"></a>
    </div>

    <div id="data-container">
        <h1>Data Display</h1>
        <!-- Add your data display code here -->
        <div class="data-box date-box"></div>
        <div class="data-box time-box"></div>
        <div class="data-box meter-box"></div>
        <div class="data-box kwh-box"></div>
    </div>

    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
    <script>
        $(document).ready(function () {
            // Function to display data on the webpage
            function displayData(data) {
                // Display each column in a separate box
                $('.date-box').text('Date: ' + data[data.length - 1].ldate);
                $('.time-box').text('Time: ' + data[data.length - 1].ltime);
                $('.meter-box').text('Meter No: ' + data[data.length - 1].meterno);
                $('.kwh-box').text('kWh: ' + data[data.length - 1].kwh);
            }

            // Function to fetch and display data
            function fetchData() {
                // Define the URL of your Google Apps Script web app for retrieving data
                var googleAppsScriptUrl =  'https://script.google.com/macros/s/AKfycbyyx5jYFLfrTY6TnZGAngcT9CC4BQzEt_41v_N-Zj6stm31m3gKXOeRKi6NV_6EqskU6Q/exec';

                // Fetch data from the Google Apps Script web app
                $.getJSON(googleAppsScriptUrl, function (data) {
                    // Display the data on the webpage
                    displayData(data);
                });
            }

            // Fetch and display data initially
            fetchData();

            // Set up a timer to fetch and display data every 5 seconds
            setInterval(fetchData, 5000);
        });
    </script>
</body>
</html>
