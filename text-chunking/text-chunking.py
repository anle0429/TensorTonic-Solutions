def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    step = chunk_size - overlap
    chunks = []
    for i in range(0, len(tokens), step):
        current_chunk = tokens[i : i + chunk_size]
        chunks.append(current_chunk)
        if i + chunk_size >= len(tokens):
            break
            
    return chunks