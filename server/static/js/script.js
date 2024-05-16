$(document).ready(function () {
    $('.photos__slider').slick({
        arrows:true,
        adaptiveHeight:true,
        slidesToShow:3,
        infinite:true,
        slidesToSqroll:1,
        appendArrows:$('.photos__slider'),
        asNavFor:".photos__slider-big",
        focusOnSelect:true,
        centerMode:true,
        variableWidth:true,
        responsive: [
            {
                breakpoint:768,
                settings: {
                    slidesToShow:3,
                    arrows:false,

                }
            }
        ]
    });
    $('.photos__slider-big').slick({
        arrows:false,
        fade:false,
        slidesToShow:1,
        asNavFor:".photos__slider"
    });
});