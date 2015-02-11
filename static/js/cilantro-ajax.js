$(".btn-delete").click(function() {
    if (confirm('Delete recipe?')) {
    var recipeid;
    recipeid = $(this).attr("data-recipeid");
    $.get('/cilantro/delete_recipe/', {recipe_id: recipeid});
    }
});

$(".btn-shopping").click(function() {
    var recipeid;
    var userid;
    recipeid = $(this).attr("data-recipeid");
    userid = $(this).attr("data-userid");
    $.get('/cilantro/add_to_shopping_list/', {recipe_id: recipeid, user_id: userid});
});

$(".btn-clear-list").click(function() {
    if (confirm('Clear shopping list?')) {
    var userid
    userid = $(this).attr("data-userid");
    $.get('/cilantro/clear_shopping_list/', {user_id: userid}, function(data){
        $('#shoplist').hide();
        $('#emptylist').show();
    });
    }
});