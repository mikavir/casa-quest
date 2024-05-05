
$(document).ready(function(){
  sideNav();
  selectForm();
  datepicker();
  // filePath();
  console.log(isThereHouseContent())
  addInfoBtnDisplay();
  initialiseModal();
  
});

function selectForm(){
  const elems = document.querySelectorAll('select');
  M.FormSelect.init(elems)
}

function datepicker(){
    const elems = document.querySelectorAll('.datepicker');
    const instances = M.Datepicker.init(elems, {
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
          done: "Select"
        }
    });
}

function sideNav() {
  $('.hamburger').on("click", function(){
    $(".mobile-menu").toggleClass("open")
  });
}

function filePath(){
  M.Forms.InitFileInputPath(document.querySelector('#image-url'));
}

function isThereHouseContent (){
  const houseInfoContent = document.querySelectorAll(".house-info-content")
  for(const houseInfo of houseInfoContent){
    if(houseInfo.innerText !== ""){
      return true;     
    }
  }
  return false;
}

function addInfoBtnDisplay (){
  const addInfoBtn = document.querySelector("#add-houseinfo-btn");
  const editInfoBtn = document.querySelector("#edit-houseinfo-btn")

  if (isThereHouseContent) {
    editInfoBtn.style.display = "none";
    addInfoBtn.style.display = "block";
  } else{
    editInfoBtn.style.display = "block";
    addInfoBtn.style.display = "none";
  }
}

function initialiseModal(){
  const elems = document.querySelectorAll('.modal');
  const instances = M.Modal.init(elems, {
    // specify options here
  });
}