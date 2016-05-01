/// <reference path="../../../../typings/main.d.ts" />
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
    
    var validateForm = function(form){
        var errors = [];
        var valids = [];
        form.serializeArray().forEach(function(element) {
            
            if (element.name === 'email') {
                if(!validateEmail(element.value) || element.value.length < 1){
                    errors.push(element.name);
                }
                else {
                    valids.push(element.name);
                }
            }
            if(element.name === 'password') {
                if(!validatePassword(element.value)  || element.value.length < 1){
                    errors.push(element.name);
                }
                else {
                    valids.push(element.name);
                }
            }
            if (element.name === 'second_name') {
                valids.push(element.name);
            }
            else if (element.name === 'second_lastname') {
                valids.push(element.name);
            }
            else if (element.name !== 'csrf_token') {
                if (element.value.length < 1) {
                    errors.push(element.name);
                }
                else {
                    valids.push(element.name);
                }
            }
        });
        
        if (errors.length > 0) {
            errors.forEach(function(errorField){
                $("#"+ errorField).toggleClass('invalid', true);
            });
            return false;
        }
        if (valids.length > 0) {
            valids.forEach(function(validField){
                $("#"+ validField).toggleClass('invalid', false);
            });
        }
        return true
    }
    
    signupForm.on('submit', function(e) {
        e.preventDefault()
        var formData = $(this).serialize();
        var csrftoken = $('meta[name=csrf-token]').attr('content');
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken)
                }
            },
        });
        if (validateForm($(this))) {
            $.ajax({
                data: formData,
                url: '/auth/signup/',
                contentType:'application/x-www-form-urlencoded;charset=UTF-8',
                type: "POST",
                success: function(response) {
                    Materialize.toast("Signed Up Succesfully!\n Please Log in!", 4000);
                    setTimeout(function() {
                        window.location.assign(location.host+"/auth/login/");    
                    }, 100);
                },
                error: function(error) {
                    var errorObj = JSON.parse(error.responseText);
                    for (var key in errorObj) {
                        var errors = "";
                        if (errorObj.hasOwnProperty(key)) {
                            var element = errorObj[key];
                            element.forEach(function(err){
                                errors += err + "\n";
                            });
                            Materialize.toast("Found errors in: " + key.toUpperCase() + " Error: " +errors, 5000);
                        }
                    }
                    
                }
            });   
        }
        
    });
});