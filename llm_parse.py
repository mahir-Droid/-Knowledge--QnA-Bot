from transformers import pipeline

# Load a question-answering pipeline
qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Example question
question = "Who wrote The Hitchhiker's Guide to the Galaxy?"

# Simulate graph-based structured data
context = """
Douglas Adams is the author of The Hitchhiker's Guide to the Galaxy.
The book was published in 1979. 
"""

response = qa_model(question=question, context=context)
print(response['answer'])
