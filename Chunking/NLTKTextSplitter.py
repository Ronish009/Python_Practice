# pip install nltk
"""
Uses punctuation AND spacing patterns

Expects a space after . to detect sentence boundaries reliably
"""
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")

from langchain_text_splitters import NLTKTextSplitter
from langchain_core.documents import Document

text = ("""
Sentence one is small. Sentence two is large. Sentence three is very vey large. Sentence Four is important. Sentence Five. Sentence six. Sentence seven. Uses punctuation AND spacing patterns. Expects a space after to detect sentence boundaries reliably.
""")
doc = Document(page_content=text)
nltk_splitter = NLTKTextSplitter(
    chunk_size=80,
    chunk_overlap=40
)

chunks = nltk_splitter.split_documents([doc])

print("Sentence chunks:",chunks)
print("Fixed Chunks size : ",len(chunks))

for i, c in  enumerate(chunks):
    print(f'\nchunk{i}:{c.page_content}:{len(c.page_content)}')