$(document).ready(function () {
    $('#studentUsersAllPostsItems').addClass('list-group-item');
    $('#list').click(function (event) {
        event.preventDefault();
        $('#studentUsersAllPostsItems').addClass('list-group-item');
        $('.sUAICL').removeClass('order-2');
        $('.sUAICR').removeClass('order-1');
        $('#studentUsersAllPostsItems').removeClass('grid-group-item');
    });
    $('#grid').click(function (event) {
        event.preventDefault();
        $('#studentUsersAllPostsItems').removeClass('list-group-item');
        $('.sUAICL').addClass('order-2');
        $('.sUAICR').addClass('order-1');
        $('#studentUsersAllPostsItems').addClass('grid-group-item');
    });
});