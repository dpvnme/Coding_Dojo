// DOM

var myObject = {
    name: "Gabe",
    location: "Irvine"
}

myObject.name = "Tood";

// console.dir(document);

// console.dir(document.getElementById("target"));

// var h1 = document.getElementById("target");
// h1.innerText = "Javascript Blows My Mind";

// console.log($);



// $("button").click(function () {
//     console.log("hello world");
//     $("#target").text("jQuery Blows My Mind");
// })

$("button").click(
    function(){
        console.log("I did something");
        $("#target").fadeOut();
    }
)