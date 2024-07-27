from sentence_transformers import SentenceTransformer, util
import torch
import pandas as pd

model_name = 'nq-distilbert-base-v1'
bi_encoder = SentenceTransformer(model_name)
top_k = 5

csv_file_path = 'directions.csv'
question = "Directions from Airport Terminal 3 to Al Furjan"

df = pd.read_csv(csv_file_path)
answers = df['answer'].dropna().tolist()

if len(answers) > 0:
    passage_embeddings = bi_encoder.encode(answers, convert_to_tensor=True, show_progress_bar=True)
    question_embedding = bi_encoder.encode(question, convert_to_tensor=True, show_progress_bar=True)

    search_results = util.semantic_search(question_embedding, passage_embeddings, top_k=top_k)
    search_hits = search_results[0]

def search(query):
    question_embedding = bi_encoder.encode(query, convert_to_tensor=True)
    hits = util.semantic_search(question_embedding, passage_embeddings, top_k=top_k)
    hits = hits[0]

    if hits:
        print("Input question:", query)
        for hit in hits:
            print("\t{:.3f}\t{}".format(hit['score'], answers[hit['corpus_id']]))
    else:
        print("No valid answers found in the CSV data.")

search("Directions from Airport Terminal 3 to Al Furjan")
