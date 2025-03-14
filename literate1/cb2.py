# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/cb2.ipynb.

# %% auto 0
__all__ = ['load_or_compute_embeddings']

# %% ../nbs/cb2.ipynb 1
import os
import json

def load_or_compute_embeddings(compute_embeddings):
    """
    Checks for required precomputed files and either loads them or computes and saves them.
    
    Parameters:
      compute_embeddings (callable): A function that computes and returns the embeddings.
    
    Returns:
      dict: The loaded or newly computed embeddings.
    """
    required_files = [
        "graph_chunk_entity_relation.graphml",
        "kv_store_text_chunks.json",
        "kv_store_doc_status.json",
        "vdb_chunks.json",
        "kv_store_full_docs.json",
        "vdb_entities.json",
        "kv_store_llm_response_cache.json",
        "vdb_relationships.json"
    ]
    
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print("Missing files detected:", missing_files)
        # Compute embeddings using the provided function
        embeddings = compute_embeddings()
        # Save results to one or more of the required files
        # (You may need to adapt this to your file structure)
        with open("vdb_chunks.json", "w", encoding="utf-8") as f:
            json.dump(embeddings, f)
        # Save other files as needed...
    else:
        print("All precomputed files found. Loading cached embeddings...")
        with open("vdb_chunks.json", "r", encoding="utf-8") as f:
            embeddings = json.load(f)
    
    return embeddings

