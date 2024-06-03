$(document).ready(function () {
  $('#add_item').on('click', function () {
    const item = $('<li></li>').text('Item');
    $('UL.my_list').append(item);
  });
});
