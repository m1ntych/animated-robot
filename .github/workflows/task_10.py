from googletrans import Translator

translator = Translator()
sentences = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

for sentence in sentences:
    translated = translator.translate(sentence, src='lv', dest='en')
    print(f"Latviešu: {sentence} -> Angļu: {translated.text}")
