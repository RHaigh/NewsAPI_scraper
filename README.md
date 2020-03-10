# NewsAPI_scraper
Code to help analysts with a mid-level knowledge of R or Python create a realtime news article streaming app utilising 
the News API. This is a free API that enables users to retrieve news articles in JSON format as they are published. 

We will produce a virtually identical app using both R and Python. 

To proceed with either, you will need to obtain a news API key from: https://newsapi.org/account.

This split will also allow us to look at two possible rendering options.

Firstly, an R shiny app that will reactively send a modified request based on input variables to the News API with every click of the submit button. This will enable more up-to-date rendering but will rapdily exhaust the limit on requests per day. 

The second Plotly Dash app, written in Python, will request all available articles on page rendering then reactively filter those displayed based on input variables. This means that the page must be refreshed to retrieve new articles but will only make 1 request per hit. Such an approach would be better suited to use from a larger team. 

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

# Python Configuration
Author: Richard Haigh

Date of Initial Upload: 

Written: Python 3.7

Packages: 
