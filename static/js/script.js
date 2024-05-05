
$(document).ready(function(){
  sideNav();
  selectForm();
  datepicker();
  // filePath();
  
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