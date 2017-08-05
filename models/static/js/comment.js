$(document).ready(function(){
    $('.reply').click(function(e){
        var dataId = $(this).attr("data-id");
        var className = "#nestedcomment" + dataId
        e.preventDefault();
        $(className).append("<li style='list-style: none;' id='li'><input type='text' id='nested' style='margin-left: 50px;'><button type='submit' id ='post' style='margin-left: 10px'>post</button></li>")
    
        var formid = "#form" + dataId
    
        $(formid).on('submit', function(event){
            event.preventDefault();
            
            //For getting CSRF token
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
            }

            var status_id = $('#state_id').val();
            var reply = $('#nested').val();
            var comment_id = dataId;
            var csrftoken = getCookie('csrftoken');

            var nestedlist = "ul." + dataId;

            $.ajax({
                url : "/postnestedcomment/",
                type : "POST",
                data : { reply : reply, comment_id : comment_id, statusid: status_id, csrfmiddlewaretoken : csrftoken, },
                success : function(json) {
                    $('#nested').val('');
                    $(className).children('#li').remove();
                    $(nestedlist).append("<li>" + reply + "</li>");
                },
                error: function(err){
                    alert(err);
                }
            });
    })

    });
});