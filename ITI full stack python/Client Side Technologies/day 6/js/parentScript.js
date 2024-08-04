let childWindow;
let intervalId;
document.getElementById("openchild").addEventListener("click", function () {
    childWindow = window.open("", "", "width=100,height=100");
    childWindow.document.write("<h1>Child Window</h1>");


    let position = 0;
    let direction = 1;
    intervalId = setInterval(() => {
        if (position >= screen.height - 100 || position <= 0) {
            direction = -direction ;
        }
        position += 5 * direction;
        
        childWindow.moveTo(200, position);
    }, 5000);

    document.getElementById('stopChild').addEventListener('click', function () {
        clearInterval(intervalId);
    })
})