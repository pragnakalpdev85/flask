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

let editPassMode = false

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
    emailV = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    //email validation
    if(r_email.value.trim() == ''){
        r_emailAlert.className = 'alert-show';
        flag = false;
    }else if(!emailV.test(r_email.value.trim())){
        r_emailAlert.innerHTML = "Invalid email"
        r_emailAlert.className = 'alert-show';
        flag = false;
    }else{
        r_emailAlert.innerHTML = "Email field is required"
        r_emailAlert.className = 'alert';
    }

    //password validation
    if(r_pass.value.trim() == ''){
        r_passAlert.className = 'alert-show';
        flag = false;
    }else if(r_pass.value.trim().length < 6){
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
    }else if(rc_pass.value.trim().length < 6){
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
        addressAlert.className = 'alert';
    }

    let arr = Array.from(hobbies);
    let isSelected = arr.some(cb => cb.checked);
    
    arr = Array.from(gender)
    let radioSelected = arr.some(r => r.checked);
    
    //hobbies validation
    if(!isSelected){
        hobbiesAlert.className = 'alert-show';
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
    emailV = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (email.value.trim() == ''){
        emailAlert.className = 'alert-show';
        flag = false
    }else if(!emailV.test(email.value.trim())){
        emailAlert.innerHTML = "Invalid email"
        emailAlert.className = 'alert-show';
        flag = false;
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

function onEditSubmit(){
    let e_f_name = document.getElementById('e_f_name');
    let e_l_name = document.getElementById('e_l_name');
    let e_address = document.getElementById('e_address');
    let e_gender = document.querySelectorAll('input[name="e_gender"]');
    let e_hobbies = document.querySelectorAll('input[name="e_option"]');

    let e_f_nameAlert = document.getElementById('e_f_name-alert');
    let e_l_nameAlert = document.getElementById('e_l_name-alert');
    let e_addressAlert = document.getElementById('e_address-alert');
    let e_hobbiesAlert = document.getElementById('e_hobbies-alert');
    let e_genderAlert = document.getElementById('e_gender-alert');
    
    flag = true
    if (editPassMode){
        flag = validateEditPass(flag)
    }

    // fisrt name validation
    if(e_f_name.value.trim() == ''){
        e_f_nameAlert.className = 'alert-show';
        flag = false;
    }else{
        e_f_nameAlert.className = 'alert';
    }

    // last name validation
    if(e_l_name.value.trim() == ''){
        e_l_nameAlert.className = 'alert-show';
        flag = false;
    }else{
        e_l_nameAlert.className = 'alert';
    }

    //address validation
    if(e_address.value.trim() == ''){
        e_addressAlert.className = 'alert-show';
        flag = false;
    }else if(e_address.value.split(/[, ;|]+/).length <= 15){
        e_addressAlert.innerHTML = 'Address must have more than 15 words';
        e_addressAlert.className = 'alert-show';
        flag = false;
    }else{
        e_addressAlert.innerHTML = 'Address Field is required';
        e_addressAlert.className = 'alert';
    }

    let arr = Array.from(e_hobbies);
    let isSelected = arr.some(cb => cb.checked);
    
    arr = Array.from(e_gender)
    let radioSelected = arr.some(r => r.checked);
    console.log(radioSelected)
    
    //hobbies validation
    if(!isSelected){
        e_hobbiesAlert.className = 'alert-show';
        flag = false
    }else{
        e_hobbiesAlert.className = 'alert';
    }

    //gender validation
    if(!radioSelected){
        e_genderAlert.className = 'alert-show';
        flag = false
    }else{
        e_genderAlert.className = 'alert';
    }

    return flag
}

function validateEditPass(flag){
    e_r_pass = document.getElementById('e_r_pass');
    e_rc_pass = document.getElementById('e_rc_pass');
    e_r_passAlert = document.getElementById('e_r_pass-alert');
    e_rc_passAlert = document.getElementById('e_rc_pass-alert')

    //password validation
    if(e_r_pass.value.trim() == ''){
        e_r_passAlert.className = 'alert-show';
        flag = false;
    }else if(e_r_pass.value.trim().length < 6){
        e_r_passAlert.innerHTML = "Password length should be greater than 6";
        e_r_passAlert.className = 'alert-show';
        flag = false
    }else{
        e_r_passAlert.innerHTML = "Password field is required"
        e_r_passAlert.className = 'alert';
    }

    if(e_rc_pass.value.trim() == ''){
        e_rc_passAlert.className = 'alert-show';
        flag = false;
    }else if(e_rc_pass.value.trim().length < 6){
        e_rc_passAlert.innerHTML = "Password length should be greater than 6";
        e_rc_passAlert.className = 'alert-show';
        flag = false
    }else if(e_rc_pass.value != e_r_pass.value){
        e_rc_passAlert.innerHTML = 'Passwords does not match'
        e_rc_passAlert.className = 'alert-show';
        flag = false
    }else{
        e_rc_passAlert.innerHTML = 'Password Confirmation field is required';
        e_rc_passAlert.className = 'alert';
    }

    return flag
}

function onChangeSelect(event){
    let passContainer = document.getElementById('change-pass');

    editPassMode = true

    let htmlPass = `
    <div class="input-containers">
        <label class="tag" for="passsword">Passsword</label>
        <input id="e_r_pass" type="password" name="password" placeholder="Password"
            value="">
        <div class="alert" id="e_r_pass-alert">Password field is required</div>
        <label class="tag" for="Confirm_passsword">Confirm passsword</label>
        <input id="e_rc_pass" type="password" name="Confirm_password" placeholder="Confirm password"
            value="">
        <div class="alert" id="e_rc_pass-alert">Password confirmation field is required</div>
    </div>`;

    passContainer.innerHTML = htmlPass;
}
