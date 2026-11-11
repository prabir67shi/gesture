LEXICON={
    "good": 2, "great": 3, "amazing": 3, "love": 3, "fast": 1, "worth": 2, "awesome": 3, "excellent": 3, "nice": 2, "perfect": 3, "bad": -2, "terrible": -3, "slow": -1, "broke": -2, "disappointed": -2, "awful": -3, "hate": -3, "poor": -2, "useless": -3,

}

NEGATIONS = {"not", "no", "never", "hardly"}
INTENSIFIERS = {"very": 2, "really": 2, "so": 2, "extremely": 3}

USE_BUT_RULE = False
USE_NEGATION_WINDOW = False
USE_NEGATION_WINDOW = 3
PUNCTUATION =  ".,!?:;\"'()"


def clean_word(word):
    return word.lower().strip(PUNCTUATION)

def is_negation(word):
    return word in NEGATIONS or word.endswith("n't")

def analyse(review):
    pairs=[]
    negate_for=0
    boost=1
    but_weight = 1

    for original in review.split():
        word=clean_word(original)
        points=0

        if is_negation(word)
        negate_for = NEGATION_WINDOW if USE_NEGATION_WINDOW else 999
        pairs.append((original, 0))
        continue

        if word == "but" and USE_BUT_RULE:
            but_weight = 2
        elif word in INTENSIFIERS:
            boost=INTENSIFIERS[word]
        elif word in LEXICON:
            points=LEXICON{word} * boost * but_weight
            if negate_for > 0:
                points = -points
                negate_for, boost =0,1

            negate_for= max(0,negate_for -1)
            pairs.append((original, points))
        return pairs

    def mood_score(review):
        return sum(points for _, points in analyse(review))


    def classify(review):
        score= mood_score(review)
        if score >= 1:
            return "POSITIVE"
        if score <= -1:
            return "NEGATIVE"
        return "NEUTRAL"

TEST_REVIEWS= [
    ("Amazing phone, I love the camera", "POSITIVE"),
    ("Terrible battery and very slow charging", "NEGATIVE"),
    ("The delivery was fast and the packing was good", "POSITIVE"),
    ("This is not good at all", "NEGATIVE"),
    ("Not bad for the price", "POSITIVE"),
    ("It arrived on Tuesday in a blue box", "NEUTRAL"),
    ("The screen is great but the battery life is terrible", "NEGATIVE"),
    ("I never thought it would be this good, totally worth it", "POSITIVE"),
    ("Really disappointed, the strap broke in a week", "NEGATIVE"),
]

def run_tests():
    correct=0
    for review, expected in TEST_REVIEWS:
        result= classify(review)
        mark= "OK" if result == expected else "XX"
        correct += result == expected
        print(f"{mark}  {result:<8} score={mood_score(review):>3} {review}")
        print(f"\nAccuracy: {correct}/{len(TEST_REVIEWS)}")

if __name__== "__main__":
    run_tests()
    print("\nType a review to chek it, or 'quit' to stop.")
    while True:
        review=input("\n> ")
        if review.strip().lower() == "quit":
            break
        scored = [(w,p) for w, p in analyse(review) if p !=0]
        print(f"{classify(review)} | score: {mood_score(review)} | words: {scored}")
