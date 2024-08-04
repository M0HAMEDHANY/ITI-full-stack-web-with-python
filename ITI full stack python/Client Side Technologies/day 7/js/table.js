
                                                                    // string manipulation
// const row = 3;
// const col = 4;
// let tableHtml = '<table border="1" width="80%">';

// for (let i = 1; i < row+1; i++){
//     tableHtml+= '<tr>';

//     for (let j = 1; j < col+1; j++){
//         tableHtml += `<td>${i} ${j}</td>`;
//     }
//     tableHtml += '</tr>';
// }
// tableHtml+='</table>';
// document.body.innerHTML = tableHtml
                                                                // DOM manipulation 
const table = document.createElement('table');
const row = 3;
const column = 4;
table.setAttribute('border', '1');
table.style.width = '80%';

for (let i = 1; i < row + 1; i++) {
    const tr = document.createElement('tr');

    for (let j = 1; j < column + 1; j++) {
        const  td = document.createElement('td');
        td.appendChild(document.createTextNode(`${i} ${j}`));
        tr.appendChild(td);
    }

    table.appendChild(tr);
}

document.body.appendChild(table);

