'''

Generative AI


Data objects -> Deep Neural Networks -> Taks


Data objects like Data, text, audio etc are inputs which are passed to DNN to understand the patterns,
correlations and charactersitics to perform tasks like create image, convert image to text etc.

------------

LLM models are suggested to run on GPU's(Graphic Processing Units) instead of CPU's 

What really happens?

Your text -> converted to tokens -> converted to numbers (embeddings)
These numbers go through:
    Matrix Multiplications,
    Attention Calculations,
    Non-linear functions.

All of this math runs on the GPU

why GPU?
GPU runs thousands of calculations in parallel


Running model via an API vs locally

Using an API
    You don't see GPU
    You don't manage hardware
    You only send input & get output

Running model locally
    you must
        load model into VRAM
        manage GPU memory
        Handle performance

But under the hood both do the same

----------

AWS EC2 provides both CPU, GPU based instances both
Example :- g5.xlarge is GPU EC2 instance

'''