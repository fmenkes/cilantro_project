$(".btn-delete").click(function() {
    if (confirm('Delete recipe?')) {
    var recipeid;
    recipeid = $(this).attr("data-recipeid");
    $.get('/cilantro/delete_recipe/', {recipe_id: recipeid}});
    }
});