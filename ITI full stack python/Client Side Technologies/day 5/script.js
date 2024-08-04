// task 1
let values =[]
for (let i = 0; i < 3; i++) {
    values.push(parseInt(prompt("Enter a numbers to do the following operations * + - /: ")))
}

let sum = values[0] + values[1] + values[2]
let sub = values[0] - values[1] - values[2]
let mul = values[0] * values[1] * values[2]
let div = values[0] / values[1] / values[2]

document.write(`the sum of the 3 values ${values.join("+")}: ${sum}<br>`)
document.write(`the sub of the 3 values ${values.join("-")}: ${sub}<br>`)
document.write(`the mul of the 3 values ${values.join("*")}: ${mul}<br>`)
document.write(`the div of the 3 values ${values.join("/")}: ${div}<br>`)

// task 2 

function CalculateCircleArea(radius) {
    radius =parseInt(prompt("Enter the radius of the circle: "))
    let area = Math.PI * radius * radius  // or you can use Math.pow(radius, 2)
    alert("The area of the circle is: " + area)

}
CalculateCircleArea()

function CalculateSquareRoot(number) {
    number =parseInt(prompt("Enter the number to calculate its square root: "))
    let sqrt = Math.sqrt(number)
    alert("The square root of the number is: " + sqrt)
}
CalculateSquareRoot()


function CalculateCosine(angle) {
    angle = parseFloat(prompt("Enter the angle in degrees: "))
    let cos = Math.cos(angle * Math.PI / 180)
    alert("The cosine of the angle is: " + cos)
}
CalculateCosine()

// task 3


let mystring =prompt("Enter a string to count the number of the letter e in it: ")
mystring = mystring.toLowerCase()
console.log(mystring)
let count = 0
for (let i = 0; i < mystring.length; i++) {
    if (mystring[i] == "e") {
        count++
    }
}
alert(`the number of the letter e in the string is: ${count}`)


// task 4


let array = []
for (let i = 0; i < 5; i++) {
    array.push(parseInt(prompt("enter 5 elements to sort them in ascending and descending order")))
}
ascending = [...array].sort( (a,b) => a - b)

descending = [...array].sort( (a,b) => b - a)

alert(`the numbers in ascending order are: ${ascending}`)
alert(`the numbers in descending  order are: ${descending }`)
