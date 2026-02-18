'''

Models like Google Gemini Embeddings,
            OpenAI Embeddings,
            HuggingFace Embeddings 
                are specifically designed to convert chunks into numerical vector representations.

Input: A piece of text(sentence, paragraph, or document chunk).
Output: A high-dimensional vector (e.g., 1x768 or 1x1536 dimensions depending on the model).
Purpose: These vectors capture the semantic meaning of the text, so that similar texts have vectors that are close together in vector space.

------------------------------------------------------------------------------------------------------------------------------

IMPORTANT NOTE

Same Embeddings model + same chunk in document, etc. -> same vector (even across DBs).
Same Embeddings model + same chunk in different context -> different vectors.
Different Embeddings model -> different vectors, even for the same chunk in the same sentence.

------------------------------------------------------------------------------------------------------------------------------


HOW CHUNKING WORKS ?

* Chunking is not word-by-word or line-by-line.
    Instead, it's usually done at the sentence or paragraph level, or by fixed token/character size (e.g., 500-1000 tokens per chunk).

* The goal is to balance:
    Too small chunks (word-by-word): We lose context. "Jordan" alone is meaningless.
    Too large chunks (whole document): Retrieval becomes inefficient and nosiy.

* Best practice:
    Split by semantic boundaries (paragraphs, sections, headings).
    Or use a sliding window of tokens (e.g., 500 tokens with 50-token overlap) to preserve context.


NOW


EMBEDDINGS per CHUNK

* Each chunk -> one embedding vector.
    Example: If we split a document into 10 chunks, we'll get 10 vectors.

* NOT PER WORD.
    Modern embedding models (OpenAI, Gemini, sentence-transformers) generate embeddings for the entire chunk of text, not individual words.

    Why? Because embeddings are contextual - the meaning of "Jordan" depends on the surrounding sentence/paragraph.



NOW


VECTOR DB Storage

* The vector DB stores one vector per chunk.

* Each vector is linked to metadata (document ID, chunk position, etc.).

* When a query comes in, the DB retrieves the most relevant chunks by comparing
   QUERY VECTOR <-> STORED VECTORS.


Chroma DB is an open-source vector database designed for AI applications like RAG.

------------------------------------------------------------------------------------------------------------


Sentence-Transformers

    A python library built on top of Hugging Face Transformers that provides pretrained models for generating dense embeddings of text.

        dense embeddings - vectors where most values are non-zero [1.2, -4, 3.6, 8.9, 1.7, -0.8, 0, 2.9, 1.7]

        sparse embeddings - vectors with many zeros - only few non zero values. [1, 0, -2.3, 0, 0, 1.9, 0, 0,]





'''