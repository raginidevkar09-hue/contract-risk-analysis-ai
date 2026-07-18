from pathlib import Path

from src.extraction.extract_text import extract_text
from src.preprocessing.clean_text import clean_text
from src.document_intelligence.fixed_chunking import fixed_chunk_text
from src.embeddings.generate_embeddings import generate_embeddings
from src.vector_db.create_faiss_index import create_faiss_index


def process_contract(pdf_path: str):

    pdf_path = Path(pdf_path)

    extracted_text = extract_text(str(pdf_path))

    cleaned_text = clean_text(extracted_text)

    chunks = fixed_chunk_text(cleaned_text)

    embeddings = generate_embeddings(chunks)

    create_faiss_index(
        chunks=chunks,
        embeddings=embeddings
    )

    return {
        "status": "success",
        "chunks": len(chunks),
        "embedding_vectors": len(embeddings)
    }