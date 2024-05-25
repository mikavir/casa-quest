
$(document).ready(function(){
  sideNav();
  selectForm();
  datepicker();
  initialiseModal();
  initialiseToolTipped();
  initialiseDropdown();

  
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

function initialiseModal(){
  const elems = document.querySelectorAll('.modal');
  const instances = M.Modal.init(elems, {
    // specify options here
  });
}

function initialiseToolTipped(){
  const elems = document.querySelectorAll('.tooltipped');
  const instances = M.Tooltip.init(elems)
}

function initialiseDropdown(){
  const elems = document.querySelectorAll('.dropdown-trigger');
  const instances = M.Dropdown.init(elems,{
    coverTrigger: false,
  });
}
