
// berger-btn
$('.menu-btn').on('click', function(e) {
    e.preventDefault();
    $('.menu').toggleClass('menu-active');
    $('.content'). toggleClass('content-active');
    $('.menu-btn').toggleClass('menu-btn-active');
})

// menu transform
$('.content, .menu-item').on('click', function() {
    $('.menu').removeClass('menu-active');
    $('.content'). removeClass('content-active');
    $('.menu-btn').removeClass('menu-btn-active');
})

// scroll
$(document).ready(function(){
    $('.menu').on("click","a", function (event) {
      //отменяем стандартную обработку нажатия по ссылке
    event.preventDefault();
      //забираем идентификатор бока с атрибута href
    var id  = $(this).attr('href'),
      //узнаем высоту от начала страницы до блока на который ссылается якорь
        top = $(id).offset().top;
            //анимируем переход на расстояние - top за 1500 мс
    $('body,html').animate({scrollTop: top}, 500);
    });
});
 