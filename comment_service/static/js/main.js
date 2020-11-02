$(document).ready(function(){
    $("a#top-comment").click(function(e){
        e.preventDefault()
        var subcomments = $(this).val();
        const url = $(this).attr("href");
        console.log(subcomments)
        console.log(url)

        $.ajax({
            url: url,
            type: 'get',
            data: {
                subcomments: subcomments
            },
            dataType: 'json',
            success: function(data) {
                console.log(data);
                if (data.has_children) {
                    $.each(data.children, function(key, value) {
                        document.getElementById("children").innerHTML = data.children[key].content;
                    })
                    // for (i = 0; i < data.children.length; i++) {
                    //     document.getElementById("children").innerHTML = data.children[i].content;
                    // }
                  }
            },
            error: function(response) {
                console.log(response)
            }
        })
    })
});