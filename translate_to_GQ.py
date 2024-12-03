from transformers import AutoModelForTokenClassification, AutoTokenizer
from transformers import pipeline

# Load NER model
tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
ner_model = AutoModelForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
ner_pipeline = pipeline("ner", model=ner_model, tokenizer=tokenizer)

# Example question
question = "Who wrote The Hitchhiker's Guide to the Galaxy?"

# Extract entities
entities = ner_pipeline(question)
print(entities)

entity = "The Hitchhiker's Guide to the Galaxy"
print(query_graph(G, entity))  # Returns relationships for the entity
