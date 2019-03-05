"use strict"
let currentUser = prompt("Who's There", '');
if(currentUser == 'Admin') {
    let passKey = prompt("Enter Password", '');
    if(passKey == "TheMaster") {
        alert("Welcom Admin!")
    }
    else if(passKey == '' || passKey == null) {
        alert("Cancelled");
    }
    else {
        alert("Wrong Password");
    }s
}
else if(currentUser == '' || currentUser == null) {
    alert("Cancelled");
}
else {
    alert("Sorry I don't know you");
}
