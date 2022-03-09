/// Weather Api 
async function loadWeatherStatus() {
    const response = await fetch('/api/weather');
    const data = await response.json();

    document.getElementById("degree-number").innerHTML = Math.round(data.result.main.temp - 273, 15) + "°";
    document.getElementById("weather-wind").innerHTML = Math.round(data.result.wind.speed * 3, 6);
    document.getElementById("highest-temp").innerHTML = Math.round(data.result.main.temp_max - 273, 15);
    document.getElementById("lower-temp").innerHTML = Math.round(data.result.main.temp_min - 273, 15);
    document.getElementById("weather-prop").innerHTML = data.result.weather[0].description;

    if (data.result.weather[0].description == "açık") {
        document.getElementById("weather-icon").innerHTML = '<div class="sun"></div>';
    } else if (data.result.weather[0].description == "kapalı" || data.result.weather[0].description == "hafif yağmur"|| data.result.weather[0].description == "parçalı bulutlu"  ) {
        document.getElementById("weather-icon").innerHTML =
            ' <div class="cloud"></div>' +
            '<div class="moon small-moon"></div>' +
            '<div class="wind">' +
            '<span></span>' +
            '<span></span>' +
            '<span></span>' +
            '<span></span>' +
            ' </div>';
    }
}
loadWeatherStatus();



/// Main Page Announcments

var swiper = new Swiper("#news-card-1 .swiper.m-p-news", {
    slidesPerColumn: 1,
    spaceBetween: 30,
    slidesPerView: 3,
    grid: {
        rows: 2,
      },
    navigation: {
        nextEl: "#news-card-1 .swiper.m-p-news .swiper-button-next",
        prevEl: "#news-card-1 .swiper.m-p-news .swiper-button-prev",
    },
    pagination: {
        el: "#news-card-1 .swiper.m-p-news .swiper-pagination",
        clickable: true,
    },
    keyboard: true,
});



/// Main Page Last Post Content

var swipers = new Swiper("#last__posts__swipper", {
    slidesPerView: 3,
    slidesPerColumn: 3,
    spaceBetween: 30,
    navigation: {
        nextEl: ".last__post__summary__row .swiper-button-next",
        prevEl: ".last__post__summary__row .swiper-button-prev",
    },
    pagination: {
        el: ".last__post__summary__row .swiper-pagination",
        clickable: true,
    },
    keyboard: true,
});


