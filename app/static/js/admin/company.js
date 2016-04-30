/// <reference path="../../../../typings/main.d.ts" />
$(document).ready(function(){
    $("#newWrapper").hide();
    $("#editWrapper").hide();
    var newSub = $("#newSub");
    var editComp = $("#editForm");
    
    var showForm = function(wrapperName) {
        $("#"+ wrapperName).show();
    };
    
    
    // desktop and mobile versions
    var deskSub = $("#addSub");
    var deskEdit = $("#editComp");
    var mobileSub =$("#addSub-mobile");
    var mobileEdit = $("#editComp-mobile");
    
    // show forms
    deskSub.on('click', showForm("newWrapper"));
    deskEdit.on('click', showForm("editWrapper"));
    mobileSub.on('click', showForm("newWrapper"));
    mobileEdit.on('click', showForm("editWrapper"));
    
    var validateSub = function(data){
      // validate all the data from the form
      // return either true or false and an error array  
    };
    
    newSub.on('submit', function(e){
       var data = $(this).serializeArray();
       if (!validateSub) {
            e.preventDefault();
           // foreach error, toggle error class in form field
       } 
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
