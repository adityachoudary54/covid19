console.log('Welcome to topNcountries');
let count=document.querySelector('#count');
let type=document.querySelector('#type');
let graph=document.querySelector('.graph');
let form=document.querySelector('form');
// country.options[0].selected=true;
// type.options[0].selected=true;
// form.submit();
// console.log(country.value,type.value);
count.addEventListener('click',function(e) {
    console.log(country.value,type.value);
    if(count.value.length!=0&&type.value.length!=0){
        form.submit();
    }
    
});
type.addEventListener('click',function(e) {
    console.log(count.value,type.value);  
    if(count.value.length!=0&&type.value.length!=0){
        form.submit();
    }    
});

// console.log(count.value,type.value);