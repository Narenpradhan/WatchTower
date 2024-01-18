fetch('combined_data.json')
    .then(response => response.json())
    .then(data => {
        for (let i = 0; i < data.length; i++){
            let feedItem = data[i]
            appendPost(feedItem)
        }
    })

const feed = document.querySelector(".content-container")
function appendPost(item) {
    feed.innerHTML += `<div class="content">
                            <div class="img"><img src="${item.Img_URL}" alt="" class="content-img"></div>
                            <div class="feed">
                                <div class="feed-header"><a href=${item.Link} target="_blank">${item.Title}</a></div>
                                <div class="feed-meta">
                                    <div><p>${item.Timestamp}</p></div>
                                    <div><p>${item.Source}</p></div>
                                </div>
                            </div>
                        </div>`
}