// This script relies on the getlocation.js script already being loaded into the DOM for the getcurrentlocation functionality.

var crimeSummaryModule = (function() {
    let _latControl;
    let _lngControl;

    function Initialize(latControl,lngControl){
        _latControl = latControl;
        _lngControl = lngControl;
        getLocation(showPosition)
    }
    
    function showPosition(position) {
        if (_latControl.value.length==0){
            let currentLat = position.coords.latitude.toFixed(5);
            _latControl.value = currentLat;
        }
        
        if (_lngControl.value.length==0){
            let currentLng = position.coords.longitude.toFixed(5);
            _lngControl.value = currentLng; 
        }
  } 
    return {
        initialize: Initialize,
      };
  }());

  $(document).ready(function() {
      let latControl = document.getElementById('summaryform_lat');
      let lngControl = document.getElementById('summaryform_lng');
      crimeSummaryModule.initialize(latControl, lngControl)
})