document.getElementById('urlForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const resourceUrl = document.getElementById('resourceUrl').value;

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
    this.reset();
});

function displayResult(short_id) {
    const resultDiv = document.getElementById('result');
    
    resultDiv.innerHTML = `Shortened URL: <a href="http://localhost:8000/${short_id}" target="_blank">http://localhost:8000/${short_id}</a>`;

    resultDiv.style.display = 'block';
}
