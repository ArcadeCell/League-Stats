const bootstrapScript = document.createElement('script');
bootstrapScript.src = 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js';
bootstrapScript.integrity = 'sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe';
bootstrapScript.crossOrigin = 'anonymous';

document.head.appendChild(bootstrapScript);

const searchButton = document.getElementById("searchButton");
const loader = document.getElementById("loader");

searchButton.addEventListener('click', () =>{
    loader.classList.remove("d-none");
    setTimeout(() =>{
        loader.classList.add("d-none");
    }, 12000);
});



