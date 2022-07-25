# Salmon-Finder-Version-2
2nd iteration of Master's capstone project, post graduation. Implementing React.js and Material UI for ease of development and cleaner user interface.

Version 1: https://austinrs016.github.io/mapHatcheries/

Feedback from version 1:
  - Black dots on map representing hatchery have 'no meaning'
  - Line graph is hard to interpret
  - No y axis for density plot
  - Hard to click on hatcheries on map
  - Needs to be more user friendly and polished

Goals:
  - Make the application more user friendly
  - Develop for mobile
  - Add recent returns (step 4)

Steps 1-3 will be revisions to features that already exist on version 1.

Step 4 will be an addition.
 
## Step 1
Process data for D3.js graphs using python.
Data from https://data.wa.gov/dataset/WDFW-Hatchery-Adult-Salmon-Returns/9q4e-xhag/data
 - Make reusable scripts so application can be updated every year
 - Revisit decision making on what fields to include/exclude, emphasis on simplification
 - Come up with organized way to store/retrieve data based on hatchery  
Outputs:
  - geoJSON of hatchery locations
  - JSON of data for bar graph
  - JSON of data for density plot
  - Possibly use same dataset for bar and densityh graph. Question of storing more data on github vs processing more data on client side.

## Step 2
Recreate map and graphs on website.

### Step 2A
Create map and add hatchery locations.
 - Come up with intuitive symbols to depict hatcheries on map "black dots have no meaning" 
 - Label hatcheries on map 

### Step 2B
Create density and bar graphs.
Make decision on where to place the graphs! Sidebar? Div below? Redirect to new page?
  - Bar graph instead of line graph this time 
  - Only show one species at a time on graphs. Add ability to switch between species

## Step 3
Add river conditions and weather forecast via API connections
  - Create custom graph for river (make it look like usgs guage)
  - Rework weather forcast visualization (make it more consice)
  - Will be placed next to graphs

## Step 4
Make live connection to WDFW salmon returns dataset to show returns for the previous 7 days
  - Show as a table next to graphs
  - Symbolize hatcheries on map to show if salmon have recently return/in season




