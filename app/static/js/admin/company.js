/// <reference path="../../../../typings/main.d.ts" />
$(document).ready(function () {
    $('.modal-trigger').leanModal();

    var editForm = $("#editform");

    editForm.on('submit', function (e) {
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

        if ($(this).serializeArray()[1].value < 1) {
            $("#" + $(this).serializeArray()[1].name).toggleClass('invalid', true);
        }
        else {
            $.ajax({
                data: formData,
                url: '/admin/company/',
                contentType: 'application/x-www-form-urlencoded;charset=UTF-8',
                type: "PUT",
                success: function (response) {
                    Materialize.toast("Name Changed Succesfully", 4000);
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
