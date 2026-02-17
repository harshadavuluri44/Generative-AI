'''

Document object/Data structure in LangChain.


from langchain.schema import Document

doc = Document(
        page_content="This is my custom text that I want to process.",
        metadata={
            "source":"manual_input",
            "data":"2026-17-02",
            "author":"Harsha Davuluri",
        }
    )

NOTE - In the Document() class we need to pass page content directly, so prefer TextLoader for .txt files to create 
       Document objects.


----------------------------------------------------------------------------------------------------------------------

TextLoader, PyPdfLoader, DirectoryLoader classes are available in langchain.document_loaders module.

    TextLoader class is used to load plain text files into Document objects.
    PyPdfLoader class is used to load PDF files into Document objects.


    DirectoryLoader class is used to load all files in a directory into Document objects.
----------------------------------------------------------------------------------------------------------------------


TextLoader class in LangChain


    from langchain.document_loaders import TextLoader

    loader = TextLoader(file_path)
    documents = loader.load()

PyPdfLoader class in LangChain


    from langchain.document_loaders import PyPdfLoader

    loader = PyPdfLoader(file_path)
    documents = loader.load()

----------------------------------------------------------------------------------------------------------------------

'''