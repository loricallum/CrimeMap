// This script relies on the getlocation.js script already being loaded into the DOM for the getcurrentlocation functionality.

var mapModule = (function() {
  var _markersIdSet = new Set();
  var _crimeMarkersLayer;
  var _map;

  function initMap(map, options) {
    // get point lat and lon
    let lon = "53.400002";
    let lat = "-2.983333";
    // zoom to point & add it to map
    map.preferCanvas = true;
    map.zoomControl = false;
    map.setView([lon, lat], 16);
    _crimeMarkersLayer = L.layerGroup().addTo(map);
    map.on('moveend', LoadCrimes);
    getLocation(showPosition)
    L.easyButton('fa-crosshairs fa-lg', function(btn, map){
      getLocation(showPosition)
    }).addTo(map);
    _map = map;
  }

  function showPosition(position) {
    let currentLat = position.coords.latitude;
    let currentLng = position.coords.longitude; 
    _map.setView([currentLat, currentLng], 16);
  }

  function RefreshAndLoadCrimes(){
    _crimeMarkersLayer.clearLayers(); 
    _markersIdSet.clear();
    LoadCrimes();
  }
  function LoadCrimes() {
    var selectedDate = $('#dateSelect').val(); 
    var bounds = _map.getBounds();
    var boundsArray = [bounds.getNorthWest(), bounds.getNorthEast(), bounds.getSouthEast(), bounds.getSouthWest()]
    var boundsText = "";

    for(let i = 0; i < boundsArray.length; i++){
      boundsText += boundsArray[i].lat + "," + boundsArray[i].lng; 
      if (i != boundsArray.length - 1){
        boundsText += ":"
      }
    }

      $.ajax({
        url: '/api/allcrimesinarea',
        type: "get",
        data: {
          'area': boundsText,
          'date': selectedDate
        },
        dataType: 'json',
        success: function (data) {
          {
            data.forEach(function(key, index){

              if (!_markersIdSet.has(key.id)){
                var lat = key.location.latitude
                var lng = key.location.longitude
                var category = key.category
                var locInfo = key.location.street.name
                var outcome = "No recorded outcome"
                if (key.outcome_status && key.outcome_status.category){
                  outcome = key.outcome_status.category
                }
  
                var crimeMarker = L.circleMarker([lat,lng], { color: '#3388ff'}).addTo(_crimeMarkersLayer);
                _markersIdSet.add(key.id);
                crimeMarker.bindPopup("<b>" + category + "</b>" + "<br>" + locInfo + "</br>" + "<br>" + outcome + "</br>")
              }
            });
          }
        }
      });
    }
    return {
      initMap: initMap,
      loadCrimes: LoadCrimes,
      refreshAndLoadCrimes: RefreshAndLoadCrimes
    };
}());