"""Multi-modal neural search engine."""
class SearchEngine:
    def __init__(self, multimodal=False):
        self.multimodal = multimodal
        self.index = []
        
    def index(self, documents):
        self.index.extend(documents)
        
    def search(self, query, modality="text", top_k=5):
        return [{"id": i, "score": 0.9 - i*0.05} for i in range(min(top_k, len(self.index)))]
