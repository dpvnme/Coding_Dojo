function a(){
    return 35;
} 
console.log(a()) //35


function a(){
    return 4;
} 
console.log(a()+a()); //8


function a(b){
    return b;
}
console.log(a(2)+a(4)); //6


function a(b){
    console.log(b);
    return b*3;
}
console.log(a(3)); //3, 9


function a(b){
   return b*4;
   console.log(b);
}
console.log(a(10)); //10


function a(b){
    if(b<10) {
        return 2;
    }
    else     {
        return 4;
    }
    console.log(b);
}
console.log(a(15)); //


function a(b,c){
    return b*c;
}
console.log(10,3);
console.log( a(3,10) ); //10,3,30


function a(b){
    for(var i=0; i<10; i++){
        console.log(i);
    }
    return i;
}
console.log(3); 
console.log(4); //3,4


function a(){
    for(var i=0; i<10; i++){
        i = i +2;
        console.log(i);
    }
}
a(); //2,5,8, 11


function a(b,c){
    for(var i=b; i<c; i++) {
       console.log(i);
   }
   return b*c;
}
a(0,10);
console.log(a(0,10)); //


function a(){
    for(var i=0; i<10; i++){
       for(var j=0; j<10; j++){
           console.log(j);
       }
       console.log(i);
    }
} //nothing prints out


function a(){
    for(var i=0; i<10; i++){
        for(var j=0; j<10; j++){
            console.log(i,j);
        }
        console.log(j,i);
    }
}//no output


var z = 10; 
function a(){
    var z = 15;
    console.log(z);
}
console.log(z); //10


var z = 10;
function a(){
    var z = 15;
    console.log(z);
}
a();
console.log(z); //15, 10


var z = 10;
function a(){
    var z = 15;
    console.log(z);
    return z;
}
z = a();
console.log(z); //15, 15

//Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.
var arr = [];
function returnArray(){
    for(var i=1; i<256; i++){
        arr[i-1]=i;
    }
    console.log(arr);
}
returnArray();

//Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.
var sum = 0;
function sumOfEvenNum(){
    for(var i=1; i<1001; i++){
        if(i%2){
            sum=sum+i;
        }
    }
    return sum;
}
console.log(sumOfEvenNum());

//Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999).
var sum = 0;
function sumOfOddNum(){
    for(var i=1; i<5001; i++){
        if(i%2!==0){
            sum=sum+i;
        }
    }
    return sum;
}
console.log(sumOfOddNum());

//Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).
var arr=[];
var sum=0;
function sumOfArray(arr){

    for(var i=0; i<arr.length; i++){
        sum+=arr[i};
    }
}   return sum;

console.log(sumOfArray[]);

//Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for 
var arr=[];
var max=0;
function findMax(arr){
    for(var i=0; 1<arr.length; i++){
        if(arr[i]>max){
            max=arr[i];
        }
    }return max;
}
console.log(findMax([1,54,5,3,2,1,7,7,5,5]));

//Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)
var arr=[];
var sum=0
var ave=0;
function findAverage(arr){
    for(var i=0; i<arr.length; i++){
        sum+=arr[i];
    }
    ave = sum / arr.length;
    return ave;
}
console.log(findAverage([1,2,3,4,5]));

//Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.
var arr=[];
function arrayOdd(){
    for(var i=0; i<51; i++){
        if(i%2!==0){
            arr.push(i);
        }
    }
    return arr;
}
console.log(arrayOdd());

//Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).
var y=0;
var arr=[];
var count=0;
function greaterThanY(arr,y){
    for(var i=0; i<arr.length; i++){
        if(arr[i]>y){
            count++;
        }
    }return count;    
}
console.log(greaterThanY([1,2,3,4,5,6,7,8,9], 5));

//Squares - Given an array with multiple values, write a function that replaces each value in the array with the value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])
var arr=[];
function square(arr){
    for(var i=0; i<arr.length; i++){
        arr[i]=arr[i]*arr[i];
    }
    return arr;    
}
console.log(square([1,2,3,4,5]));

//Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])
var arr=[];
function negative(arr){
    for(var i=0; i<arr.length; i++){
        if(arr[i]<0){
            arr[i]=0;
        }
    }return arr;
}    
console.log(negative([1,2,-3,4,5]));

//Max/Min/Avg - Given an array with multiple values, write a function that returns a new array that only contains the maximum, minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])
var arr=[];

function minMaxAve(arr){
var sum=0;
var avg=0;
var min=arr[0];
var max=arr[0];
    for(var i=0; i<arr.length; i++){
        if(arr[i]>max){
            max=arr[i];
        }
        if(arr[i]<min){
            min=arr[i]; 
        }
        sum += arr[i]; 
    }
    ave = sum / arr.length;
    console.log("min is: " +min);
    console.log("max is: " +max);
    console.log("ave is: " +ave);
}
console.log(minMaxAve([1,2,3,4,5]));

//Swap Values - Write a function that will swap the first and last values of any given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1]).
var arr=[];
function swapFirstLast(arr){
    var temp=arr[0];
    arr[0]=arr[arr.length-1];
    arr[arr.length-1]=temp;
    return arr;
}
console.log(swapFirstLast([1,2,3,4,5]));

//Number to String - Write a function that takes an array of numbers and replaces any negative values within the array with the string 'Dojo'. For example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].
var arr=[];
function numToString(arr){
    for(var i=0; i<arr.length; i++){
        if(arr[i]<0){
            arr[i]="Dojo";
        }  
    }
    return arr;
}
console.log(numToString([-1,2,5,-3,23]));

//Count Positives - Given an array of numbers, create a function to replace the last value with the number of positive values found in the array.  Example, countPositives([-1,1,1,1]) changes the original array to [-1,1,1,3] and returns it.
var arr=[];
function countPositive(arr){
    var count=0;
    for(var i=0; i<arr.length; i++){
        if(arr[i]>0){
            count++;
        }
    }
    arr[arr.length-1]=count;
    return arr;
}
console.log(countPositive([-1,-2,3,4,5]));

//Evens and Odds - Create a function that accepts an array.  Every time that array has three odd values in a row, print "That's odd!".  Every time the array has three evens in a row, print "Even more so!".
function evenAndOdd(arr){
    for(var i=0; i<arr.length-2; i++){
        if(arr[i]%2===0 && arr[i+1]%2===0 && arr[i+2]%2===0){
            console.log("Even more so!");
        }
        else if(arr[i]%2===1 && arr[i+1]%21===1 && arr[i+2]%2===1){
            console.log("That's odd!");
        }    
    }
}
evenAndOdd([2,2,1,2,2,2,1,1,1,1,1]);

//Increment the Seconds - Given an array of numbers arr, add 1 to every other element, specifically those whose index is odd (arr[1], arr[3], arr[5], etc).  Afterward, console.log each array value and return arr.
function incrementTheSeconds(arr){
    for(var i=1; i<arr.length; i+2){
        arr[i]+=1;
        console.log(arr[i-1]);
        console.log(arr[i]);
    }
}
incrementTheSeconds([1,2,3,4,5,6,7]);
