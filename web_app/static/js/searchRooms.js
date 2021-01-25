const searchField = document.querySelector("#searchField");
searchField.addEventListener("keyup",(e) => {
    const searchValue = e.target.value;

    if(searchValue.length > 0){
        console.log(searchValue);
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.response.JSON);
                console.log("hej");
            }
        };
        xhttp.open("POST", "/ahoj", true);
        xhttp.send();
        /*fetch("/search-rooms",{
            body: JSON.stringify({searchText: searchValue}),
            method: "POST",

        })
            .then((res)=> res.json())
            .then((data)=>{console.log("data".data);
        });*/
    }
});