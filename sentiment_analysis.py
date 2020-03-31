from textblob import TextBlob


def analyze_sentiment(comment):
    blob1 = TextBlob(comment)
    p = blob1.sentiment.polarity
    print("score: ", p)
    polarity = sentiment_category(p)
    print("category: ", polarity)
    return polarity


def sentiment_category(score):
    category = 'x'
    if score > 0.5:
        category = 'p'

    if score < 0.5:
        category = 'n'

    return category


if __name__ == '__main__':
    comment = "fabulous....."
    analyze_sentiment(comment)
