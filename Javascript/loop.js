//Prime Numbers
"use strict"
let flag = true;
let size = prompt("Enter the number till which you want Prime Numbers", '2')
outer:
for (let i = 2; i <= size ; i++) {
    flag = true; 
    for(let j = 2 ; j < i; j++) {
        if( i % j == 0) {
            flag = false;
            //continue outer;
        }
    }
    if(flag) {
        alert(i);
    }
}