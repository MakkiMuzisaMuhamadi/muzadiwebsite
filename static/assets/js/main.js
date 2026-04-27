(function () {
  "use strict";

  const body = document.body;
  const mobileToggle = document.querySelector(".mobile-nav-toggle");

  // =============================
  // MOBILE NAV TOGGLE
  // =============================
  if (mobileToggle) {
    mobileToggle.addEventListener("click", function (e) {
      e.preventDefault();
      body.classList.toggle("mobile-nav-active");

      this.classList.toggle("bi-list");
      this.classList.toggle("bi-x");
    });
  }

  // =============================
  // PREVENT MENU AUTO-CLOSING
  // =============================
  document.querySelectorAll("#navmenu a").forEach((link) => {
    link.addEventListener("click", function (e) {

      const parent = this.parentElement;

      // IF DROPDOWN → DO NOT CLOSE MENU
      if (parent.classList.contains("dropdown")) {
        return;
      }

      // NORMAL LINKS → CLOSE MENU
      if (window.innerWidth < 1200) {
        body.classList.remove("mobile-nav-active");

        if (mobileToggle) {
          mobileToggle.classList.add("bi-list");
          mobileToggle.classList.remove("bi-x");
        }
      }
    });
  });

  // =============================
  // MOBILE DROPDOWN (FIXED)
  // =============================
  document.querySelectorAll(".navmenu .dropdown > a").forEach((el) => {
    el.addEventListener("click", function (e) {

      if (window.innerWidth < 1200) {
        e.preventDefault();
        e.stopPropagation();

        const parent = this.parentElement;
        const submenu = parent.querySelector("ul");

        // CLOSE OTHER DROPDOWNS
        document.querySelectorAll(".navmenu .dropdown ul").forEach((menu) => {
          if (menu !== submenu) {
            menu.classList.remove("dropdown-active");
          }
        });

        submenu.classList.toggle("dropdown-active");
      }
    });
  });

  // =============================
  // HERO SLIDER (STABLE)
  // =============================
  const slides = document.querySelectorAll(".hero-slide-item");
  const dots = document.querySelectorAll(".hero-dot");
  const prevBtn = document.querySelector(".hero-nav.prev");
  const nextBtn = document.querySelector(".hero-nav.next");

  if (slides.length > 0) {
    let current = 0;
    let interval;

    function showSlide(index) {
      slides.forEach((slide, i) => {
        slide.classList.remove("active");
        if (i === index) slide.classList.add("active");
      });

      dots.forEach((dot, i) => {
        dot.classList.toggle("active", i === index);
      });

      current = index;
    }

    function nextSlide() {
      current = (current + 1) % slides.length;
      showSlide(current);
    }

    function prevSlide() {
      current = (current - 1 + slides.length) % slides.length;
      showSlide(current);
    }

    function startSlider() {
      interval = setInterval(nextSlide, 5000);
    }

    function stopSlider() {
      clearInterval(interval);
    }

    if (nextBtn) nextBtn.addEventListener("click", () => {
      stopSlider();
      nextSlide();
      startSlider();
    });

    if (prevBtn) prevBtn.addEventListener("click", () => {
      stopSlider();
      prevSlide();
      startSlider();
    });

    dots.forEach((dot, i) => {
      dot.addEventListener("click", () => {
        stopSlider();
        showSlide(i);
        startSlider();
      });
    });

    showSlide(0);
    startSlider();
  }

  // =============================
  // AOS INIT
  // =============================
  if (typeof AOS !== "undefined") {
    AOS.init({
      duration: 800,
      easing: "ease-in-out",
      once: true
    });
  }

})();

