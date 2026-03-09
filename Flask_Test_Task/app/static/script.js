//login credential inputs
let email = document.getElementById('email-input');
let pass = document.getElementById('password-input');

//validation message fields for login
let emailAlert = document.getElementById('email-alert');
let passAlert = document.getElementById('pass-alert');

//registration fields
let f_name = document.getElementById('f_name');
let l_name = document.getElementById('l_name');
let r_email = document.getElementById('r_email');
let r_pass = document.getElementById('r_pass');
let rc_pass = document.getElementById('rc_pass');
let address = document.getElementById('address');
let hobbies = document.querySelectorAll('input[name="option"]');
let gender = document.querySelectorAll('input[name="gender"]');

//registration validation message fields
let f_nameAlert = document.getElementById('f_name-alert');
let l_nameAlert = document.getElementById('l_name-alert');
let r_emailAlert = document.getElementById('r_email-alert');
let r_passAlert = document.getElementById('r_pass-alert');
let rc_passAlert = document.getElementById('rc_pass-alert');
let addressAlert = document.getElementById('address-alert');
let hobbiesAlert = document.getElementById('hobbies-alert');
let genderAlert = document.getElementById('gender-alert');

function onRegister(){
    let flag = true

    //fisrt name validation
    if(f_name.value.trim() == ''){
        f_nameAlert.className = 'alert-show';
        flag = false;
    }else{
        f_nameAlert.className = 'alert';
    }

    //last name validation
    if(l_name.value.trim() == ''){
        l_nameAlert.className = 'alert-show';
        flag = false;
    }else{
        l_nameAlert.className = 'alert';
    }

    //email validation
    if(r_email.value.trim() == ''){
        r_emailAlert.className = 'alert-show';
        flag = false;
    }else{
        r_emailAlert.className = 'alert';
    }

    //password validation
    if(r_pass.value.trim() == ''){
        r_passAlert.className = 'alert-show';
        flag = false;
    }else if(r_pass.value.length < 6){
        r_passAlert.innerHTML = "Password length should be greater than 6";
        r_passAlert.className = 'alert-show';
        flag = false
    }else{
        r_passAlert.innerHTML = "Password field is required"
        r_passAlert.className = 'alert';
    }

    if(rc_pass.value.trim() == ''){
        rc_passAlert.className = 'alert-show';
        flag = false;
    }else if(rc_pass.value.length < 6){
        rc_passAlert.innerHTML = "Password length should be greater than 6";
        rc_passAlert.className = 'alert-show';
        flag = false
    }else if(rc_pass.value != r_pass.value){
        rc_passAlert.innerHTML = 'Passwords does not match'
        rc_passAlert.className = 'alert-show';
        flag = false
    }else{
        rc_passAlert.innerHTML = 'Password Confirmation field is required';
        rc_passAlert.className = 'alert';
    }

    //address validation
    if(address.value.trim() == ''){
        addressAlert.className = 'alert-show';
        flag = false;
    }else if(address.value.split(/[, ;|]+/).length <= 15){
        addressAlert.innerHTML = 'Address must have more than 15 words';
        addressAlert.className = 'alert-show';
        flag = false;
    }else{
        addressAlert.innerHTML = 'Address Field is required';
    }

    let arr = Array.from(hobbies);
    let isSelected = arr.some(cb => cb.checked);
    
    arr = Array.from(gender)
    let radioSelected = arr.some(r => r.checked);
    
    //hobbies validation
    hobbiesAlert.className = 'alert-show';
    if(!isSelected){
        flag = false
    }else{
        hobbiesAlert.className = 'alert';
    }

    //gender validation
    if(!radioSelected){
        genderAlert.className = 'alert-show';
        flag = false
    }else{
        genderAlert.className = 'alert';
    }


    return flag
}

function onSubmit(){

    let flag = true

    //email validation
    if (email.value.trim() == ''){
        emailAlert.className = 'alert-show';
        flag = false
    }else{
        emailAlert.className = 'alert';
    }

    //password validation
    if (pass.value.trim() == ''){
        passAlert.className = 'alert-show';
        flag = false
    }else if(pass.value.length < 6){
        passAlert.innerHTML = "Password length should be greater than 6";
        passAlert.className = 'alert-show';
        flag = false
    }else{
        passAlert.innerHTML = 'Passsword field is required';
        passAlert.className = 'alert';
    }
    
    return flag 
}
