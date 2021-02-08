# Political Popularity of Misinformation
- This project looks at the popularity and influence of politicians on Twitter by analyzing the engagement ratios as well as the rolling and cumulative maxes of likes and retweets over time.

### Using `run.py`
- To get the data, from the project root directory, run `python run.py data`
    * This downloads the data using the tweet IDs found in `src/data`.
    * The politicians to analyze can be specified in `config/data-params.json`.
    * The name of the txt file containing the tweet IDs must match the name specified in `config/data-params.json`.
    * Output is a json file for each politician containing their collection of tweets.

- To get the data needed for the ratios, from the project root directory, run `python run.py ratio`
    * This downloads the data using the tweet IDs found in `src/data`.
    * The politicians to analyze can be specified in `config/data-params.json`.
    * The name of the txt file containing the tweet IDs must match the name specified in `config/data-params.json`.
    * Output is a csv file for each politician containing the engagement metrics of their tweets.

- To run the test target, from the project root directory, run `python run.py test`
    * This runs most of the above targets on a small, fake dataset.

### Note
- To get the data necessary to replicate this project, access to the Twitter API is needed. 