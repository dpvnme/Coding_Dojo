var x = [1,2,3,4,5,10]
for(var i=0; i<5;i++){   
   console.log(i); //1,2,3,4,5
}

var x = [1,2,3,4,5,10]
for(var i=0; i<5; i++)
{
   i = i + 1;  
   console.log(i);  //1,3,5
}

var x = [1,2,3,4,5,10]
for(var i=0; i<5; i++)
{
   i = i + 3; 
   console.log(i);  //3, 7
}

function y(num1, num2){   
    return num1+num2;
 }
 console.log(y(2,3))
 console.log(y(3,5))  //5, 8


function y(num1, num2){
    console.log(num1);   
    return num1+num2;
 }
 console.log(y(2,3))
 console.log(y(3,5))  //2, 5, 3, 8

 a = 15;
console.log(a);
function y(a){
   console.log(a);   
   return a;
}
b = y(10);
console.log(b);  //15, 10, 10

a = 15;
console.log(a);
function y(a){
   console.log(a);   
   return a*2;
}
b = y(10);
console.log(b);  //15, 10, 20

function multiply(x,y){
   console.log(x);
   console.log(y);
}
b = multiply(2,3);
console.log(b); //2,3

function multiply(x,y){
   return x*y;
}
b = multiply(2,3);
console.log(b);
console.log(multiply(5,2)); //6, 10

var x = [1,2,3,4,5,10];
for(var i=0; i<5; i++)
{
   i = i + 3; 
   console.log(i);  //3, 7
}

var x=15;
console.log(x);
function awesome(){
    var x=10;
    console.log(x);
}
console.log(x);
awesome();
console.log(x); //15, 15, 10, 15

for(var i=0; i<15; i+=2){
   console.log(i);
} //0, 2, 4, 6, 8, 10, 12, 14

for(var i=0; i<3; i++){
   for(var j=0; j<2; j++){      
       console.log(i*j);
   }
} //0,0,0,1,0,2

function looping(x,y){
   for(var i=0; i<x; i++){
      for(var j=0; j<y; j++){        
         console.log(i*j);
      } 
   }
   return x*y;
}
z = looping(3,5);
console.log(z); //