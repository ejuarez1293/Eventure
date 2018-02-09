$(document).ready(function() {
    $('.add-item').click(function(ev) {
        ev.preventDefault();
        var count = $('#items-form-container').children().length;
        var tmplMarkup = $('#item-template').html();
        var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);

        $('tbody#items-form-container').append(compiledTmpl);
        $('tbody#items-form-container [id^=item-]').addClass("itemTable");


        // update form count
        $('#id_item-TOTAL_FORMS').attr('value', count+1);
        addItemBootStrap(); // Add BS to new forms
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

        console.log(compiledTmpl);

        // update form count
        $('#id_invitee-TOTAL_FORMS').attr('value', count+1);
        addEmailBootStrap();
    });
});

var itemTable = $('.itemTable');

// Delete button
itemTable.on("click", "a.deleteElement", function(ev) {
    ev.preventDefault();
    $(this).parent().parent().children("td").children().hide();

});

// Undo button
itemTable.on("click", "a.redoElement", function(ev) {
    ev.preventDefault();

    $(this).parent().parent().children("td").children().show();

});

// Toggle Delete/Undo button
itemTable.on("click", "a.modifyItemList", function(ev) {
    $(this).parent().children().toggle();
});


// Start up
$(document).ready(function (){
    addEmailBootStrap();
    addItemBootStrap();
    addItemTableBootStrap();
});

// Submit function
$('#edit').submit(function(event) {

 event.preventDefault(); //this will prevent the default submit
 removeHiddenElements();

 $(this).unbind('submit').submit(); // continue the submit unbind preventDefault
});

// Set up for deletion
function removeHiddenElements() {
    $('.tableItemName').each(function (index) {
        if( $(this).children().is(":hidden") )
            $(this).parent().children('.tableItemAmount').children().val(0);


    });


}

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


function addItemTableBootStrap(){
    $('td input[id$="name"]').each(function(index) {
        $(this).addClass("form-control");
    });

}


