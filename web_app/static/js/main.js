function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
        document.getElementById("active").style.float = "none";
    } else {
        x.className = "topnav";
        document.getElementById("active").style.float = "left";
    }
}
kontrola_pokoje(this.value){
    
}