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