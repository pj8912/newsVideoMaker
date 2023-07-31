


const create_button = document.querySelector('create_btn')
create_button.addEventListener('click', converToVideo)

function convertToVideo(e){
    e.preventDefault()

    let title = document.getElementById('news_title').innerText;
    let description= document.getElementById('news_desc').innerText;
    let image_url= document.getElementById('news_img').src;
    let source_url= document.getElementById('news_source_url').href;


    fetch('/c2video',{
        method:"POST",
        body :JSON.stringify({
            'news_title' :title,
            'news_desc' :description, 
            'news_image_url' :image_url, 
            'news_source_url' :source_url, 
        })
    }) 

}