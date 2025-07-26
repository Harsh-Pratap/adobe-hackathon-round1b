from sentence_transformers import SentenceTransformer
import numpy as np

class Ranker:
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def rank(self, persona, job, doc_sections, top_k=5):
        query = persona + " " + job
        query_emb = self.model.encode([query])
        contents = [sec['content'] for sec in doc_sections]
        embeddings = self.model.encode(contents)
        scores = np.inner(embeddings, query_emb).squeeze()
        idx = np.argsort(-scores)[:top_k]
        return [{
            "rank": i + 1,
            "page": doc_sections[j]["page"],
            "content": doc_sections[j]["content"],
            "score": float(scores[j])
        } for i, j in enumerate(idx)]
