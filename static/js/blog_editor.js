$(document).ready(() => {
    let csrfToken = Cookies.get('csrftoken');

    let markdownArea = $('#markdownArea');
    let htmlPreview = $('#htmlPreview');
    let saveText = $('#saveText');
    let dirty = true;
    setInterval(() => {
        if (dirty) {
            let text = markdownArea.val();
            $.post({
                url: '/blog/render_markdown/',
                data: text,
                headers: {
                    'X-CSRFToken': csrfToken
                },
                success: (resp) => {
                    htmlPreview.empty();
                    htmlPreview.append($(resp));
                    dirty = false;
                }
            });
            saveText.text('Saving...')
            $.post({
                url: '../save_markdown/',
                data: text,
                headers: {
                    'X-CSRFToken': csrfToken
                },
                success: (resp) => {
                    saveText.text('Saved.');
                }
            })
        }
    }, 750);

    markdownArea.on('input', () => {
        dirty = true;
    });
})