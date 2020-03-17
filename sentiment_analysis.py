from textblob import TextBlob


def analyze_sentiment(comment):
    blob1 = TextBlob(comment)
    print(comment)
    print(blob1.sentiment.polarity)

    return "null"
