document.getElementById('feedbackForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const feedbacks = document.getElementById('comments').value;
    alert("Your feedback has been sent")
    this.reset();
    try {
        const response = await fetch('/api/feedback', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name : name,
                email : email,
                feedback : feedbacks
            })
        });

        const data = await response.json();

        if (response.ok){
            console.log(data.message);
        }
        else{
            console.error('Error:'+response.statusText+"\n"+data.message);
        }

    } catch (error) {
        console.error('Error:', error);
    }

});
