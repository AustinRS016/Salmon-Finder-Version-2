## 'Facility' Field from hatcheryLocations will be used as key to retrieve data


## 'river_guage' Field is to retrieve USGS river data
Example call that retrieves an image
ex: "http://waterdata.usgs.gov/nwisweb/graph?agency_cd=USGS&site_no="  + e.features[0].properties.river_gauge + "&parm_cd=00060&period=7&cacheTime=" + cacheDtTm;


## 'hatchLat' and 'hatchLon' are used to retrieve weather data
"https://api.openweathermap.org/data/2.5/onecall?lat="+ hatchLat +"&lon="+ hatchLon +"&exclude=hourly,minutely&units=imperial&appid=c6e7120c57d9cf83d3bdb078b1beb1f1"
