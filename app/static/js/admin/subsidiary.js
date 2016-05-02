/// <reference path="../../../../typings/main.d.ts" />
$(document).ready(function () {
    $('.modal-trigger').leanModal();

    var newSub = $("#newSub");

    var validateForm = function(form){
        var errors = [];
        var valids = [];
        form.serializeArray().forEach(function(element) {
            
            if (element.name !== 'csrf_token') {
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
    };
    
    newSub.on('submit', function (e) {
        e.preventDefault();
        var formData = $(this).serialize();
        var csrftoken = $('meta[name=csrf-token]').attr('content');
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken)
                }
            },
        });

        if (validateForm($(this))) {
            $.ajax({
                data: formData,
                url: '/admin/subsidiaries/',
                contentType: 'application/x-www-form-urlencoded;charset=UTF-8',
                type: "POST",
                success: function (response) {
                    Materialize.toast("Subsidiary successfully added", 4000);
                    setTimeout(function () {
                        window.location.reload();
                    }, 750);
                },
                error: function (error) {
                    var errorObj = JSON.parse(error.responseText);
                    if (error.status === 400) {
                        for (var key in errorObj) {
                            var errors = "";
                            if (errorObj.hasOwnProperty(key)) {
                                var element = errorObj[key];
                                element.forEach(function (err) {
                                    errors += err + "\n";
                                });
                                Materialize.toast("Found errors in: " + key.toUpperCase() + " Error: " + errors, 5000);
                            }
                        }
                    }
                    else if (error.status === 404 || error.status === 409) {
                        for (var key in errorObj) {
                            if (errorObj.hasOwnProperty(key)) {
                                Materialize.toast("Found: " + key.toUpperCase() + " " + errorObj[key], 5000);
                            }
                        }
                    }

                }
            });
        }
    });
});
