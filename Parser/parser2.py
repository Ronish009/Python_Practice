from langchain_core.tracers import LangChainTracer
from langchain_core.runnables import RunnableLambda
# --------------------------------------------------------------
# 0️⃣  Install (run once)
# --------------------------------------------------------------
# pip install --upgrade "langchain[all]" "langchain-ollama"

# --------------------------------------------------------------
# 1️⃣ Imports – new core locations
# --------------------------------------------------------------
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
import json, re, asyncio, sys
from itertools import islice
from langsmith import Client


class MovieInfo(BaseModel):
    """Information about the requested movie."""
    title: str = Field(..., description="Official title of the movie")
    year: int = Field(..., description="Release year (e.g. 2008)")
    director: str = Field(..., description="Full name of the director")


pydantic_parser = PydanticOutputParser(pydantic_object=MovieInfo)

print(pydantic_parser)

llm = ChatOllama(
    model="gemma3:1b",  # any local Ollama model that supports JSON mode
    temperature=0.0,
    max_tokens=1024,
    # **Important** – tell Ollama to emit *pure* JSON, no markdown
    #   The underlying API accepts a `format="json"` kwarg.
    #   In the Python wrapper we pass it via `response_format`.
    response_format="json",  # <-- forces JSON output
)

template = """
Return ONLY valid JSON with EXACTLY these keys:
- title (string)
- year (integer)
- director (string)

Do NOT include schema, properties, descriptions, or extra text.

User question: {user_query}
"""
prompt = PromptTemplate(
    template=template,
    input_variables=["user_query"],

)

print(prompt)

full_prompt = prompt.invoke({"user_query": "What is Iron Man's first movie called, release Year, Director?"})
print(full_prompt)

print("2")
raw_output1 = llm.invoke(full_prompt)
print(raw_output1)
raw_output = llm.invoke(full_prompt).content
print(raw_output)

print("3")
movie = pydantic_parser.parse(raw_output)
print(movie)
print("4")
print(pydantic_parser.invoke(raw_output1))
json_match = re.search(r"\{[\s\S]*?\}", raw_output)
print(json_match)
print(json_match.group(0))
print(json.loads(json_match.group(0)))

print("*" * 60)
print("classic")


def safe_parse(text: str) -> MovieInfo:
    """
    Tries the normal Pydantic parser.
    If it fails, extracts the first JSON block with a regex
    and parses that raw dict.
    """
    try:
        return pydantic_parser.invoke(text)
    except Exception as exc:
        # ------------------------------------------------------
        # 5️⃣a  Grab the *first* {...} block (handles markdown fences)
        # ------------------------------------------------------
        json_match = re.search(r"\{[\s\S]*?\}", text)
        if not json_match:
            raise RuntimeError(f"Unable to find JSON in LLM output: {text}") from exc

        candidate = json_match.group(0)
        try:
            data = json.loads(candidate)
            return MovieInfo(**data)
        except Exception as inner:
            raise RuntimeError(
                f"Could not build MovieInfo from extracted JSON: {candidate}"
            ) from inner


pipeline = (
        prompt
        | llm
        | StrOutputParser()      # converts AIMessage → plain string
        | RunnableLambda(safe_parse)  # safe_parse returns a MovieInfo
)

# optional tracing – prints a tiny tree to stdout
#pipeline = pipeline.with_config(callbacks=[LangChainTracer()])

result_sync = pipeline.invoke(
    {"user_query": "What is Iron Man's first movie called?"}
)
print("\nResult (sync):", result_sync)


async def async_part():
    result_async = await pipeline.ainvoke(
        {"user_query": "What is Iron Man's first movie called?"}
    )
    print("\nResult (async):", result_async)


asyncio.run(async_part())


print("^"*60)

print("\n--- Streaming flow (token‑by‑token) ---")
# Build the prompt string first (the Ollama model expects a string)
#prompt_str = prompt.invoke({"user_query": "What is Iron Man's first movie called?"})
prompt_str = prompt.invoke({"user_query": "What is Iron Man's first movie called?"})
# Stream the model – we receive AIMessageChunk objects
token_stream = llm.stream(prompt_str)
print(token_stream)
collected = ""
print("[Streaming output]")
for chunk in token_stream:
    txt = chunk.content
    print(txt, end="", flush=True)  # live display
    collected += txt
print("\n--- end of stream ---")

# Parse the final collected text
movie = safe_parse(collected)
print("\nParsed after streaming:")
print(movie)