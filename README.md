# southafrica-twitter
A tool to scrape and visualize twitter data using the official Twitter API, Google Maps and NetworkX/PyVis.

## Code
This app requires `Python 3.9` and pip to be installed.

Run 'setup.sh' to install the required Python Libraries. 

```sh
chmod +x ./setup.sh
./setup.sh
```

To run `userlist.py` & `userlist_fromList.py` it is required to set up an application on the Twitter Development Platform. Create your credentials there and input them in `credentials.py`.

### Usage

`userlist.py` is used for the first step of the data scraping process. <br />
`userlist_fromList.py` is used for the second step of the data scraping process.<br />
`visualization.py` is used for Network Graph Visualization of the dataset.<br />
`geo.py` is used to apply coordinates(latitude & longitude) to the dataset. <br />
`location_map.ipynb` is used to create a heat map with google maps.<br />

## Data

Contains two CSV File's. <br />

`network_data.csv` contains all the scraped data with `userlist.py` & `userlist_fromList.py`. <br />
`location_map.csv` contains the filtered data with coordinates for every scraped account.<br />

## Network Graph Visualization HTML

Contains 4 HTML Files representing the networks mentioned in the paper. 
Opening the files should open a browser window.
