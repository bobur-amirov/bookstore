$(document).on('click', '#likeButton', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '{% url "like" %}',
        data: {
            book_slug: $('#likeButton').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success: function (json) {
            document.getElementById("likeAll").innerHTML = json['book_likes']
            // console.log(json)
        }
    })
})