const form = document.getElementById('send');
form.addEventListener('submit', (event => {
    event.preventDefault();
    const data = {
        name: form.name.value,
        email: form.email.value,
        message: form.message.value
    };
    fetch('/message', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            toastr.success('Message was sent successfully!');
        } else {

            console.error('Error sending message', data.error);
        }
    })
    .catch(error => {
        console.error("Error:", error);
    })
}))
