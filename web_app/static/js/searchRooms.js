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
                console.log(responce[message]);   
                if (responce[message] == "found") {
                    document.getElementById("pokoj-check").style.boxShadow = "0 0px 0px 0 rgb( 0,255, 0), 0 0px 6px 0 rgb( 0,255, 0)";
                    document.getElementById("error").style.display="none";
                }else if(responce[message] == "notfound"){
                    document.getElementById("pokoj-check").style.boxShadow = "0 0px 0px 0 rgb(255, 0, 0), 0 0px 6px 0 rgb(255, 0, 0)";
                    document.getElementById("error").style.display="block";
                    } 
                if(responce[message] == "empty"){
                    document.getElementById("pokoj-check").style.boxShadow = "0 0px 0px 0 rgb( 0,0, 0), 0 0px 0px 0 rgb( 0,0, 0)";
                    document.getElementById("error").style.display="none";
                }
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