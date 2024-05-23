document.getElementById('urlForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const resourceUrl = document.getElementById('resourceUrl').value;

    // Example of how you might send the URL to the backend to be shortened
    try {
        const response = await fetch('/api/shorten', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ resource_url: resourceUrl })
        });
        const data = await response.json();
        displayResult(data.short_id);
    } catch (error) {
        console.error('Error:', error);
        displayResult('An error occurred. Please try again.');
    }
});

function displayResult(short_id) {
    const resultDiv = document.getElementById('result');
    // if (shortUrl.startsWith('http')) {
        // resultDiv.innerHTML = `Shortened URL ID: ${short_id}`;
        resultDiv.innerHTML = `Shortened URL: <a href="http://localhost:8000/${short_id}" target="_blank">http://localhost:8000/${short_id}</a>`;
    // } else {
    //     resultDiv.innerHTML = short_id;
    // }
    resultDiv.style.display = 'block';
}
