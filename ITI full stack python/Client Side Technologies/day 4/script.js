// task 1
for (i = 1; i <= 6; i++) { 
    document.write("<h" + i + ">" + "this is header " + i + "</h" + i + ">");
}

// task 2

let sum = 0;
let value;
while (value != 0) {
    value = prompt("Enter a number(0 to quit): ");
    if (value !=0) {{
        sum += parseInt(value);
    }}
    }

alert("The sum is: " + sum);

// task 3

let userinput = prompt("Enter a expression like 2+3*5: ");
let result = eval(userinput);
alert("the expression you entered is: " + userinput + " and the result is =" + result);

// task 4


let userName;
let birthYear;
let age;

while (true) {
    userName = prompt("Enter your name: ");
    if (isNaN(userName)) {
        birthYear = parseInt(prompt("Enter your birth year: "));
        if (!isNaN(birthYear) && birthYear < 2010) {
            age = 2024 - birthYear;
            document.write("<b>Name:</b> " + userName + "<br>");
            document.write("<b>Birth year:</b> " + birthYear + "<br>");
            document.write("<b>Age:</b> " + age);
            break;
        } else {
            alert("Please enter a valid birth year (less than 2010).");
        }
    } 
    else {
        alert("Please enter a valid name.");

    }
}


