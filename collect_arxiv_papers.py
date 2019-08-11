import arxiv

topics = ['quantum', 'deep learning', 'machine learning', 'mathematics']

for topic in topics:
    result = arxiv.query(query=topic, max_chunk_results=10, iterative=True)
    for paper in result():
        arxiv.download(paper, dirpath="./dataset/ebooks", slugify=arxiv.slugify)
