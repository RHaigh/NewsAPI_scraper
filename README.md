# NewsAPI Scraper
Code to help analysts with a mid-level knowledge of R or Python create a real time news article streaming app utilising 
the News API. This is a free API that enables users to retrieve news articles in JSON format as they are published from a variety of news sources. 

We will produce a virtually identical app using both R and Python. 

To proceed with either, you will need to obtain a news API key from: https://newsapi.org/account.

This split will also allow us to look at two possible rendering options.

Firstly, an R shiny app that will reactively send a modified request based on input variables to the News API with every click of the submit button. This will enable more up-to-date rendering but will rapdily exhaust the limit on requests per day. 

The second, a Plotly Dash app written in Python, will request all available articles on page rendering then reactively filter those displayed based on input variables. This means that the page must be refreshed to retrieve new articles but will only make 1 request per hit. Such an approach would be better suited to use from a larger team. 

# R Configuration
Author: Richard Haigh

Date of Intial Upload: 03/03/2020

Written: R Desktop 3.6.2

Environment: RStudio v1.2.1335

Packages: Shiny v1.4.0, newsanchor v0.1.1, googleAuthR v1.1.1, googleAnalyticsR v0.7.1, highcharter v0.7.0, shinythemes v1.1.2 (optional)

In line with best practice, save your API key to your .Renviron folder and ensure your packages are the correct versions.
Once this is done, you should be able to run the app.R file and deploy the news article search tool to your local environment.

The sources that can be retrieved with the newsanchor R package are limited to those listed when the get_sources() function is run. As many of these as you wish may be used in your dataset dropdown menu, just ensure you match UI input to server.

A more in-depth guide to the newsanchor functions can be found at: https://cran.r-project.org/web/packages/newsanchor/vignettes/usage-newsanchor.html. 

If you wish to deploy this app externally, we recommend the use of shinyapps.io for simplicity. 

# Python Configuration
Author: Richard Haigh

Date of Initial Upload: 09/04/2020

Written: Python 3.7
Packages: dash v1.9.1, dash-core-components v1.8.1, dash-html-components v1.0.2, dash-table v4.6.1, newsapi v0.1.1, datetime v4.3, pandas v0.25.3

Utilise pip install/update to ensure packages are in line with versions given. Enter in API key and run to local drive. 

The NewsAPI limits get_everything() to 100 articles per request. This means search requests will be limited to the first 100 captured that have been published within the date/time range chosen. These will then be conditionally filtered by search input criteria. This leads to fewer articles per search. 

An in-depth guide to custom python requests to the news API library can be found at: https://newsapi.org/docs/client-libraries/python

Dash utilises Flask under the hood and, should you wish to deploy an app like this, you will need to follow the guidelines for flask cloud / server deployment: https://dash.plotly.com/deployment
