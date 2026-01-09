# Paragraph
from langchain_core.documents import Document

text = """
Para 1 : Large Language Models process text as tokens, not characters.

Para 2 : Token-based chunking helps avoid context window overflow.

Para 3 : This is useful when sending long documents to an LLM.
"""

paragraph = [pgph.strip() for pgph in text.split("\n\n") if pgph.strip()]

chunks =  [Document(page_content=para) for para in paragraph]

print("Sentence chunks:",chunks)
print("Fixed Chunks size : ",len(chunks))

for c in chunks:
    print(f'\n{c.page_content}:{len({c.page_content})}')