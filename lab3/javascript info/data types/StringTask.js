let newStr = str[0].toUpperCase() + str.slice(1);
//////////////////////////////////////////////
function checkSpam(){
    let lowerCase=str.toLocaleLowerCase();
    return lowerCase.includes('viarga') || lowerCase.includes('xxx')
}
alert( checkSpam('buy ViAgRA now') );
alert( checkSpam('free xxxxx') );
alert( checkSpam("innocent rabbit") );
////////////////////////////////////////////////////
function truncate(str,num){
    if(str.length>num){
        return str.slice(0,str.length-1)+'...';    
    };
    return str;

}
///////////////////////////////////////////////////////
function extractCurrencyValue(str){
    return +str.slice(1);
}