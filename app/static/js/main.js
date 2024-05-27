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
    const shortUrlSpan = document.getElementById('shortUrl');
    const shortUrl = `http://localhost:8000/${short_id}`;

    shortUrlSpan.innerHTML = `Shortened URL: <a href="${shortUrl}" target="_blank">${shortUrl}</a>`;

    resultDiv.style.display = 'block';

    document.getElementById('copyButton').addEventListener('click', function() {
        copyToClipboard(shortUrl);
    });
}

function copyToClipboard(text) {
    const tempInput = document.createElement('input');
    tempInput.style.position = 'absolute';
    tempInput.style.left = '-9999px';
    tempInput.value = text;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    document.body.removeChild(tempInput);
    alert('URL copied to clipboard!');
}
