const wrapper = document.querySelector('.main__card-block');

fetch('http://127.0.0.1:8000/api/v1/catalog/')
  .then((response) => response.json())
  .then((data) => {
    data.forEach((item) => {
      let card = document.createElement('a');
      card.classList.add('main__card');
      card.innerHTML = `
        <h2 class="main__card-title">${item.title}</h2>
        <p class="main__card-desc">${item.desc}</p>
        <p class="main__card-date">${item.date_created}</p>
        <a href="#" class="main__card-category">${item.category}</a>
      `
      wrapper.appendChild(card);
    });
  })
  .catch((error) => {
    console.error('Ошибка:', error);
  });