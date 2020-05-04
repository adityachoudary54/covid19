console.log('Welcome to trends');
let country=document.querySelector('#country');
let type=document.querySelector('#type');
let graph=document.querySelector('.graph');
let form=document.querySelector('form');
// country.options[0].selected=true;
// type.options[0].selected=true;
// form.submit();
// console.log(country.value,type.value);
country.addEventListener('click',function(e) {
    console.log(country.value,type.value);
    if(country.value.length!=0&&type.value.length!=0){
        form.submit();
    }
    
});
type.addEventListener('click',function(e) {
    console.log(country.value,type.value);  
    if(country.value.length!=0&&type.value.length!=0){
        form.submit();
    }    
});

// console.log(country.value,type.value);