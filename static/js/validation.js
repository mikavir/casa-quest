function validateHouseInfo() {
    let epc = document.forms["add_house_info"]["add_epc"].value;
    let taxBand = document.forms["add_house_info"]["add_tax_band"].value;
    let floodRisk = document.forms["add_house_info"]["add_flood_risk"].value;
    let internetSpeed = document.forms["add_house_info"]["add_internet_speed"].value;
    let errorMessage = document.getElementById("add-house-info-error");

    if (epc == "" || taxBand == "" || floodRisk == "" || internetSpeed == "") {
        console.log("validation failed");
        errorMessage.innerText = "Please fill out all the required fields";
        return false;
    } 
}

function validateEditHouseInfo() {
    let epc = document.forms["edit-house-info"]["epc"].value;
    let taxBand = document.forms["edit-house-info"]["tax_band"].value;
    let floodRisk = document.forms["edit-house-info"]["flood_risk"].value;
    let internetSpeed = document.forms["edit-house-info"]["internet_speed"].value;
    let errorMessage = document.getElementById("edit-house-info-error");

    if (epc == "" || taxBand == "" || floodRisk == "" || internetSpeed == "") {
        console.log("validation failed");
        errorMessage.innerText = "Please fill out all the required fields";
        return false;
    } 
}

// Form validation for adding House viewing information
function validateAddHouseViewing() {
    let sellersSituation = document.forms["add-house-viewing"]["add_sellers-sitaution"].value;
    let neighbours = document.forms["add-house-viewing"]["add_neighbours"].value;
    let facilities = document.forms["add-house-viewing"]["add_facilities"].value;
    let traffic = document.forms["add-house-viewing"]["add_traffic"].value;
    let errorMessage = document.getElementById("add-house-viewing-error");

    if (sellersSituation == "" || neighbours == "" || facilities == "" || traffic == "") {
        console.log("validation failed");
        errorMessage.innerText = "Please fill out all the required fields";
        return false;
    } 
}