const create_button = document.querySelector('#create_btn')
create_button.addEventListener('click', saveContent)

async function saveContent() {

    let title = document.getElementById('news_title').innerText;
    let description = document.getElementById('news_desc').innerText;
    let image_url = document.getElementById('news_img').src;
    let source_url = document.getElementById('news_source_url').href;
    console.log(title)

    await fetch('/savec', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'news_title': title,
            'news_desc': description,
            'news_image_url': image_url,
            'news_source_url': source_url,
        })
    })
        .then(res => res.json())
        .then(response => {
            if (response.status == 0) {
                console.log(`Status:${response.message}`)
            }
            else if (response.status == 1) {
                console.log(`Status:${response.message}`)
            }
        })
        .catch(err => console.log(err))
}