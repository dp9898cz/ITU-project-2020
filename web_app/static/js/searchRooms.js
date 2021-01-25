const searchField = document.querySelector("#searchField");
searchField.addEventListener("keyup",(e) => {
    const searchValue = e.target.value;

    if(searchValue.length >= 0){
        console.log(searchValue);
        $.ajax({
            type: "POST",
            contentType: "application/json",
            url: "/search-rooms",
            traditional: "true",
            data: JSON.stringify({searchValue}),
            dataType: "json",
            success: function (responce) {
                console.log(responce);   
            },
        });
    
        /*var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                console.log("hej");
            }
        };
        xhttp.open("POST", "/search-rooms", true);
        xhttp.send();
            */
        /*fetch("/search-rooms",{
            body: searchValue,
            method: "POST",

        })
            .then((text)=>text.json())
            .then((message)=>{
                console.log(message);
        });*/
    }
});