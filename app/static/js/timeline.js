// GET timeline posts ========================================
const posts = document.querySelector('#posts');

// fetch timeline post data from api
const getPosts = () => {
    fetch('/api/timeline_post')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            const posts_data = data['timeline_posts']
            const html = posts_data.map(post2html).join('\n');
            posts.innerHTML = html;
        }
        );
    
}

// prints post
const post2html = (post) =>{
    return `
        <li>Name: ${post['name']},
            Email: ${post['email']}, 
            Content: ${post['content']}</il>
        `
}

getPosts();

// POST a timeline post ====================================

const form = document.querySelector('#form');
 
form.addEventListener('submit', function(e) {
    console.log('listening for form data')
    // Prevent default behavior:
    e.preventDefault();
    // Create new FormData object:
    const formData = new FormData(form);
    console.log(formData)
    // Convert formData object to URL-encoded string:
    const payload = new URLSearchParams(formData);
    console.log(payload)
    // Post the payload using Fetch:
    fetch('/api/timeline_post', {
        method: 'POST',
        body: payload,
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);
        getPosts();
    })
})