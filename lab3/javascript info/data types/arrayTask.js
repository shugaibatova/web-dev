let fruits = ["Apples", "Pear", "Orange"];

// push a new value into the "copy"
let shoppingCart = fruits;
shoppingCart.push("Banana");

// what's in fruits?
alert( fruits.length ); // 4
///////////////////////////////////////////////
let music=["Jazz","Blues"];
music.push("Pock-n-Roll");
styles[Math.floor((styles.length - 1) / 2)] = "Classics";
music.shift();
music.unshift("Rap","Reggae");
////////////////////////////////////////////////
let arr = ["a", "b"];

arr.push(function() {
  alert( this );
});

arr[2](); // a, b, function
/////////////////////////////////////////////////
function sumInput() {

    let numbers = [];
  
    while (true) {
      let value = prompt("A number please?", 0);
      if (value === "" || value === null ) break;
      numbers.push(+value);
    }
  
    let sum = 0;
    for (let number of numbers) {
      sum += number;
    }
    return sum;
  }
  
  alert( sumInput() );
///////////////////////////////////////////////////
function getMaxSubMax(arr){
    let sum=0;
    for (let i = 0; i < arr.length; i++) {
        let sumFixedStart = 0;
        for (let j = i; j < arr.length; j++) {
            sumFixedStart += arr[j];
            maxSum = Math.max(maxSum, sumFixedStart);
    }
  } return maxSum;

}