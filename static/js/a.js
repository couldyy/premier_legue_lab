$(document).ready(() => { 
    let commentForm = $('.commententries form').clone();
    let reply = $('.comment span button');

    reply.on('click', (e) => {
        if(commentForm.hasClass('replyComment')) {
            $('.replyComment').remove();
            commentForm = $('.commententries form').clone();
        } else {
            $(e.target).closest('.reply').append(commentForm);
            commentForm.attr('class', 'replyComment');
        }
    })
});