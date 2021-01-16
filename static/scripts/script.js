$(document).ready(function() {

  var active1 = false;
  var active2 = false;
  var active3 = false;
  var active4 = false;

    $('.parent2').on('mousedown touchstart', function() {

    if (!active1) $(this).find('.test1').css({'background-color': 'rgba(0,0,0,0.4)', 'transform': 'translate(0px,125px)'});
    else $(this).find('.test1').css({'background-color': 'rgba(0,0,0,0)', 'transform': 'none'});
     if (!active2) $(this).find('.test2').css({'background-color': 'rgba(0,0,0,0.4)', 'transform': 'translate(60px,105px)'});
    else $(this).find('.test2').css({'background-color': 'rgba(0,0,0,0)', 'transform': 'none'});
      if (!active3) $(this).find('.test3').css({'background-color': 'rgba(0,0,0,0.4)', 'transform': 'translate(105px,60px)'});
    else $(this).find('.test3').css({'background-color': 'rgba(0,0,0,0)', 'transform': 'none'});
      if (!active4) $(this).find('.test4').css({'background-color': 'rgba(0,0,0,0.4)', 'transform': 'translate(125px,0px)'});
    else $(this).find('.test4').css({'background-color': 'rgba(0,0,0,0)', 'transform': 'none'});

    active1 = !active1;
    active2 = !active2;
    active3 = !active3;
    active4 = !active4;

    });
});

$(document).ready(function() {
  $("#addusers").click(function() {
    $("#adduserform").toggle();
  });
});


// CHAT BOOT MESSENGER////////////////////////


$(document).ready(function(){
    $(".chat_on").click(function(){
        $(".Layout").toggle();
        $(".chat_on").hide(300);
    });

       $(".chat_close_icon").click(function(){
        $(".Layout").hide();
           $(".chat_on").show(300);
    });

});
