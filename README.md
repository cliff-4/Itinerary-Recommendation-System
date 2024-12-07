# Itinerary-Recommendation-System

## Tech used

-   Gemini API (free-tier)
-   Streamlit

## Working

-   User inputs self data, which is used to generate the initerary
-   User can change inputs and the system remembers the history of the conversation

## Reasoning for certain decisions

-   Why not use LLVM?
    -   LLVM requires a `triton` package, which is developed by OpenAI. Due to the package no longer being compatible with my python version, I chose to not include it.
-   Why not use LangChain?
    -   LangChain has a simple feature where we can easily chain conversations and prompt them as a conversation into the model. This would have made things much easier, but due to the constraint of not using packages, I chose to not use it either.
-   Why Maps API has not been included in this?
    -   Google Maps API is not free of cost and requires a credit card, which I did not want to use. On top of that, properly integrating the API with the model conversation would require more time, which I could not do in the 17 hour time span for this project, including the sleeping time.
-   Why not use multi-agent conversation
    -   Again, due to the 17 hour time span, I could not improve the project as much as I wanted to.
    -   I would have added:
        -   Maps API for collecting nearby attractions based on user ratings and daily visitors
        -   Select interested locations as nodes (done by LLM)
        -   Represent the selected nodes as a graph and determine an optimized travel path
        -   Taxi fares will be strictly based on the country's average fare costs, multiplied by distance
        -   Finally the result will be presented as a realistic travel plan for the day(s)
