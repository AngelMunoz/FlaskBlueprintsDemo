/// <reference path="../../../../typings/main.d.ts" />
$(document).ready(function(){
    $("#newSub").hide();
    $("#editForm").hide();
    var newSub = $("#newSub");
    var editComp = $("#editForm");
    
    
    // desktop and mobile versions
    var deskSub = $("#addSub");
    var deskEdit = $("#editComp");
    var mobileSub =$("#addSub-mobile");
    var mobileEdit = $("#editComp-mobile");
    
    // show forms
    deskSub.on('click', function(){
        $("#newSub").show();
    });
    deskEdit.on('click', function(){
        $("#editForm").show();
    });
    mobileSub.on('click', function(){
        $("#newSub").show();
    });
    mobileEdit.on('click', function(){
        $("#editForm").show();
    });
    
    var validateSub = function(data){
      // validate all the data from the form
      // return either true or false and an error array  
    };
    
    newSub.on('submit', function(e){
        e.preventDefault();
        var newSubData = $(this).serialize();
        var csrftoken = $('meta[name=csrf-token]').attr('content');
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken)
                }
            },
        });
        $.ajax({
                //more changes here
                data: newSubData,
                url: '/admin/company/',
                contentType:'application/x-www-form-urlencoded;charset=UTF-8',
                type: "POST",
                success: function(response) {
                    console.log(response);
                },
                error: function(error) {
                    console.error(error);
                    console.error(error.responseText);
                }
            });
       
    });
    
    var validateEdit = function(data){
      // validate all the data from the form
      // return either true or false and an error array  
    };
    
    editComp.on('submit', function(e){
       var data = $(this).serializeArray();
       if (!validateEdit) {
           e.preventDefault();
           // foreach error, toggle error class in form field
       }
    });
    
});
