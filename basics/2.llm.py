'''

LLM (Large Language Model)

    An LLM is a Deep Learning model trained on massive amounts of text to understand, generate, and reason with human language.

    It can answer questions, summarize text, write code, translate languages, and more — all based on patterns learned during training.
    (e.g., GPT, LLaMA, Claude, Gemini, Mistral)

    
Limitations:
    - Knowledge is frozen at the training cutoff date.
    - May hallucinate (produce confident but incorrect answers).
    - Can give outdated information about recent events.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

1 Billion (1B) = 1,000 Million = 10,000 Lakh = 100 Crore

Example model: LLaMA-2-70B (released by Meta AI)

    series          : LLaMA
    version         : 2
    parameters      : 70 Billion
    precision       : float16 (each parameter = 2 bytes)
    model size      : 70B * 2 bytes = 140 GB

Conceptually, the model on disk is just two files:

    1. parameters.bin (or .safetensors)  -> ~140 GB
        Contains the weights of the Neural Network.

    2. inference code (~500 lines, any language: C / Python / Rust)
        Implements the Neural Network architecture: takes input, runs it through the weights, and produces output.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Training   -> The process of LEARNING the weights by exposing the model to data.
                This is expensive (GPUs, time, electricity).

Inference  -> The process of USING already-learned weights to generate predictions.
                This is what happens every time you send a prompt to an LLM.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

How are the parameters obtained?

    Chunks of text from the internet (books, code, web pages, papers)
        -> ~6,000 GPUs running for ~12 days
        -> Neural Network (a Deep Learning architecture called a Transformer)
        -> parameters.bin

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

What happens when you give the LLM a prompt?

    The prompt is fed into the NEURAL NETWORK (a Transformer), which runs inference using the learned parameters (loaded from .bin / .safetensors) and predicts the
    next token in the sequence — one token at a time.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                        NEURAL NETWORK
                                Predicts the next word in the sequence

        cat   ->
        sat   ->        passed through the NN                       ->   mat (97%)
        on    ->        (parameters spread across the layers)
        a     ->

    Context window: 4 tokens                                            Prediction: next token

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Stage 1: Pretraining

    Train on a huge, unlabeled text corpus (the internet).
    Output: a BASE MODEL that is good at predicting the next token, but not yet good at following instructions or holding a conversation.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Stage 2: Finetuning (Supervised Finetuning / SFT)

    Fine-tuning a LLM is the process of taking a pre-trained model (like GPT, LLaMa, or similar) and adapting it to perform better on a specific task or domain by 
    training it further on a smaller, specialized dataset.


    1. Write labeling instructions.
    2. Hire human labelers (or use AI assistance) to collect ~100K high-quality ideal question-answer pairs and comparisons.
    3. Finetune the base model on this curated data (~1 day of training).
    4. Obtain an ASSISTANT MODEL that follows instructions and chats naturally.
    5. Run evaluations, monitor for misbehavior, and iterate.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Stage 3: RLHF — Reinforcement Learning from Human Feedback (optional but common)

    Humans rank multiple model responses from best to worst.
    A reward model is trained on these rankings, and the LLM is further optimized to produce responses that humans prefer.

    This stage is what makes assistant models feel more helpful, harmless, and aligned with user intent.

'''