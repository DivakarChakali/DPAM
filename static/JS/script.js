document.addEventListener('DOMContentLoaded', function() {
  const menuToggle = document.querySelector('#ULM-toggle');
  const menuList = document.querySelector('.UL-list');

  menuToggle.addEventListener('click', function() {
    menuList.classList.toggle('active');
  });
});
document.addEventListener('DOMContentLoaded', function() {
  const menuToggle = document.querySelector('#USM-toggle');
  const menuList = document.querySelector('.US-list');

  menuToggle.addEventListener('click', function() {
    menuList.classList.toggle('active');
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const menuToggle = document.querySelector(".menu-toggle");
  const menu = document.querySelector(".menu");

    menuToggle.addEventListener("click", function () {
        menu.classList.toggle("active");
    });
  });
function removeFlashMessage() {
  var flashMessage = document.querySelector('.alert');
  if (flashMessage) {
      setTimeout(function () {
          flashMessage.style.display = 'none';
      }, 5000);  // 5 seconds (5000 milliseconds)
  }
}
// Call the function when the page loads
window.onload = removeFlashMessage;


