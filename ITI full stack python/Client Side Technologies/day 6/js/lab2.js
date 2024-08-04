const books = [
    {
        title: 'Bill Gates',
        author: 'The Road Ahead',
        readingStatus: true
    },
    {
        title: 'Steve Jobs',
        author: 'Walter Isaacson',
        readingStatus: true
    },
    {
        title: 'Mockingjay: The Final Book of The Hunger Games',
        author: 'Suzanne Collins',
        readingStatus: false
    }
];

books.forEach(book => {
    if (book.readingStatus) {
        document.write(`Already read '${book.title}' by ${book.author}. <br>`);
    } else {
        document.write(`You still need to read '${book.title}' by ${book.author}. <br> <hr>`);
    }
});


function convertHours(hour) {
    const minutes = hour * 60;
    const seconds = minutes * 3600;
    return {
        hour: hour,
        minutes: minutes,
        seconds: seconds
    }
}
const time = convertHours(4);
document.write(`Hours : ${time.hour} <br>
                Minutes : ${time.minutes} <br>
                Seconds : ${time.seconds}<hr>`)


function testArray(numbers) {
    const length = numbers.length;
    const smallest = Math.min(...numbers);
    const biggest = Math.max(...numbers);
    const sum = function () {
        let total = 0;
        for (let i = 0; i < length; i++) {
            total += numbers[i];
        }
        return total
    }
    const average = sum() / length;

    return {
        length: length,
        smallest: smallest,
        biggest: biggest,
        average: average
    }

}

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const result = testArray(numbers);
document.write(`Length : ${result.length} <br>
                Smallest : ${result.smallest} <br> 
                Biggest : ${result.biggest} <br> 
                Average : ${result.average}`)