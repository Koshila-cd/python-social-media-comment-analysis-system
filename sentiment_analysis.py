from textblob import TextBlob


def analyze_sentiment(comment):

    blob1 = TextBlob(comment)
    polarity = blob1.sentiment.polarity

    return polarity


def sentiment_category(score):
    category = 'x'
    if score > 0.5:
        category = 'p'

    if score < 0.5:
        category = 'n'

    return category
