document.addEventListener('DOMContentLoaded', function() {
    var elemssidenav = document.querySelectorAll('.sidenav');
    var instancessidenav = M.Sidenav.init(elemssidenav);
   });

   $(document).ready(function() {
    $('.link').click(function() {
      $('.link').removeClass('active-link');
      $(this).addClass('active-link');
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    var dropdowns = document.querySelectorAll('.dropdown-trigger');
    var options = {
      alignment: 'left'
    }
    var instances = M.Dropdown.init(dropdowns, options);
    
    for (var i = 0; i < instances.length; i++) {
      instances[i].el.addEventListener('click', function(e) {
        var dropdown = e.target.nextElementSibling;
        dropdown.classList.toggle('active');
        dropdown.style.right = 'auto';
        dropdown.style.left = e.target.offsetLeft + 'px';
        dropdown.style.top = e.target.offsetTop + e.target.offsetHeight + 'px';
      });
    }
  });


