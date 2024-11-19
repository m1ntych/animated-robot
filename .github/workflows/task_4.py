from textblob import TextBlob

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

for sentence in sentences:
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        print(f"Pozitīvs: {sentence}")
    elif sentiment < 0:
        print(f"Negatīvs: {sentence}")
    else:
        print(f"Neitrāls: {sentence}")
