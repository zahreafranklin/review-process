import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    Creates ans saves a bar chart of sentiment counts for the reviews received from customers

    Args: 
    sentiments (list) : A list of sentiment labels as strings, that represent the categories of the reviews received

    Returns: 
    None
    """
    sentiment_counts = {
        'positive' : 0,
        'neutral' : 0,
        'negative' :0,
        'irrelevant' : 0 
    }

    for sentiment in sentiments: 
        if sentiment in sentiment_counts:
            sentiment_counts[sentiment] += 1

    categories = list(sentiment_counts.keys())
    counts = list(sentiment_counts.values())

    plt.figure(figsize=(8, 6))
    plt.bar(categories, counts, color=['green', 'yellow', 'red', 'gray'])
    plt.title("Reviews Analysis Results")
    plt.xlabel("Reviews")
    plt.ylabel("Count")

    plt.savefig("images/sentiment_plot.png")
    plt.close()
