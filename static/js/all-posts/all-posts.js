var swipers = new Swiper("#allPostPage .featured__posts__swipper", {
    slidesPerView: 3,
    slidesPerColumn: 3,
    spaceBetween: 30,
    navigation: {
        nextEl: "#allPostPage .featured_posts .swiper-button-next",
        prevEl: "#allPostPage .featured_posts .swiper-button-prev",
    },
    pagination: {
        el: "#allPostPage .featured_posts .swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        640: {
            slidesPerView: 1,
            spaceBetween: 20,
        },
        768: {
            slidesPerView: 1,
            spaceBetween: 20,
        },
        900: {
            slidesPerView: 2,
            spaceBetween: 10,
        },
        1100: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        1500: {
            slidesPerView: 2,
            spaceBetween: 50,
        },
        1700: {
            slidesPerView: 3,
            spaceBetween: 20,
        },
        1900: {
            slidesPerView: 3,
            spaceBetween: 20,
        },
        2200: {
            slidesPerView: 4,
            spaceBetween: 20,
        },
        2500: {
            slidesPerView: 4,
            spaceBetween: 20,
        },
    },
    keyboard: true,
});


var swipers = new Swiper("#allPostPage .trend__posts__swipper", {
    slidesPerView: 3,
    slidesPerColumn: 3,
    spaceBetween: 30,
    navigation: {
        nextEl: "#allPostPage .trend_posts .swiper-button-next",
        prevEl: "#allPostPage .trend_posts .swiper-button-prev",
    },
    pagination: {
        el: "#allPostPage .trend_posts .swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        640: {
            slidesPerView: 1,
            spaceBetween: 20,
        },
        768: {
            slidesPerView: 1,
            spaceBetween: 20,
        },
        900: {
            slidesPerView: 2,
            spaceBetween: 10,
        },
        1100: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        1500: {
            slidesPerView: 2,
            spaceBetween: 50,
        },
        1700: {
            slidesPerView: 3,
            spaceBetween: 20,
        },
        1900: {
            slidesPerView: 3,
            spaceBetween: 20,
        },
        2200: {
            slidesPerView: 4,
            spaceBetween: 20,
        },
        2500: {
            slidesPerView: 4,
            spaceBetween: 20,
        },
    },
    keyboard: true,
});


var swipers = new Swiper("#allPostPage .all__posts__categories", {
    slidesPerView: "auto",
    spaceBetween: 30,
    navigation: {
        nextEl: "#allPostPage .all-posts-part .swiper-button-next",
        prevEl: "#allPostPage .all-posts-part .swiper-button-prev",
    },
    pagination: {
        el: "#allPostPage .all-posts-part .swiper-pagination",
        clickable: true,
    },
    freeMode: true,
    keyboard: true,
    mousewheel: true,
});


var swipers = new Swiper("#allPostPage .post_card_tags", {
    slidesPerView: "auto",
    spaceBetween: 20,
    navigation: {
        nextEl: "#allPostPage .post_card_tags .swiper-button-next",
        prevEl: "#allPostPage .post_card_tags .swiper-button-prev",
    },
    freeMode: true,
    keyboard: true,
});



