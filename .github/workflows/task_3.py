text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

words1 = set(text1.lower().split())
words2 = set(text2.lower().split())

# Aprēķināt sakritību
common_words = words1.intersection(words2)
similarity = len(common_words) / len(words1.union(words2)) * 100
print(f"Sakritība: {similarity:.2f}%")
