library(shiny)
library(shinydashboard)
library(newsanchor)
library(googleAuthR)
library(googleAnalyticsR)
library(highcharter)
library(shinythemes)

# Save your news API key to your .Renviron file in the format NEWS_API_KEY = 'xxx' with an empty line after
access_token  <- Sys.getenv("NEWS_API_KEY")

# Enter in UI, editing any desired theme also
ui <- fluidPage(theme = shinytheme("superhero"),

    # Application title
    titlePanel("News API"),

    # Sidebar with a dropdown selector for your chosen news sources
    sidebarLayout(
        sidebarPanel(
        # You can include any news sources you wish, use get_sources() to see all available 
            selectInput("dataset", "Select a news source:",
                         choices = c("BBC News",
                                     "Reuters",
                                     "The Independent",
                                     "CNN",
                                     "Business Insider",
                                     "The Wall Street Journal"))
            
            # Text input box for your chosen subject to search by
            ,textInput("search", "Enter Search Criteria")
            
            ,actionButton("Update", "Update")
        ),

    mainPanel(width = '100%',
       tableOutput("news_articles") 
    )
  )
)

server <- function(input, output) {
# Note that the News API is limited to 500 requests per day
  
  data <- reactive({
    
    # We will use with_shiny() to reactively send new API requests with every refresh of the page or update selection
    x <- with_shiny(get_everything, 
    # Note that get_everything() is a newsanchor package specific function but could be swapped for another, more specific one
               query=searchInput(), language="en", 
               sources = c(dataSetInput()), 
               shiny_access_token = access_token)
               # As arguments, we will enter in our reactive functions
    
   data.frame(Date = as.character(x[[2]]$published_at),
                    Author = x[[2]]$name,
                    Title = x[[2]]$title,
                    Summary = x[[2]]$description,
                    # We want the url links to be live so we will inject html script directly
                    Link = paste0("<a href='",x[[2]]$url,"' target='_blank'>",x[[2]]$url,"</a>"))
   })

# Here we create out reactive functions that send new data to the API with our users selections
    dataSetInput <- eventReactive(input$Update, {
        switch(input$dataset,
               "BBC News" = "bbc-news",
               "Reuters" = "reuters",
               "The Independent" = "independent",
               "CNN" = "cnn",
               "Business Insider" = "business-insider",
               "The Wall Street Journal" = "the-wall-street-journal"
        )
    }, ignoreNULL = FALSE)
    
    searchInput <- eventReactive(input$Update, {
      input$search
    })
    
    output$news_articles <- renderTable({
    # We will include an error message for when there are no relevent articles found
      if(nrow(data()) == 0)
        return("Your search did not return any results")
      
      head(data(), 10) # We will limit the results to 10
  }, sanitize.text.function = function(x) x) # Sanitizing the text rendered will be necessary for our url links
}

# So to clarify, we use two reactive functions - dataSetInput and searchInput - to pass reactive variables to data()
# Data() then uses these arguments to interact with the news API and renders our table with the results

shinyApp(ui = ui, server = server)
