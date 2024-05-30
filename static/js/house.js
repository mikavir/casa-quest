
document.addEventListener("DOMContentLoaded", () => {
    addInfoBtnDisplay();
    houseViewDisplay();
    houseCheckDisplay();
});



function isThereHouseContent(houseContent) {

    for (const content of houseContent) {
        if (content.innerText !== "") {
            return true;
        }
    }
    return false;
}

function addInfoBtnDisplay() {
    const addInfoBtn = document.getElementById("add-houseinfo-btn");
    const editInfoBtn = document.getElementById("edit-houseinfo-btn");
    const houseInfoDiv = document.getElementById("house-info");
    const houseInfoContent = document.querySelectorAll(".house-info-content");

    if (isThereHouseContent(houseInfoContent)) {
        houseInfoDiv.style.display = "block";
        editInfoBtn.style.display = "block";
        addInfoBtn.style.display = "none";

    } else {
        houseInfoDiv.style.display = "none"
        editInfoBtn.style.display = "none";
        addInfoBtn.style.display = "block";
    }
}

function houseViewDisplay() {
    const addInfoBtn = document.getElementById("add-houseviewing-btn");
    const editInfoBtn = document.getElementById("edit-houseviewing-btn");
    const houseViewingDiv = document.getElementById("house-viewing");
    const houseViewingContent = document.querySelectorAll(".house-viewing-content");

    if (isThereHouseContent(houseViewingContent)) {
        houseViewingDiv.style.display = "block";
        editInfoBtn.style.display = "block";
        addInfoBtn.style.display = "none";

    } else {
        houseViewingDiv.style.display = "none";
        editInfoBtn.style.display = "none";
        addInfoBtn.style.display = "block";
    }
}

function houseCheckDisplay() {
    const addInfoBtn = document.getElementById("add-housecheck-btn");
    const editInfoBtn = document.getElementById("edit-housecheck-btn");
    const houseCheckDiv = document.getElementById("house-check");
    const houseCheckContent = document.querySelectorAll(".house-check-content");

    if (isThereHouseContent(houseCheckContent)) {
        houseCheckDiv.style.display = "block";
        editInfoBtn.style.display = "block";
        addInfoBtn.style.display = "none";

    } else {
        houseCheckDiv.style.display = "none";
        editInfoBtn.style.display = "none";
        addInfoBtn.style.display = "block";
    }
}



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