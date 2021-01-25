const searchField = document.querySelector("#searchField");
console.log("hez")
searchField.addEventListener("keyup",(e) => {
    const searchValue = e.target.value;

    if(searchValue.lenght > 0){
        console.log(searchValue)
    }
})