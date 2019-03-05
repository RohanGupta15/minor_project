"use strict"
let num = prompt("Enter the Number", "");
if (+num == 0) {
    alert("Entered Number is Zero");
}
else if (+num >= 0) {
    alert("Positive Number");
}
else if (+num <= 0) {
    alert("Negative Number");
}
else {
    alert("Invalid Number!");
}
