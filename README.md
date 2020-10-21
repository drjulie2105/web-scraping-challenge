# Web Scraping Challenge
## Step 1 - Scraping
### Scraped the [NASA Mars News site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest) 

- Utilized Jupyter Notebook, BeautifulSoup, Pandas and Requests/Splinter

- Scraped the latest news title and paragraph text

- Scraped the [featured space image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) for Mars

- Scraped the [Mars fact page](https://space-facts.com/mars/) and converted to HTML string

- Scraped the [Mars Hemispheres USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) for images of the 4 Mars Hemispheres

## Step 2 - [MongoDB](https://www.mongodb.com/) and [Flask](https://flask-doc.readthedocs.io/en/latest/)
### Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from above

- Converted jupyter notebook into a python file called [scrape_mars.py](https://github.com/drjulie2105/web-scraping-challenge/blob/development/Missions_to_Mars/scrape_mars.py)

- Created a route /scrape to import the python file

- Stored the return value in Mongo as a python dictionary

- Create a root route / to query the Mongo database and pass the mars data into an HTML template to display the data

- Created a template HTML file called [index.html](https://github.com/drjulie2105/web-scraping-challenge/blob/development/Missions_to_Mars/templates/index.html) that will take the mars data dictionary and display all of the data in the appropriate HTML elements




