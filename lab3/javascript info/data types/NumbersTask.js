let a=+prompt("a=",0);
let b=+prompt("b=",0);
alert(a+b);
/////////////////////////////////////
alert( 6.35.toFixed(20) ); // 6.34999999999999964473
alert( 1.35.toFixed(20) ); // 1.35000000000000008882
/////////////////////////////////
function readNumber(){
    let num;
    do{
        num=prompt("NUmber=",0);

    } while (!isFinite(num));
    if(num==null || num=='') return  null;
    return +num;
    
}
alert('Read ${readNumber()}');
////////////////////////////////////////////////
let i = 0;
while (i != 10) {
  i += 0.2;
} // like 0,1+0,2!=0.3  it will never equal to 10
////////////////////////////////////////////////////////
function random(min,max){
    return min + Math.random() * (max - min);

}
//////////////////////////////////////////////////////
function randomInteger(min, max) {
    // here rand is from min to (max+1)
    let rand = min + Math.random() * (max + 1 - min);
    return Math.floor(rand);
  }
alert( randomInteger(1, 3) );