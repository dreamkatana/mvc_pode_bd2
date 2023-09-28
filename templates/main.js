function showCreateForm() {
    document.getElementById('createForm').style.display = 'block';
    document.getElementById('searchForm').style.display = 'none';
}

function showSearchForm() {
    document.getElementById('createForm').style.display = 'none';
    document.getElementById('searchForm').style.display = 'block';
}

document.getElementById('store-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    
    fetch('/loja', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch((error) => {
        console.error('Error:', error);
    });
});

function searchLoja() {
    const name = document.getElementById('search').value;
    
    fetch(`/loja/${name}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('searchResult').innerText = JSON.stringify(data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
