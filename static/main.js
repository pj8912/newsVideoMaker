// const create_button = document.querySelector('#create_btn')
// create_button.addEventListener('click', saveContent)

// async function saveContent(button) {

//     let card = button.closest('.card');
//     let title = card.document.querySelector('.news_title').innerText;
//     let description = card.document.querySelector('.card-news-description').innerText;
//     let image_url = card.document.querySelector('#news_img').src;
//     let source_url = card.document.querySelector('#news_source_url').href;
//     console.log(title)

//     try {
//         const response = await fetch('/savec', {
//             method: "POST",
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({
//                 'news_title': title,
//                 'news_desc': description,
//                 'news_image_url': image_url,
//                 'news_source_url': source_url,
//             })
//         });

//         const data = await response.json();
//         if (data.status == 0) {
//             console.log(`Status:${data.message}`);
//         } else if (data.status == 1) {
//             console.log(`Status:${data.message}`);
//         }
//     } catch (err) {
//         console.log(err);
//     }

//     // await fetch('/savec', {
//     //     method: "POST",
//     //     headers: {
//     //         'Content-Type': 'application/json'
//     //     },
//     //     body: JSON.stringify({
//     //         'news_title': title,
//     //         'news_desc': description,
//     //         'news_image_url': image_url,
//     //         'news_source_url': source_url,
//     //     })
//     // })
//     //     .then(res => res.json())
//     //     .then(response => {
//     //         if (response.status == 0) {
//     //             console.log(`Status:${response.message}`)
//     //         }
//     //         else if (response.status == 1) {
//     //             console.log(`Status:${response.message}`)
//     //         }
//     //     })
//     //     .catch(err => console.log(err))
// }




async function saveContent(button) {
    let card = button.closest('.card'); // Get the parent card element
    let titleElement = card.querySelector('.news_title');
    let descriptionElement = card.querySelector('.card-news-description');
    let imageElement = card.querySelector('#news_img');
    let sourceElement = card.querySelector('#news_source_url');

    if (!titleElement || !descriptionElement || !imageElement || !sourceElement) {
        console.log("Error: Missing required elements in the card.");
        return;
    }

    let title = titleElement.innerText;
    let description = descriptionElement.innerText;
    let image_url = imageElement.src;
    let source_url = sourceElement.href;
    console.log(title)

    try {
        const response = await fetch('/savec', {
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
        });

        const data = await response.json();
        if (data.status == 0) {
            console.log(`Status:${data.message}`);
        } else if (data.status == 1) {
            console.log(`Status:${data.message}`);
        }
    } catch (err) {
        console.log(err);
    }


}