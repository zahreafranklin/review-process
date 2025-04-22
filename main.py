from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    Reads the JSON file, processes the reviews and returns its sentiments
    """
    # open the json object
    with open(filepath, "r") as file:
        data = json.load(file)
   
    # extract the reviews from the json file
    reviews =data.get("results", [])

    print(f"Extracted {len(reviews)} reviews.")

    # get a list of sentiments for each line using get_sentiment
    sentiments = get_sentiment(reviews)

    # plot a visualization expressing sentiment ratio
    make_plot(sentiments)

    sentiment_counts = {}
    for s in sentiments:
        if s in sentiment_counts:
            sentiment_counts[s] += 1
        else:
            sentiment_counts[s] = 1

    # Print the sentiment counts manually
    print("\nSentiment counts:")
    for key in sentiment_counts:
        print(key + ":", sentiment_counts[key])

    # return sentiments
    return sentiments


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
