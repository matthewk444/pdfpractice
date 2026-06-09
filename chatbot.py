

from sentence_transformers import SentenceTransformer
from embedding import collection
import anthropic



#create question and encode it to get the embedding vector for the question
model = SentenceTransformer('all-MiniLM-L6-v2')
question = ["what is the most recent work experience?"]

question_embedding = model.encode(question)

#query ChromaDB to get most similar embedding to the question 
results = collection.query(
    query_embeddings = question_embedding.tolist(),
    n_results = 3
)

documents = results.get('documents') if isinstance(results, dict) else None
if documents and documents[0]:
    context = "\n".join(documents[0])
else:
    context = ""

client = anthropic.Anthropic()
client.messages.create(
    model = "claude-opus-4-0", 
    mes



