const wrapper = document.querySelector('.main__card-block');
const catalogApi = 'http://127.0.0.1:8000/api/v1';
let path = window.location.pathname;

fetch(catalogApi + path)
    .then((response) => response.json())
    .then((data) => {
        let card = document.createElement('a');
        card.classList.add('main__card');
        card.innerHTML = `
            <h2 class="main__card-title">${data.title}</h2>
            <p class="main__card-desc">${data.desc}</p>
            <p class="main__card-date">${data.date_created}</p>
            <p class="main__card-desc">${data.author}</p>
            <a href="?category=${data.category}" class="main__card-category">${data.category}</a>
            <form method="post" class="main__card-func">
                <input hidden name="method" value="DELETE">
                <input hidden name="csrfmiddlewaretoken" value="${document.cookie.split('=')[1]}">
                <button class="main__card-delete" id="delete_card">delete</button>
            </form>
            <form method="post" class="main__card-func">
                <input hidden name="method" value="PUT">
                <input hidden name="csrfmiddlewaretoken" value="${document.cookie.split('=')[1]}">
                <input type="text" name="title" value=${data.title}>
                <input type="text" value=${data.desc}>
                <input type="text" value=${data.author}>
                <button class="main__card-delete" id="delete_card">Update</button>
            </form>
            <button class="main__card-delete" id="delete_card">________</button>
        `;
        wrapper.appendChild(card);

    });
