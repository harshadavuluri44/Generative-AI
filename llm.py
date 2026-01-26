'''

An LLM is a deep learning model trained on massive amounts of text to understand, generate, and reason with human language.


It can answer questions, summarize text, write code, and more based on patterns learned during training
(e.g., GPT, LLaMA)


LIMITATION :- Knowledge is fixed to training data and it may hallucinate or give outdated answers.

-----------------------------------------------------------------------------------------------------------------------------

1B = 1000M = 1000*10L = 10,000L

Let's consider a Model 

        llama-2-70b  -> Released by Meta AI

            series - llama
            version/iteration - 2
            parameters - 70Billion - 70B * 2bytes = 140GigaBytes

    Each parameter is float16 data type(2 bytes)

In the backend this Model contains 2 files in Hypothetical directory

1. parameters.zip/ .bin (140GB)
    Parameters = Weights of Neural Networks

2. .c file (~500 line of C code) It can be any language
    The brain Mechanics to implement Neural Networks architecture, take input, work on parameters/weights, produce output

--------------------------------------------------------------------------------------------------------------------------------

Training  - Preparing the weights and teaching/learning to Deep Learning Models behind LLM
Inference - Use already learned weights through LLMs to predict text, etc.

--------------------------------------------------------------------------------------------------------------------------------

Parameters - How do we obtain them?

    passing chunks of data from iternet -> 6000GPUs for 12 days + Neural Network (a deep learning model 
    called a Transformer) -> parameters.bin

----------------------------------------------------------------------------------------------------------------------------------

When a prompt is given to an LLM, behind the scenes a NEURAL NETWORK (a deep learning model called a Transformer) runs inference
using the learned parameters(stored in .bin/ .safetensors) and generates output.

-----------------------------------------------------------------------------------------------------------------------------------


                                        NEURAL NETWORK
                                Predicts the nextword in sequence

        cat         ->
        sat         ->                  passed to  NN                                 ->   mat (97%)      
        on          ->      (parameters from parameters.bin is spread across NN)
        a           ->

e.g context of 4 words                                                              Predicts next word

'''