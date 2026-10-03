"""
Semantic search module using FAISS and Sentence Transformers.
"""

import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Optional


class SemanticSearcher:
    """
    Semantic search engine using FAISS vector search and Sentence Transformers.

    Example:
        searcher = SemanticSearcher("index.faiss", "metadata.json")
        results = searcher.search("neural networks for materials analysis", top_k=3)
    """

    def __init__(
            self,
            index_path: str,
            metadata_path: str,
            model_name: str = 'paraphrase-multilingual-MiniLM-L12-v2'
    ):
        """
        Initialize the semantic searcher.

        Args:
            index_path: Path to FAISS index file
            metadata_path: Path to JSON metadata file
            model_name: Name of the sentence transformer model
        """
        self.model = SentenceTransformer(model_name)
        self.index = faiss.read_index(index_path)
        with open(metadata_path, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

    def search(self, query_text: str, top_k: int = 2) -> List[Dict]:
        """
        Search for similar documents.

        Args:
            query_text: Search query
            top_k: Number of results to return

        Returns:
            List of dictionaries with similarity scores and metadata
        """
        query_emb = self.model.encode(query_text)
        query_emb = query_emb / np.linalg.norm(query_emb)
        query_array = np.array([query_emb]).astype('float32')

        distances, indices = self.index.search(query_array, top_k)

        results = []
        for i, idx in enumerate(indices[0]):
            if idx != -1:
                results.append({
                    "similarity": float(distances[0][i]),
                    "title": self.metadata[idx]["title"],
                    "abstract": self.metadata[idx]["abstract"],
                    "authors": self.metadata[idx]["authors"],
                    "year": self.metadata[idx]["year"]
                })
        return results

    def create_index(
            self,
            texts: List[str],
            index_path: str,
            metadata: Optional[List[Dict]] = None
    ) -> None:
        """
        Create FAISS index from texts.

        Args:
            texts: List of text documents to index
            index_path: Path to save FAISS index
            metadata: Optional list of metadata dictionaries
        """
        embeddings = []
        for text in texts:
            emb = self.model.encode(text)
            emb = emb / np.linalg.norm(emb)
            embeddings.append(emb)

        embeddings_array = np.array(embeddings).astype('float32')
        dimension = embeddings_array.shape[1]

        index = faiss.IndexFlatIP(dimension)
        index.add(embeddings_array)
        faiss.write_index(index, index_path)

        if metadata:
            metadata_path = index_path.replace('.faiss', '.json')
            with open(metadata_path, "w", encoding="utf-8") as f:
                json.dump(metadata, f, ensure_ascii=False, indent=2)
