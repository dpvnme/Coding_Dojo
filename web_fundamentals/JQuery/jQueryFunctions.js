$("#button1").click(function(){
    $(this).parent().find("p").css("color","red");
});

$("#button2").click(function(){
    $(this).parent().find("p").slideToggle();
});

$("#button3").click(function(){
    $(this).parent().find("p").append("<p>This is a new paragraph!</p>");
});

// $("#button4").click(function(){
//     $(this).parent().find("h1").toggle();
//     $(this).toggle(
//         function(){
//             $().text("Show");
//         },
//         function(){
//             $().text("Hide");
//         }
//     );
// });    

// $("#button4").click(function(){
//     $(this).text(function(i,j){
//         return j === "Hide" ? "Show" : "Hide"
//     });
// });

// $("#button4").click(function(){
//     $(this).parent().find("h1").toggle()
// });

$("#button4").click(function(){
    $(this).text(function(i,j){
        return j === "Hide" ? "Show" : "Hide"
    });
    
    $(this).parent().find("h1").toggle();
});

console.dir(document);