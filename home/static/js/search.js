const searchBox = document.querySelector('#search-box');
const searchResults = document.querySelector('#search-results');

let allCards = [];

function createCard(result) {
  const card = `
  <div class="container justify-content-center" style="height: 100%;">
  <div class="card hoverable white card-item">
    <div class="card-image waves-effect waves-block waves-light" style="max-width:100%">
      <img class="activator" src="${result.logo}" alt="${result.name} logo" max-width="100%" height="250px">
    </div>
    <div class="card-reveal">
      <span class="card-title text-icons"><i class="material-icons right" style="color:purple">close</i></span>
      <br>
      <p class="text-title-carrusel">${result.name}</p>
      <p class="text-description-carrusel">${result.description.slice(0, 100)}</p>
      <p class="text-email-carrusel ">${result.email}</p>
      <ul class="center-align">
        <li><a class="text-href" href="consejos/${parseInt(result.id)}">Saber más</a></li>
      </ul>
    </div>
  </div>
  </div>
  `;

  const item = document.createElement('div');
  item.classList.add('item');
  item.innerHTML = card;
  return item;
}



// Función para buscar las cartas
function searchCards(query) {
  clearTimeout(timeoutId);
  timeoutId = setTimeout(() => {
    const filteredCards = allCards.filter(card => {
      return card.name.toLowerCase() === query.toLowerCase();
    });
    showSearchResults(filteredCards);
  }, 500);
}


// Carga todas las cartas al iniciar la página
const xhr = new XMLHttpRequest();
xhr.open('GET', '/search_consejos/');
xhr.onload = () => {
  if (xhr.status === 200) {
    const results = JSON.parse(xhr.responseText).results;
    allCards = results;
    showSearchResults(allCards);
  }
};
xhr.send();

let slickCarousel;

function showSearchResults(results) {
  const carousel = document.querySelector('.carousel');
  searchBox.addEventListener('input', (event) => {
    const query = event.target.value.trim();
    searchCards(query);
  });

  // eliminar la carta de la lista de resultados
  if (slickCarousel) {
    slickCarousel.slick('unslick');
  }
  carousel.innerHTML = '';

  const cards = results.map(result => {
    return createCard(result);
  });

  cards.forEach(card => {
    const item = document.createElement('div');
    item.classList.add('item');
    item.innerHTML = card.innerHTML;
    carousel.appendChild(item);
    item.querySelector('.card-item').removeAttribute('style');
  });

  // Configura el carrusel 
  slickCarousel = $('.carousel').slick({
    autoplay: true,
    autoplaySpeed: 2000, 
    slidesToShow: 4,
    slidesToScroll: 4,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
        }
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 400,
        settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]
});

let timeoutId;

function searchCards(query) {
  clearTimeout(timeoutId);
  timeoutId = setTimeout(() => {
    if (query === '') {
      showSearchResults(allCards);
    } else {
      const filteredCards = allCards.filter(card => {
        return card.name.toLowerCase().includes(query.toLowerCase());
      });
      showSearchResults(filteredCards);
    }
  }, 500);
}

}