const searchField = document.querySelector("#searchField");

searchField.addEventListener("keyup",(e) => {
    const searchValue = e.target.value;
    console.log("hez")
    if(searchValue.lenght > 0){
        console.log("searchValue",searchValue);
    }
})