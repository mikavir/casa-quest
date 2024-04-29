
$(document).ready(function(){
    $('.sidenav').sidenav();
    $( ".close-btn" ).on( "click", function() {
        $('.sidenav').sidenav('close')
    })
  });
        