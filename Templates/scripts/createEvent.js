$(document).ready(function() {
    $('.add-item').click(function(ev) {
        ev.preventDefault();
        var count = $('#items-form-container').children().length;
        var tmplMarkup = $('#item-template').html();
        var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);

        $('div#items-form-container').append(compiledTmpl);
        $('div#items-form-container [id^=item-]').addClass("itemTable");

        // update form count
        $('#id_item-TOTAL_FORMS').attr('value', count+1);
        addItemBootStrap();
    });
});

$(document).ready(function() {
    $('.add-invitee').click(function(ev) {
        ev.preventDefault();
        var count = $('#invitees-form-container').children().length;
        var tmplMarkup = $('#invitee-template').html();
        var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);

        $('div#invitees-form-container').append(compiledTmpl);
        $('div#invitees-form-container [id^=invitee-]').addClass("inviteTable");

        // update form count
        $('#id_invitee-TOTAL_FORMS').attr('value', count+1);
        addValidationRules();
        addEmailBootStrap();
    });
});



$(document).ready(function (){
    $( "#submitButton" ).prop( "disabled", true );
    highLightBox();
    addEmailBootStrap();
    addItemBootStrap();

    constantErrorChecking();

});

$(document).ready(function() {

     var validator = $("#SigningUp").validate({
      onkeyup: function (element, event) {
            if (event.which === 9 && this.elementValue(element) === "") {
                return;
            } else {
                this.element(element);
            }
      },
      rules: {
        name: {
            required: true,
            minlength: 6
        },

        location : {
             required: true,
             minlength: 3
        },
        date : {
            required: true,
            date: true
        },
        time :{
            required : true,
            timeAMPM : true
        },
      },
      messages: {
          name:{
              required : "Name field is required",
              minlength : "Name has to be at least 6 characters"
          },
          location: {
              required : "Location field is required",
              minlength : "Location has to be at least 3 characters"
          },
          time: {
              timeAMPM : "Please enter a valid time"
          },

      }
    });
    addValidationRules();
});

/* This adds a validator to all email classes */
function addValidationRules(){
     $('[name$="-email"]').each(function() {
         $(this).rules('add', {
             EmailWithDot: true
         });
     });
}

/************** Custom validators *******************/

jQuery.validator.addMethod("EmailWithDot", function(value, element) {
    return this.optional( element ) || ( /^[A-Za-z0-9]+([-._][a-z0-9]+)*@([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{1,4}$/
        .test( value ) && /^(?=.{1,64}@.{3,64}$)(?=.{6,100}$).*/.test( value ) );
}, 'Not a valid email address.');

jQuery.validator.addMethod("timeAMPM", function(value, element) {
    return this.optional( element ) || ( /^[01]?[0-9]:[0-6]{2}[a,p]m$/.test( value ) );
}, 'Please enter a valid time');


/************** Tab Functions *******************/
$(function () {
      $('#myTab a:last').tab('show')
  })

$('.btnNext').click(function(){
    $('.nav-tabs > .active').next('li').find('a').trigger('click');

});
$('.btnPrevious').click(function(){
    $('.nav-tabs > .active').prev('li').find('a').trigger('click');

});
/**********************************************/

// Mark Event Info as Boostrap forms
$("#EventInfo :text, textarea" ).each(function( index ) {
    $(this).addClass("form-control");
});

function addEmailBootStrap(){
    $('[id$="email"]').each(function(index) {
        $(this).addClass("form-control");
    });

    $('.inviteTable').each(function(){
       $(this).addClass('form-inline');
    });
}

function addItemBootStrap(){
    $('[id$="itemName"]').each(function(index) {
        $(this).addClass("form-control");
    });

    $('[id$="amount"]').each(function(index) {
        $(this).addClass("form-control itemAmountInput");
    });
    $('.itemTable ').each(function(){
       $(this).addClass('form-inline');
    });
}

function constantErrorChecking(){
    $('input[type="text"], #id_description').on('input change', function () { //'input change keyup paste'
        submitOnlyWhenValid();
        //checkAndMarkActiveTyping(this);


    });
    checkAndMarkBlur();
}

/* This highlights al the boxes that has an error */
function checkAndMarkActiveTyping(field){
        if ( $(field).attr('aria-invalid') != 'false')
            addError(field);
        else
            removeError(field);
}

function checkAndMarkBlur(){
    $('input[type="text"], #id_description').blur(function(){
         if ( $(this).attr('aria-invalid') != 'false'){
             addError(this);
         } else {
             removeError(this);
         }
     });
}

function highLightBox(){
    $('.errorlist').parent().each(function(){
        addError(this);
     });
}

function addError(field){
    //$(field).addClass('form-control')
    $(field).parent().addClass('has-error')
}

function removeError(field){
    $(field).parent().removeClass('has-error')
}

function submitOnlyWhenValid(){
    if ($('#SigningUp').valid()) {
        $( "#submitButton" ).prop( "disabled", false );
    } else {
        $( "#submitButton" ).prop( "disabled", true );
    }
}