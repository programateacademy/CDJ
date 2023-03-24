$(document).ready(function() {
  $('.card.event').mouseover(function() {
    $('#' + $(this).attr('id') + ' .text-event').removeClass('d-none');
  });
  $('.card.event').mouseout(function() {
    $('#' + $(this).attr('id') + ' .text-event').addClass('d-none');
  });
});
