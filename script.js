function startPasswordBruteForce() {
    const password = document.getElementById('password').value;
    const output = document.getElementById('output');
    output.innerHTML = 'Starting password brute force...';

    fetch('http://127.0.0.1:5000/bruteforce', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ password: password })
    })
    .then(response => response.json())
    .then(data => {
        output.innerHTML = data.result;
    })
    .catch(error => {
        output.innerHTML = 'Error: ' + error;
    });
}

function startDirectoryBruteForce() {
    const password = document.getElementById('password').value;
    const output = document.getElementById('output');
    output.innerHTML = 'Starting directory brute force...';

    fetch('http://127.0.0.1:5000/dir_bruteforce', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ password: password })
    })
    .then(response => response.json())
    .then(data => {
        output.innerHTML = data.result;
    })
    .catch(error => {
        output.innerHTML = 'Error: ' + error;
    });
}
