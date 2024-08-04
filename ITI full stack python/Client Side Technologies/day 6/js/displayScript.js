function display() {
    const name = localStorage.getItem("name");
    const age = localStorage.getItem("age");
    const birthday = localStorage.getItem("birthday");
    const address = localStorage.getItem("address");

    document.getElementById("displayData").innerHTML = `
                <p>Name: ${name}</p>
                <p>Age: ${age}</p>
                <p>Birthday: ${birthday}</p>
                <p>Address: ${address}</p>
            `;
}

window.onload = display();