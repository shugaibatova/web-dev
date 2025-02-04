describe("Raises x to the power n", function(){
    it("5 in the power of 1 equals 5", function(){
        alert.equal(pow(5,1),5);
    });
    it("5 in the power 2 is 25",function(){
        alert.equal(pow(5,2),25);
    });
    it("5 in the power 3 is 125",function(){
        alert.equal(pow(5,3),125);
    });
});

//   // Mocha will run only this block
//   it.only("5 in the power of 2 equals 25", function() {
//     assert.equal(pow(5, 2), 25);
//   });