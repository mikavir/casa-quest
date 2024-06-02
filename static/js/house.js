/* jshint esversion: 11, jquery: true */

// Main Function
document.addEventListener("DOMContentLoaded", () => {
    addInfoBtnDisplay();
    houseViewDisplay();
    houseCheckDisplay();
});

//  -------------DISPLAY OF MODAL FUNCTIONS------

/** Checks if there is house content, returns a boolean */ 
function isThereHouseContent(houseContent) {

    for (const content of houseContent) {
        if (content.innerText !== "") {
            return true;
        }
    }
    return false;
}

/** Toggle display of the house info content */ 
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
        houseInfoDiv.style.display = "none";
        editInfoBtn.style.display = "none";
        addInfoBtn.style.display = "block";
    }
}

/** Toggle display of the content of house viewing */ 
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

/** Toggle display of the content of house checks*/ 
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

// -------- Form validation of forms in house.html
// https://www.w3schools.com/js/js_validation.asp

/** Form validation for adding House information */ 
function validateHouseInfo() {
    const epc = document.forms.add_house_info.add_epc.value;
    const taxBand = document.forms.add_house_info.add_tax_band.value;
    const floodRisk = document.forms.add_house_info.add_flood_risk.value;
    const internetSpeed = document.forms.add_house_info.add_internet_speed.value;
    const errorMessage = document.getElementById("add-house-info-error");

    if (epc == "" || taxBand == "" || floodRisk == "" || internetSpeed == "") {
        console.log("validation failed");
        errorMessage.innerText = "Please fill out all the required fields";
        return false;
    }
    return true; 
}

/** Form validation for editing House information */ 
function validateEditHouseInfo() {
    const epc = document.forms.edit_house_info.epc.value;
    const taxBand = document.forms.edit_house_info.tax_band.value;
    const floodRisk = document.forms.edit_house_info.flood_risk.value;
    const internetSpeed = document.forms.edit_house_info.internet_speed.value;
    const errorMessage = document.getElementById("edit-house-info-error");

    if (epc == "" || taxBand == "" || floodRisk == "" || internetSpeed == "") {
        console.log("validation failed");
        errorMessage.innerText = "Please fill out all the required fields";
        return false;
    }
    return true; 
}

/** Form validation for adding House viewing information */ 
function validateAddHouseViewing() {
    const sellersSituation = document.forms.add_house_viewing.add_sellers_sitaution.value;
    const neighbours = document.forms.add_house_viewing.add_neighbours.value;
    const facilities = document.forms.add_house_viewing.add_facilities.value;
    const traffic = document.forms.add_house_viewing.add_traffic.value;
    const errorMessage = document.getElementById("add-house-viewing-error");

    if (sellersSituation == "" || neighbours == "" || facilities == "" || traffic == "") {
        console.log("validation failed");
        errorMessage.innerText = "Please fill out all the required fields";
        return false;
    }
    return true;
}

/** Form validation for adding House viewing information */ 
function validateEditHouseViewing() {
    const sellersSituation = document.forms.edit_house_viewing.sellers_sitaution.value;
    const neighbours = document.forms.edit_house_viewing.neighbours.value;
    const facilities = document.forms.edit_house_viewing.facilities.value;
    const traffic = document.forms.edit_house_viewing.traffic.value;
    const errorMessage = document.getElementById("edit-house-viewing-error");

    if (sellersSituation == "" || neighbours == "" || facilities == "" || traffic == "") {
        console.log("validation failed");
        errorMessage.innerText = "Please fill out all the required fields";
        return false;
    }
    return true; 
}

/** Form validation for adding House checks information */ 
function validateAddHouseCheck() {
    const propertyFacing = document.forms.add_house_check.add_property_facing.value;
    const noiseLevel = document.forms.add_house_check.add_noise_level.value;
    const boiler = document.forms.add_house_check.add_boiler_noise.value;
    const storageSpace = document.forms.add_house_check.add_storage_space.value;
    const roofCondition = document.forms.add_house_check.add_roof_condition.value;
    const errorMessage = document.getElementById("add-house-check-error");

    if (propertyFacing == "" || noiseLevel == "" || boiler == "" || storageSpace == ""|| roofCondition == "") {
        console.log("validation failed");
        errorMessage.innerText = "Please fill out all the required fields";
        return false;
    } 
    return true;
}

/** Form validation for editing House checks information */ 
function validateEditHouseCheck() {
    const propertyFacing = document.forms.edit_house_check.property_facing.value;
    const noiseLevel = document.forms.edit_house_check.noise_level.value;
    const boiler = document.forms.edit_house_check.boiler_noise.value;
    const storageSpace = document.forms.edit_house_check.storage_space.value;
    const roofCondition = document.forms.edit_house_check.roof_condition.value;
    const errorMessage = document.getElementById("edit-house-check-error");

    if (propertyFacing == "" || noiseLevel == "" || boiler == "" || storageSpace == ""|| roofCondition == "") {
        console.log("validation failed");
        errorMessage.innerText = "Please fill out all the required fields";
        return false;
    } 
    return true;
}