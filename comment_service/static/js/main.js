$(document).ready(function(){
    $(document).on('click', 'a.reply-comment', function(){
        console.log($(this).data('commentid'));
        console.log($(this).data('depth'));
        var parent = $(this).parent();
        console.log(parent)
        var form = $('#comment_form').clone();
        form.find('input[name="parent"]').val($(this).data('commentid'));
        parent.append(form);
        return false;
    });
    $("a.top-comment").click(function(e){
        e.preventDefault()
        const url = $(this).attr("href");
        var comment_id = $(this).data("commentid");
        console.log($(this).data('depth'));
        console.log(comment_id)
        console.log(url)

        $.ajax({
            url: url,
            type: 'get',
            dataType: 'json',
            success: function(data) {
                console.log(data);
                if (data.has_children) {
                    $.each(data.children, function(key, value) {
                        console.log($('ul.children-' + comment_id))
                        $('ul.children-' + comment_id)
                        .append(
                            $('<li/>').text(value.content)
                                .append(
                                    $('<a/>')
                                        .text('reply')
                                        .addClass('reply-comment')
                                        .data('commentid', value.id)
                                )
        
                        )
                    })
                    // $.map( data.children, function( val, i ) {
                    //     $("#children").append(data.children[i].content) + "<br/>";
                    //   });
                    // for (i = 0; i < data.children.length; i++) {
                    //     document.getElementById("children").innerHTML = data.children[i].content;
                    // }
                  }
            },
            error: function(response) {
                console.log(response)
            }
        })
        return false;
    })
});