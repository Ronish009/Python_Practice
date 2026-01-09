# Heading
from langchain_text_splitters import MarkdownHeaderTextSplitter

md_text = """
# Intro
Para 1 : Large Language Models process text as tokens, not characters.

## Explain
Para 2 : Token-based chunking helps avoid context window overflow.

### Summary
Para 3 : This is useful when sending long documents to an LLM.
"""

headerSplit = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#" , "Header1"),
        ("##" , "Header2"),
        ("###" , "Header3"),
    ]
)

sections = headerSplit.split_text(md_text)

for i, section in enumerate(sections):
    print(f'\nchunk{i}:{section.page_content}:{len(section.page_content)}')