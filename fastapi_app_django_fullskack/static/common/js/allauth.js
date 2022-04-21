document.addEventListener('DOMContentLoaded', function(){
    let elements = document.querySelectorAll("input[type='text'], input[type='password'], input[type='email']");
    // console.log(elements);
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.add("uk-input",);
    }    
    let checkbox_elements = document.querySelectorAll("input[type='checkbox']");
    // console.log(elements);
    for (var i = 0; i < checkbox_elements.length; i++) {
        checkbox_elements[i].classList.add("uk-checkbox",);
    }    
});
