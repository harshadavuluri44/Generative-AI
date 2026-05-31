'''

python-dotenv package is used to load environment variables from .env file into os.environ.





1. Add python-dotenv in requirements.txt file



2. from dotenv import load_dotenv



load_dotenv() looks for a .env file (by default in the current working directory or any parent directory) and loads its key-value pairs into os.environ



After loading

    os.getenv("GOOGLE_API_KEY") then retrieves the value of the GOOGLE_API_KEY variable from .env



'''