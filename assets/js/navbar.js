function scrollFunction() {
  console.log('scrollFunction')
  const navbar = document.getElementById("navbar");
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    // If scrolled down more than 50px, add the fade-out class
    navbar.classList.add("fade-out");
  } else {
    // If at the top or scrolled up within 50px, remove the fade-out class
    navbar.classList.remove("fade-out");
  }
}