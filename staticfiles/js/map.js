let map, autocomplete, selectedPlace, currentLocationMarker;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 22.1261475, lng: 105.8329401 },
        zoom: 11
    });

    autocomplete = new google.maps.places.Autocomplete(document.getElementById('autocomplete'));
    autocomplete.addListener('place_changed', onPlaceChanged);

    // Add click event to the map
    map.addListener('click', function(event) {
        const latitude = event.latLng.lat();
        const longitude = event.latLng.lng();
    
        // Fill the form with coordinates
        document.getElementById('latitude').value = latitude;
        document.getElementById('longitude').value = longitude;

        // Remove previous marker if exists
        if (currentLocationMarker) {
            currentLocationMarker.setMap(null);
        }
        // Create a new marker at the clicked location
        currentLocationMarker = new google.maps.Marker({
            position: event.latLng,
            map: map,
            title: 'Selected Location'
        });
    });
}

function onPlaceChanged() {
    selectedPlace = autocomplete.getPlace();
    if (selectedPlace.geometry) {
        map.setCenter(selectedPlace.geometry.location);
        map.setZoom(12);
        if (currentLocationMarker) currentLocationMarker.setMap(null);
        currentLocationMarker = new google.maps.Marker({
            position: selectedPlace.geometry.location,
            map: map
        });
    } else {
        alert('Please select a place from the dropdown.');
    }
}

function getCurrentLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
            const lat = position.coords.latitude;
            const lng = position.coords.longitude;
            map.setCenter({ lat, lng });
            map.setZoom(12);
            if (currentLocationMarker) currentLocationMarker.setMap(null);
            currentLocationMarker = new google.maps.Marker({
                position: { lat, lng },
                map: map,
                title: 'You are here'
            });
        });
    } else {
        alert('Geolocation is not supported by this browser.');
    }
}

function showReportOptions() {
    document.getElementById('report-options').style.display = 'block';
    document.getElementById('report-form').style.display = 'none';
}

function showForm(reportType) {
    document.getElementById('report-options').style.display = 'none';
    document.getElementById('report-form').style.display = 'block';
    document.getElementById('report-type').value = reportType;
    document.getElementById('form-title').innerText = `Report ${reportType.charAt(0).toUpperCase() + reportType.slice(1)} Location`;
}


window.onload = initMap;