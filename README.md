# NewsAPI_scraper
Code to help analysts with a mid-level knowledge of R or Python create a realtime news article streaming app utilising 
the News API. This is a free API that enables users to retrieve news articles in JSON format as they are published. 

To proceed with either, you will need to obtain a news API key from: https://newsapi.org/account.

An identical dashboard app has been created in R using the shiny package and in Python using the Plotly Dash package.

# R Configuration
Author: Richard Haigh

Date of Intial Upload: 03/03/2020

Written - R Desktop 3.5.2

Environment: RStudio v1.2.1335

Packages: Shiny v1.4.0, newsanchor v0.1.1, googleAuthR v1.1.1, googleAnalyticsR v0.7.1, highcharter v0.7.0, shinythemes v1.1.2 (optional)

In line with best practice, save your API key to your .Renviron folder and ensure your packages are the correct versions.
Once this is done, you should be able to run the app.R file and deploy the news article search tool to your local environment.
The sources that can be retrieved with the newsanchor R package are limited to those listed when the get_sources() function is
run. As many of these as you wish may be used in your dataset dropdown menu, just ensure you match UI input to server.

A more in-depth guide to the newsanchor functions can be found at: https://cran.r-project.org/web/packages/newsanchor/vignettes/usage-newsanchor.html. 

# Python Configuration
