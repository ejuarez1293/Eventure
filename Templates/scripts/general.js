$(document).ready(function(){
    var date_input=$('input[name="date"]'); //our date input has the name "date"
    var container=$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
    var optionsDate={
        format: 'mm/dd/yyyy',
        container: container,
        todayHighlight: true,
        autoclose: true,
        startDate: '+0d',
    };
    date_input.datepicker(optionsDate);

    var time_input=$('input[name="time"]');
    var optionsTime={

    };
    time_input.timepicker(optionsTime);
})