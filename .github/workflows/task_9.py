from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
start_phrase = "Reiz kādā tālā zemē"
generated_text = generator(start_phrase, max_length=50)
print(generated_text[0]['generated_text'])
