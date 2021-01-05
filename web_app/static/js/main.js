function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
        document.getElementById("active").style.float = "none";
    } else {
        x.className = "topnav";
        document.getElementById("active").style.float = "left";
    }
    function kontrola_pokoje() {
        var obsah = document.getElementById("number").innerHTML; 
        var rooms = {{rooms}};
        print(rooms);
       /* {% for u in uklidy %}
            var id = {{ u.room.number }};
            var nalezen = 0;
            if (id == obsah) {
                nalezen = 1;
                break;
            } 
        {% endfor %}*/

        if (nalezen == 0) {
                document.getElementById("pokoj-check").style.box-shadow = "none";
        }else (nalezen == 1){
                document.getElementById("pokoj-check").style.box-shadow = "0 0px 0px 0 rgb(255, 0, 0), 0 0px 6px 0 rgb(255, 0, 0)";
                alert("Číslo tohoto pokoje neexistuje!");
            } 
}