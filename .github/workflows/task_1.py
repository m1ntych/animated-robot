import re
from collections import Counter

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

# Tīrīt tekstu un pārveidot uz maziem burtiem
text_cleaned = re.sub(r'[^\w\s]', '', text.lower())
words = text_cleaned.split()

# Skaitīt vārdu biežumu
word_count = Counter(words)
print(word_count)
