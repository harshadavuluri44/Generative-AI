'''

Models like Google Gemini Embeddings,
            OpenAI Embeddings,
            HuggingFace Embeddings 
                are specifically designed to convert text(or chunks of text) into numerical vector representations.

Input: A piece of text(sentence, paragraph, or document chunk).
Output: A high-dimensional vector (e.g., 1x768 or 1x1536 dimensions depending on the model).
Purpose: These vectors capture the semantic meaning of the text, so that similar texts have vectors that are close together in vector space.

------------------------------------------

IMPORTANT NOTE

Same Embeddings model + same word in sentence -> same vector (even across DBs).
Same Embeddings model + same word in different context -> different vectors.
Different Embeddings model -> different vectors, even for the same word in the same sentence.


'''