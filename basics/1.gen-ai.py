'''

GENERATIVE AI core idea :-  Data Objects -> Deep Neural Networks (DNNs) -> Tasks


Data objects (text, images, audio, video, etc.) are fed as input to a Deep Neural Network. The DNN learns the underlying patterns, correlations, and characteristics 
of that data, and then uses what it has learned to perform generative tasks such as creating images, converting images to text, or generating new text.


LLMs are built on top of DNNs.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

LLMs are recommended to run on GPUs (Graphics Processing Units) rather than CPUs.

What actually happens when you query an LLM?

    Input text -> tokenized into tokens -> converted into vectors (embeddings)

    These vectors then flow through several mathematical operations:
        - Matrix multiplications (the bulk of the computation)
        - Attention calculations (which tokens attend to which)
        - Non-linear activation functions (e.g., GELU, Softmax)

    All of this heavy math is executed on the GPU.

Why a GPU and not a CPU?
    - A CPU has a few powerful cores optimized for sequential tasks.
    - A GPU has thousands of smaller cores optimized to run calculations in parallel.
    - LLM workloads are essentially massive parallel matrix operations, which makes them a perfect fit for GPU architecture.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Running a LLM via an API vs running it locally

    Using an API (e.g., OpenAI, Anthropic, Bedrock):
        - You don't see or manage the GPU.
        - You don't manage hardware, drivers, or memory.
        - You simply send an input (prompt) and receive an output (response).

    Running a LLM locally:
        - You must load the LLM weights into VRAM (GPU memory).
        - You must manage GPU memory, batching, and quantization.
        - You are responsible for performance, latency, and scaling.

    Under the hood, both approaches execute the same kind of math — the only real difference is who owns and operates the GPU.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

AWS EC2 provides both CPU-based and GPU-based instances.
    Example: g5.xlarge is a GPU-backed EC2 instance (NVIDIA A10G), commonly used for inference and fine-tuning of mid-sized models.

'''