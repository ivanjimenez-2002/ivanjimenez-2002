// Function to get the number of selected neighbors from radio buttons
function getNeighbors() {
    var neighbors = document.getElementsByName('uiNeighbors'); // Get all elements with the name 'uiNeighbors'
    for (var i in neighbors) { // Loop through all elements
        if (neighbors[i].checked) { // Check if the radio button is selected
            return parseInt(i) + 1; // Return the index + 1 as the selected value
        }
    }
    return -1; // Return -1 if no selection is found
}

// Function to get the number of selected stories from radio buttons
function getStories() {
    var stories = document.getElementsByName('uiStories'); // Get all elements with the name 'uiStories'
    for (var i in stories) {
        if (stories[i].checked) { // Check if the radio button is selected
            return parseInt(i) + 1;
        }
    }
    return -1;
}

// Function to get the number of selected bathrooms from radio buttons
function getBathrooms() {
    var bathrooms = document.getElementsByName('uiBathrooms'); // Get all elements with the name 'uiBathrooms'
    for (var i in bathrooms) {
        if (bathrooms[i].checked) { // Check if the radio button is selected
            return parseInt(i) + 1;
        }
    }
    return -1;
}

// Function to get the number of selected bedrooms from radio buttons
function getBedrooms() {
    var bedrooms = document.getElementsByName('uiBedrooms'); // Get all elements with the name 'uiBedrooms'
    for (var i in bedrooms) {
        if (bedrooms[i].checked) { // Check if the radio button is selected
            return parseInt(i) + 1;
        }
    }
    return -1;
}

// Function to get the number of selected pools from radio buttons
function getPools() {
    var pools = document.getElementsByName('uiPools'); // Get all elements with the name 'uiPools'
    for (var i in pools) {
        if (pools[i].checked) { // Check if the radio button is selected
            return parseInt(i) + 1;
        }
    }
    return -1;
}

// Function to handle the click event of the estimate price button
function onClickedEstimatePrice() {
    console.log("Estimate price button clicked"); // Log button click event
    
    // Get input values from the form
    var sqft = document.getElementById("uiSqft"); // Get the square footage input field
    var landsqft = document.getElementById("uiLandSqft"); // Get the land square footage input field
    var neighbors = getNeighbors(); // Get selected number of neighbors
    var stories = getStories(); // Get selected number of stories
    var bathrooms = getBathrooms(); // Get selected number of bathrooms
    var bedrooms = getBedrooms(); // Get selected number of bedrooms
    var pools = getPools(); // Get selected number of pools
    var estPrice = document.getElementById("uiEstimatedPrice"); // Get the estimated price display element

    // Define the API endpoint for price estimation
    // var url = "http://127.0.0.1:5000/predict_home_price";
    var url = "/api/predict_home_price"; //nginx purposes

    // Send an HTTP POST request to the Flask API
    $.post(url, {
        sqft: parseFloat(sqft.value), // Convert square footage input to a float
        landsqft: parseFloat(landsqft.value), // Convert land square footage input to a float
        neighbors: neighbors, // Pass selected number of neighbors
        stories: stories, // Pass selected number of stories
        bathrooms: bathrooms, // Pass selected number of bathrooms
        bedrooms: bedrooms, // Pass selected number of bedrooms
        pools: pools // Pass selected number of pools
    }, function(data, status) {
        console.log(data.estimated_price); // Log the estimated price returned from the server
        
        // Display the estimated price on the webpage
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " USD</h2>";
        
        console.log(status); // Log the request status
    });
}
