// save news content to database
async function saveContent(button) {
    let card = button.closest('.card'); // Get the parent card element
    let titleElement = card.querySelector('.news_title');
    let descriptionElement = card.querySelector('.card-news-description');
    let imageElement = card.querySelector('#news_img');
    let sourceElement = card.querySelector('#news_source_url');
    let news_lang = null;

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
                'news_language' : news_lang
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

// Delete saved news content
async function deleteNews(id){
    const news_id = id.toString();
    console.log(typeof(news_id))
    try{
        const response = await fetch('/deletenews',{
            method:"POST",
            headers : {"Content-Type"  :"application/json"},
            body : JSON.stringify({
                'newsid' : news_id
            })
        });
        const data = await response.json()
        if (data.status == 0){console.log(`Status:${data.message}`)}
        else if (data.status == 1){
            console.log(`Status:${data.message}`)
            // delay a second
            setTimeout(function(){ 
                console.log("Ready")
            }, 1000);
            // reload page
            location.reload();
        }
    }
    catch(err){
        console.log(err)
    }
}



 // JavaScript to toggle the dropdown menu for all divs with class "dropdown"
 const dropdowns = document.querySelectorAll(".dropdown");

 dropdowns.forEach(function(dropdown) {
   const dropbtn = dropdown.querySelector(".dropbtn");
   const dropdownContent = dropdown.querySelector(".dropdown-content");

   dropbtn.addEventListener("click", function() {
     dropdownContent.classList.toggle("show");
   });

   window.addEventListener("click", function(event) {
     if (!dropdown.contains(event.target)) {
       dropdownContent.classList.remove("show");
     }
   });
 });