def answer_question(question, graph, qa_model):
    # Parse question for entities
    entities = ner_pipeline(question)
    entity_names = [e['word'] for e in entities if e['entity'] == "B-LOC" or e['entity'] == "B-PER"]
    
    # Query the graph
    answers = []
    for entity in entity_names:
        answers.extend(query_graph(graph, entity))
    
    # If no structured answer, fallback to LLM
    if not answers:
        context = " ".join([f"{subj} {pred} {obj}." for subj, obj, pred in graph.edges(data='relation')])
        llm_response = qa_model(question=question, context=context)
        return llm_response['answer']
    return answers

# Test the system
print(answer_question("Who wrote The Hitchhiker's Guide to the Galaxy?", G, qa_model))
