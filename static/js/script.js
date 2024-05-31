/* jshint esversion: 11, jquery: true */
// Main Function 
$(document).ready(function () {
  sideNav();
  selectForm();
  datepicker();
  initialiseModal();
  initialiseToolTipped();
  initialiseDropdown();
  manageAccount();


});

/** Initialisation of Materialize Select elements*/
function selectForm() {
  const elems = document.querySelectorAll('select');
  M.FormSelect.init(elems);
}


/** Initialisation of Materialize datepicker elements*/
function datepicker() {
  const elems = document.querySelectorAll('.datepicker');
  const today = new Date();
  // Calculate the date 3 months from `today`
  // Credits to Tim Nelson for helping calculate the three months
  const threeMonthsFromToday = new Date(today);
  threeMonthsFromToday.setMonth(today.getMonth() + 3);
  const instances = M.Datepicker.init(elems, {
    format: "dd mmmm, yyyy",
    minDate: today,
    maxDate: threeMonthsFromToday,
    yearRange: 1,
    showClearBtn: true,
    i18n: {
      done: "Select"
    }
  });
}


/** Initialisation of sidenav*/
function sideNav() {
  $('.hamburger').on("click", function () {
    $(".mobile-menu").toggleClass("open");
  });
}



/** Initialisation of Materialize Modal elements*/
function initialiseModal() {
  const elems = document.querySelectorAll('.modal');
  const instances = M.Modal.init(elems);
}


/** Initialisation of Materialize tooltipped elements*/
function initialiseToolTipped() {
  const elems = document.querySelectorAll('.tooltipped');
  const instances = M.Tooltip.init(elems);
}



/** Initialisation of Materialize dropdown elements*/
function initialiseDropdown() {
  const elems = document.querySelectorAll('.dropdown-trigger');
  const instances = M.Dropdown.init(elems, {
    coverTrigger: false,
  });
}


/** Parent link(#manage-account) also changes while child links are hovered */
function manageAccount() {
  $(".manage-account-link").hover(
    function () {
      $("#manage-account").addClass("hovered teal-text text-darken-4");
    },
    function () {
      $("#manage-account").removeClass("hovered teal-text text-darken-4");
    }
  );
}