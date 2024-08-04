const tips = [
    "Use '===' instead of '==' for comparison.",
    "Use 'let' and 'const' instead of 'var'.",
    "Always end your lines with semicolons.",
    "Use template literals for strings.",
    "Understand the difference between 'null' and 'undefined'.",
    "Use 'map', 'filter', and 'reduce' for array operations.",
    "Keep your functions pure.",
    "Use arrow functions for shorter syntax.",
    "Avoid global variables.",
    "Learn and use async/await for asynchronous operations."
];

document.getElementById('tipButton').addEventListener('click', function () {
    const randomIndex = Math.floor(Math.random() * tips.length);
    alert(tips[randomIndex]);
});