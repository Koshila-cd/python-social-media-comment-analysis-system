from textblob import TextBlob


def analyze_sentiment(comment):

    blob1 = TextBlob(comment)
    polarity = blob1.sentiment.polarity.__str__()

    return polarity
