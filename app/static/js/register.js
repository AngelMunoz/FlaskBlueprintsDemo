/// <reference path="../../../typings/main.d.ts" />
$(document).ready(function() {
    
    var signupForm = $('#signupForm');
    
    var validateEmail = function(email) {
        var regex = /^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/;   
        return regex.test(email);
    }
    
    var validatePassword = function (password){
      var regex = /^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$/
      return regex.test(password);  
    }
    
    signupForm.on('submit', function(e) {
        var formData = $(this).serializeArray();
        //console.log(formData);
        if(!validateEmail(formData[1].value)){
            e.preventDefault()
            $('#email').toggleClass('invalid');
        }
        if(!validatePassword(formData[2].value)){
            e.preventDefault()
            $('#password').toggleClass('invalid');
        }
        if(!(formData[3].value === formData[2].value)){
            e.preventDefault()
            $('#password_repeat').toggleClass('invalid');
        }
        if(formData[4].value.length <= 0){
            e.preventDefault()
            $('#name').toggleClass('invalid');
        }
        if(formData[6].value.length <= 0){
            e.preventDefault()
            $('#lastname').toggleClass('invalid');
        }
        if(formData[8].value.length <= 0){
            e.preventDefault()
            $('#rfc').toggleClass('invalid');
        }
    });
});