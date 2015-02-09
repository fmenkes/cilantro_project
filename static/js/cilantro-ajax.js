$(".btn-delete").click(function() {
    if (confirm('Delete recipe?')) {
    var recipeid;
    recipeid = $(this).attr("data-recipeid");
    $.get('/cilantro/delete_recipe/', {recipe_id: recipeid});
    }
});

$(".btn-shopping").click(function() {
    var recipeid;
    recipeid = $(this).attr("data-recipeid");
    $.get('/cilantro/add_to_shopping_list/', {recipe_id: recipeid});
});

$(".btn-clear-list").click(function() {
    if (confirm('Clear shopping list?')) {
    $.get('/cilantro/clear_shopping_list/', function(data){
        $('#shoplist').hide();
        $('#emptylist').show();
    });
    }
});