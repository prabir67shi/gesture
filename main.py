SPAM_WORDS= {
    "free": 2, "winner": 3, "won": 3, "prize": 3, "lottery": 3,
    "urgent": 2, "click": 2, "claim": 2, "cash": 2, "verify": 2,
    "congratulations": 2, "offer": 1, "limited": 1, "account": 1,
}
THRESHOLD = 4
USE_LEFT = False

LEET = str.maketrans("13450@$","ieasoas" )
PUNCTUATION = ",.!?:;\"'()"

def clean_word(word):
    word = word.lower()
    if USE_LEET:
        word = word.translate(LEET)
    return word.strip(PUNCTUATION)

def tokenize(message):
    words = []
    for word in message.split():
        cleaned = clean_word(word)
        if cleaned:
            words.append(cleaned)
        return words


def spam_score(message):
    score=0
    for word in tokenize(message):
        score += SPAM_WORDS.get(word, 0)
    return score


def classify(message):
    if spam_score(message) >= THRESHOLD:
        return "SPAM"
    return "SAFE"

def explain(message):
    return [word for word in tokenize(message) if word in SPAM_WORDS]

TEST_MESSAGES=[ 
    ("Congratulations ! You WON a free IPhone. Click now to claim", "SPAM"),
    ("Urgent: verify your account or it will be blocked", "SPAM"),
    ("Claim your cash before midnight", "SPAM"),
    ("Hey, are we still meeting at 5?", "SAFE"),
    
]