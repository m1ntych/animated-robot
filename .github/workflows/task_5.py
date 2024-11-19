import re

text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"
cleaned_text = re.sub(r'[@#\!\?\.\,;:]', '', text)  # Noņem liekos simbolus
cleaned_text = re.sub(r'http\S+', '', cleaned_text)  # Noņem URL
cleaned_text = cleaned_text.lower()  # Pārvērst uz maziem burtiem
print(cleaned_text)
