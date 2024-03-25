reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

def important_words(review):
    keywords = ["good", "excellent", "bad", "poor", "average"]
    each_review = review
    for keyword in keywords:
        each_review =each_review.replace(keyword, keyword.upper())
    return each_review
for review in reviews:
    print(important_words(review))

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally_sentiments(reviews):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    
    for review in reviews:
        positive_words = 0
        negative_words = 0
        review_lower = review.lower()
        for positive in positive_words:
            positive_count += review_lower.count(positive_words)
        for negative in negative_words:
            negative_count += review_lower.count(negative_words)

print(f"Positive words: {positive_words}, Negative words: {negative_words}")
