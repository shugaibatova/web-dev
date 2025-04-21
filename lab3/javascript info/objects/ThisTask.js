function makeUser() {
    return {
      name: "John",
      ref() {
        return this;
      }
    };
  }
  
  let user = makeUser();
  
  alert( user.ref().name ); // John
/////////////////////////////////////////////////
let calculator = {
    // ... your code ...
    sum(){
        return this.a+this.b;
    },
    mul(){
      return this.a*this.b;
    },
    read(){
      let a=+prompt("a=",0);
      let b=+prompt("b=",0);
    }
  };
  
  calculator.read();
  alert( calculator.sum() );
  alert( calculator.mul() );
//  //////////////////////////////////////////////////////
let ladder = {
  step: 0,
  up() {
    this.step++;
    return this;
  },
  down() {
    this.step--;
    return this;
  },
  showStep: function() { // shows the current step
    alert( this.step );
    return this;
  }
};
ladder.up().up().down().showStep().down().showStep(); // shows 1 then 0