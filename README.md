# Neural Search 🔎

Multi-modal neural search with learned embeddings and reranking.

## Features

- **Multi-modal**: Text, image, audio search
- **Semantic Matching**: Beyond keyword search
- **Learned Reranking**: BERT-based precision
- **Real-time Indexing**: Sub-second indexing latency

## Benchmarks

| Task | Recall@5 | Recall@10 | Latency |
|------|----------|-----------|---------|
| Text retrieval | 0.89 | 0.93 | 12ms |
| Image retrieval | 0.82 | 0.88 | 25ms |
| Cross-modal | 0.76 | 0.83 | 35ms |

## Quick Start

```python
from neural_search import SearchEngine

engine = SearchEngine(multimodal=True)
engine.index(documents)
results = engine.search("modern architecture", modality="text", top_k=5)
```

## License

MIT