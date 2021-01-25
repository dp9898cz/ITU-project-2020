const searchField = document.querySelector("#searchField");
console.log("hez0")
searchField.addEventListener("keyup",(e) => {
    const searchValue = e.target.value;
    console.log("searchValue",searchValue);
    console.log("hez1")
    if(searchValue.lenght > 0){
        console.log("hez2")
        
    }
});