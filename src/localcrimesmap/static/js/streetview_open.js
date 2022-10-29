// this script relies on bootbox being loaded as a static file already in the DOM

var openStreetViewModule = (function(){

    function OpenStreetView(location){
        bootbox.confirm("Open crime location in Google StreetView?", function(result){
            if (result){
                let streetViewURL = "https://www.google.com/maps/@?api=1&map_action=pano&viewpoint="+location;
                window.open(streetViewURL);
            }
        });
    }

    return {
        OpenStreetView: OpenStreetView,
      };
  }());