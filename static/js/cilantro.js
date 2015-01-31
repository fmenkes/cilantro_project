$(document).ready(function() {
    $(".category-item").click(function() {
        var children = $(this).closest("li").children("ul");
        children.slideToggle();
    });
});