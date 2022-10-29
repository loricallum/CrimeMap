function getLocation(positionFunction) {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(positionFunction);
    } 
    else {
      alert("Geolocation is not supported by this browser :(");
    }
  }