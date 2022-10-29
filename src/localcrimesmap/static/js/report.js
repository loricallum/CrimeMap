$(document).ready(function(){
    $("#crimetype-select").change(function() {
        var searchterm = $(this).val().toUpperCase();
        
        $("#crimesList div").each(function() {
            var currentText = $(this).text().toUpperCase();
            if (currentText.indexOf(searchterm) > -1) {
                $(this).show();
            }
            else{
                $(this).hide();
            }
          });
    });
});