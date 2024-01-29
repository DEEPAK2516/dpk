<?php
// Check if it's a GET request
if ($_SERVER['REQUEST_METHOD'] == "GET") {
    // Get the values from the URL parameters
    $storeVal1 = isset($_GET["a1"]) ? $_GET["a1"] : null;
    $storeVal2 = isset($_GET["a2"]) ? $_GET["a2"] : null;
    $storeVal3 = isset($_GET["a3"]) ? $_GET["a3"] : null;

    // Perform any operations with the received values
    // For example, you can store them in a database or perform calculations
    // In this example, we'll just print them
    echo "Received values: a1=$storeVal1, a2=$storeVal2, a3=$storeVal3";
} else {
    // If it's not a GET request, handle accordingly
    echo "Invalid request method.";
}
?>
