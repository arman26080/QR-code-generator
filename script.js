function generateQR() {
    let text = document.getElementById("qr-text").value;
    if (text === "") {
        alert("Please enter text or URL!");
        return;
    }

    fetch("/generate_qr", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        let img = document.getElementById("qr-image");
        img.src = data.qr_code;
        img.style.display = "block";
    });
}
