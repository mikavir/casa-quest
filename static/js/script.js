
$(document).ready(function(){
    $('.hamburger').on("click", function(){
        $(".mobile-menu").toggleClass("open")
    });
   
    const elems = document.querySelectorAll('select');
    M.FormSelect.init(elems)
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
          done: "Select"
        }
      });


});
        