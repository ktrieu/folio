$(document).ready(() => {
    let markdownArea = $('#markdownArea');
    let htmlPreview = $('#htmlPreview');
    let saveText = $('#saveText');
    let dirty = true;
    setInterval(() => {
        if (dirty) {
            let text = markdownArea.val();
            $.post('/blog/render_markdown/', text, (resp) => {
                htmlPreview.empty();
                htmlPreview.append($(resp));
                dirty = false;
            });
            saveText.text('Saving...')
            $.post('../save_markdown/', text, (resp) => {
                saveText.text('Saved.')
            });
        }
    }, 750);

    markdownArea.on('input', () => {
        dirty = true;
    });
})