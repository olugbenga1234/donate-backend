
//Get the button:
const btnScrollToTop = document.querySelector("#btnScrollToTop");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    btnScrollToTop.style.display = "block";
  } else {
    btnScrollToTop.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
btnScrollToTop.addEventListener("click", function () {
    window.scrollTo(0, 0);

    window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth"
   })
});


////smooth scroll
$(document).ready(function(){
    // Add smooth scrolling to all links
    $("a").on('click', function(event) {

      //active nav link
      //$("a").css("color","");
      //$(this).css("color","blue")
  
      // Make sure this.hash has a value before overriding default behavior
      if (this.hash !== "") {
        // Prevent default anchor click behavior
        event.preventDefault();
  
        // Store hash
        var hash = this.hash;
  
        // Using jQuery's animate() method to add smooth page scroll
        // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
        $('html, body').animate({
          scrollTop: $(hash).offset().top
        }, 100, function(){

            // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
    });
  } // End if
});
});

