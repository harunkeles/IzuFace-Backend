// var menu = ['Slide 1', 'Slide 2', 'Slide 3']
var swiper = new Swiper(".mySwiper.std-aboutTab-certificates", {
    slidesPerView: 2,
    spaceBetween: 10,
    navigation: {
        nextEl: ".std-aboutTab-certificates .swiper-button-next",
        prevEl: ".std-aboutTab-certificates .swiper-button-prev",
    },
    pagination: {
        el: ".std-aboutTab-certificates .swiper-pagination",
        clickable: true,
        //   renderBullet: function (index, className) {
        //     return '<span class="' + className + '">' + (menu[index]) + '</span>';
        //   },
    },
    mousewheel: false,
    keyboard: true,
});


//?  User Images click-prop

function studentUserImageModal(i) {
    var modal = document.getElementById('studentUser-img-modal');
    var modalImg = document.getElementById("studentUser-modal-image");
    var captionText = document.getElementById("studentUser-modal-caption");
    var top_izu_face_logo = document.getElementById("myProfilePage__izu-face-logo")
    var main_hamburger_menu = document.getElementById("mainMenu")    

    var cerimg = document.getElementById('studentUser-image-' + i);
    modal.style.display = "block";
    modalImg.src = cerimg.src;
    captionText.innerHTML = cerimg.alt;
    top_izu_face_logo.style.display = "none";
    main_hamburger_menu.style.display = "none";

    var span = document.getElementById("studentUser-img-modal-close");

    span.onclick = function () {
        modal.style.display = "none";
        top_izu_face_logo.style.display = "block";
        main_hamburger_menu.style.display = "block";
    
    }
}



//?  Certificate click-prop

function cerImageModal(i) {
    var modal = document.getElementById('cer-img-modal');
    var modalImg = document.getElementById("modal-image");
    var captionText = document.getElementById("modal-caption");
    var top_izu_face_logo = document.getElementById("myProfilePage__izu-face-logo")
    var main_hamburger_menu = document.getElementById("mainMenu")    

    var cerimg = document.getElementById('cer-image-' + i);
    modal.style.display = "block";
    modalImg.src = cerimg.src;
    captionText.innerHTML = cerimg.alt;
    top_izu_face_logo.style.display = "none";
    main_hamburger_menu.style.display = "none";

    var span = document.getElementById("cer-img-modal-close");

    span.onclick = function () {
        modal.style.display = "none";
        top_izu_face_logo.style.display = "block";
        main_hamburger_menu.style.display = "block";
    
    }
}

