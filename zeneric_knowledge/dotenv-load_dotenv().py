"""

python-dotenv package

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

The python-dotenv package reads key-value pairs from a .env file and loads them into os.environ, so they can be accessed like any other environment variable using 
os.getenv() or os.environ[...].


---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Setup


1. Install the package (or add it to requirements.txt):

       pip install python-dotenv

2. Create a .env file in your project root:

       GOOGLE_API_KEY=your_api_key_here
       OPENAI_API_KEY=sk-xxxx
       DEBUG=True

3. Import and call load_dotenv() early in your program.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------

How load_dotenv() works?



- By default, it searches for a .env file in the current working directory, then walks up parent directories until one is found.

- It parses each KEY=VALUE line and injects them into os.environ.

- Existing environment variables are NOT overridden unless you pass `override=True`.

"""

import os
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
debug_mode = os.getenv("DEBUG", "False")

print("GOOGLE_API_KEY loaded:", bool(google_api_key))
print("DEBUG:", debug_mode)
