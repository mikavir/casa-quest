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

  // Credits to Tim Nelson for helping fix Materialize select bug
  // Wait for the Materialize initialization to complete
  setTimeout(() => {
    // Select each .select-wrapper.input-field and swap the label and ul if needed
    $('.select-wrapper.input-field').each(function () {
      const $parentDiv = $(this);

      // get the label and ul within the parent div
      const $label = $parentDiv.children('label');
      const $ul = $parentDiv.children('ul.select-dropdown');
      const $caret = $parentDiv.find('svg.caret');
      const $input = $parentDiv.find('input.select-dropdown');

      // move the label before the ul if it's not already
      if ($label.length && $ul.length && $label.next()[0] !== $ul[0]) {
        $label.insertBefore($ul);
      }

      // Ensure the caret triggers the dropdown
      if ($caret.length && $input.length) {
        $caret.on('click', function () {
          $input.trigger('click');
        });
      }

      // Close the dropdown when an option is clicked
      $ul.children('li').on('click', function () {
        $input.trigger('click');
      });
    });
  }, 0);
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
      $("#manage-account").addClass("hovered");
    },
    function () {
      $("#manage-account").removeClass("hovered");
    }
  );
}