from langchain_text_splitters import CharacterTextSplitter, TokenTextSplitter, RecursiveCharacterTextSplitter
from langchain_core.documents import Document

docs = [
    Document(page_content="this is document one. this has several sentences. Two common types of prompt templates are static prompt templates and dynamic prompt templates. Static templates use fixed instructions with minimal variation, while dynamic templates include placeholders that are filled with user input or data. Both help maintain consistency, improve efficiency, and generate accurate responses from large language models"),
]
print(type(docs))

docs1 = [
    Document(page_content="when is document one. this has several sentences"),
]

"""
splitter = CharacterTextSplitter(
    separator="", ##By default chuck is happened based on new line which is \n\n
    chunk_size=6,
    chunk_overlap=0,
)
"""
splitter = RecursiveCharacterTextSplitter(
    separators=[" ",""], ##By default chuck is happened based on new line which is \n\n
    chunk_size=2,
    chunk_overlap=0,
)


chunks = splitter.split_documents(docs1)

print(chunks)

print("Fixed chunk size : ",len(chunks))

for i, c in  enumerate(chunks):
    print(f'\nchunk{i} :{c.page_content}:length {len(c.page_content)}' )