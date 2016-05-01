/// <reference path="../../../../typings/main.d.ts" />
$(document).ready(function(){
    var loginForm = $('#loginForm');
    
    var validateEmail = function(email) {
        var regex = /^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/;   
        return regex.test(email);
    }
    var validateForm = function(form){
        var errors = [];
        var valids = [];
        form.serializeArray().forEach(function(element) {
            if (element.value.length < 1) {
                errors.push(element.name);
            }
            else {
                valids.push(element.name);
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
    loginForm.on('submit', function(e) {
        e.preventDefault();
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
                url: '/auth/login/',
                contentType:'application/x-www-form-urlencoded;charset=UTF-8',
                type: "POST",
                success: function(response) {
                    Materialize.toast("Welcome!", 4000);
                    setTimeout(function(){
                        window.location.reload();
                    },750); 
                },
                error: function(error) {
                    var errorObj = JSON.parse(error.responseText);
                    if(error.status === 400)
                    {
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
                    else if (error.status === 404 || error.status === 409)
                    {
                        for (var key in errorObj) {
                            if (errorObj.hasOwnProperty(key)) {
                                Materialize.toast("Found: " + key.toUpperCase() + " " + errorObj[key] , 5000);
                            }
                        }
                    }
                    
                }
            });
        }
    });
});