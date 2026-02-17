'''

A LLM is a Deep Learning model trained on massive amounts of text to understand, generate, and reason with human language.


It can answer questions, summarize text, write code, and more based on patterns learned during training.
(e.g., GPT, LLaMA)


LIMITATION :- Knowledge is fixed to training data and it may hallucinate or give outdated answers.

-------------------------------------------------------------------------------------------------------------------------------------

1B = 1000M = 1000*10L = 10,000L = 100 Crores

Let's consider a Model 

        LLaMA-2-70b  -> Released by Meta AI

            series - LLaMA
            version/iteration - 2
            parameters - 70Billion - 70B * 2bytes = 140GigaBytes

    Each parameter is float16 data type(2 bytes)

In the backend this Model contains 2 files in Hypothetical directory

1. parameters.zip/ .bin (140GB)
    Parameters = Weights of Neural Networks

2. .c file (~500 line of C code) It can be any language
    The brain Mechanics to implement Neural Networks architecture, take input, work on parameters/weights, produce output.

-------------------------------------------------------------------------------------------------------------------------------------

Training  - Preparing the weights and teaching/learning to Deep Learning Models behind LLM
Inference - Using already learned weights through LLMs to predict text, etc.

-------------------------------------------------------------------------------------------------------------------------------------

Parameters - How do we obtain them?

    passing chunks of data from iternet -> 6000GPUs for 12 days + Neural Network (a Deep Learning model 
    called a Transformer) -> parameters.bin

-------------------------------------------------------------------------------------------------------------------------------------

When a prompt is given to an LLM, behind the scenes a NEURAL NETWORK (a Deep Learning model called a Transformer) runs inference
using the learned parameters(stored in .bin/ .safetensors) and generates output.

-------------------------------------------------------------------------------------------------------------------------------------


                                        NEURAL NETWORK
                                Predicts the nextword in sequence

        cat         ->
        sat         ->                  passed to  NN                                 ->   mat (97%)      
        on          ->      (parameters from parameters.bin is spread across NN)
        a           ->

   e.g context of 4 words                                                              Predicts next word


   
The whole above is like Pretraining

-------------------------------------------------------------------------------------------------------------------------------------

Stage 2: Finetuning


Write labeling instructions
Hire people or use Ai, collect 100K high quality ideal Q&A responses, and and/or comparisions.
Finetune base model(above) on this data, wait ~1 day.

Obtain Assistant Model.

Run lot of evaluations.
Monitor, collect misbehaviors, repeat the step 1.

-------------------------------------------------------------------------------------------------------------------------------------

Stage 3: RHF - Reinforcement Learning from Human Feedback (optional)

'''