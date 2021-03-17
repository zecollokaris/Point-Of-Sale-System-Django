
// Reveals White Nav Bar On Screen Width (Above) 1200px Width
window.onscroll = function () {
    scrollFunction();
  };
  function scrollFunction() {
    var sn = document.getElementById("sticky_nav");
    if (
      document.body.scrollTop > 100 ||
      document.documentElement.scrollTop > 100
    ) {
      sn.style.top = "0px";
    } else {
      sn.style.top = "-100px";
    }
  }
  
  // Reveals White Nav Bar On Screen Width (Below) 1200px Width
  $(window).scroll(function () {
    if ($(window).scrollTop() > 100) {
      $(".header4").addClass("sticky");
    } else {
      $(".header4").removeClass("sticky");
    }
  });
  
  
  // Makes Transparent Mobile Nav Bar (header3) Disappear On Scroll
  $(window).scroll(function() {
    var x = $(window).width();
    if ($(this).scrollTop() >200) {
      $('.header3').fadeOut();
    } else if (x < 1200)  {
      $('.header3').fadeIn();
    }
  });
  
  
  $(document).ready(function () {
    menu();
    function menu() {
      $('.hamburger-menu').click(function () {
          $('html').toggleClass('open-menu');
      });
    }
  });
  
  
  var open = document.querySelectorAll('.open')[0];
  var close = document.querySelectorAll('.close')[0];
  open.addEventListener("click", animate);
  close.addEventListener("click", animate);
  
  function animate($e){
    if (open.classList.contains('clicked')) {
      //if the menu is already opend and the user clicks
      //add the rewind animation to revert back to hamburger
        open.classList.remove("clicked");
        close.classList.remove("clicked");
        open.classList.add("clicked-rewind");
        close.classList.add("clicked-rewind");     
    }
    else{
      //if the menu is clicked and not already open show click animation
      open.classList.add("clicked");
      close.classList.add("clicked");
      open.classList.remove("clicked-rewind");
      close.classList.remove("clicked-rewind");
    }
  }
  
  
  // Mebile Menu Slider
  $(function() {
    // Opens Up Mobile Slider Menu
    function slideMenu() {
      var activeState = $(".menu-container .mobile-menu-list").hasClass("active");
      $(".menu-container .mobile-menu-list").animate({left: activeState ? "0%" : "-100%"},);
    }
  
    $("#menu-wrapper").click(function(event) {
      event.stopPropagation();
      $("#hamburger-menu").toggleClass("open");
      $(".menu-container .mobile-menu-list").toggleClass("active");
      slideMenu();
  
      $("body").toggleClass("overflow-hidden");
    });
  
  
    // Opens Up Menu DropDown Options In Menu
    $(".mobile-menu-list").find(".menu-toggle").click(function() {
      $(this).next().toggleClass("open").slideToggle("fast");
      $(this).toggleClass("active-tab").find(".menu-link").toggleClass("active");
  
      $(".mobile-menu-list .submenu-content").not($(this).next()).slideUp("fast").removeClass("open");
      $(".mobile-menu-list .menu-toggle").not(jQuery(this)).removeClass("active-tab").find(".menu-link").removeClass("active");
    });
  });
  
  



  