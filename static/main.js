// =========== FOR NOTIFICATION ===============
function notify(text, link = false) {
    n = document.querySelector(".notify")
    if (n !== null) n.remove()
    if (link) {
        el = document.createElement("a")
        el.href = link
    }
    else {
        el = document.createElement("span")
    }
    el.innerText = text
    document.body.append(el)
    el.classList.add('notify')
    setTimeout(function () {
        el.remove()
    }, 3500);
}

// =========== SAVE NEWS CONTENT TO DATABASE ==================
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
                'news_language': news_lang
            })
        });

        const data = await response.json();
        if (data.status == 0) {
            console.log(`Status:${data.message}`);
        } else if (data.status == 1) {
            console.log(`Status:${data.message}`);
            notify("News Saved")
        }
    } catch (err) {
        console.log(err);
    }
}

// ============== DELETE SAVED NEWS =================
async function deleteNews(id) {
    const news_id = id.toString();
    console.log(typeof (news_id))
    try {
        const response = await fetch('/deletenews', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                'newsid': news_id
            })
        });
        const data = await response.json()
        if (data.status == 0) { console.log(`Status:${data.message}`) }
        else if (data.status == 1) {
            console.log(`Status:${data.message}`)
            // delay a second
            setTimeout(function () {
                console.log("Ready")
            }, 1000);
            // reload page
            location.reload();
        }
    }
    catch (err) {
        console.log(err)
    }
}

// =============== EDIT NEWS PAGE ==============================
async function editNews(news_id){
    
    try{
        const response = await fetch("/editnewspage",{
            method : "POST",
            headers : {"Content-Type" : "application/json"},
            body: JSON.stringify({
                'newsid' :news_id
            })
        })
        let response_data = await response.json()
        if(response_data.status == 0) {console.log(`Status:${response_data.message}`)}
        if(response_data.status == 1){}
    }
    catch(err){console.log(err)}
}


// JavaScript to toggle the dropdown menu for all divs with class "dropdown"
const dropdowns = document.querySelectorAll(".dropdown");

dropdowns.forEach(function (dropdown) {
    const dropbtn = dropdown.querySelector(".dropbtn");
    const dropdownContent = dropdown.querySelector(".dropdown-content");

    dropbtn.addEventListener("click", function () {
        dropdownContent.classList.toggle("show");
    });

    window.addEventListener("click", function (event) {
        if (!dropdown.contains(event.target)) {
            dropdownContent.classList.remove("show");
        }
    });
});





// ======== GO TOP BUTTON ==========

// Get the button
let mybutton = document.getElementById("topBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}


// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}


// GOT TO BOTTOM
function gotoBottom(){
    var element = document.getElementById("bottom-btn");
    element.style.display = "block";
    element.scrollTop = element.scrollHeight - element.clientHeight;
 }

