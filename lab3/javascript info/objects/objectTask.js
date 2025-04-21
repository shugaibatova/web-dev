//<!-- Create an empty object .user -->
let user={};
//<!-- Add the property with the value .nameJohn -->
user.name="John";
//<!-- Add the property with the value .surnameSmith -->
user.name="Smith";
//<!-- Change the value of the to .namePete -->
user.name="Pete";
//<!-- Remove the property from the object.name -->
delete user.name;

//////////////////////////////////////////////////
function isEmpty(obj) {
    for (let key in obj) {
      return false;
    }
    return true;
  }
//////////////////////////////////////////////////
let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
  }
let sum=0;
for(key in salaries){
    
    sum+=salaries[key];
}
alert(sum);
//////////////////////////////////////////////
function multiplyNumeric(obj){
    for(let key in obj){
        if(typeof obj[key]=="number"){
            obj[key]*=2;
        }
    }
}
