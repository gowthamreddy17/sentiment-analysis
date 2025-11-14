// Display preloader and hide content
function showPreloader() {
  document.getElementById('preloader').style.display = 'block';
  document.body.style.overflow = 'hidden'; // Hide scrollbar
}

// Hide preloader and show content after 5 seconds
function hidePreloader() {
  setTimeout(function() {
    document.getElementById('preloader').style.display = 'none';
    document.body.style.overflow = 'auto'; // Show scrollbar
  }, 5000); // 5 seconds delay
}

// Call functions to show and hide preloader
showPreloader();
hidePreloader();

