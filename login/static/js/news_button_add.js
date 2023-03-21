$(document).on('click', '.delete-post', function(e) {
    e.preventDefault();
    var url = $(this).data('url');
    $('#delete-form').attr('action', url);
    $('#deleteModal').modal('show');
  });


    