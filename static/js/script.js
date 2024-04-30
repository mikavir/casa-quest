
$(document).ready(function(){
    $('.hamburger').on("click", function(){
        $(".mobile-menu").toggleClass("open")
    });
    $('select').formSelect();
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
          done: "Select"
        }
      });


});
        