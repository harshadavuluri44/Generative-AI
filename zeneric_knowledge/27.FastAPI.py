f'''

What is FastAPI?


FastAPI is a Python web framework for building APIs, built on top of Starlette (web parts) and Pydantic (data validation).



It uses Python type hints to:

    validate request/response data automatically (via Pydantic)

    auto-generate interactive docs (Swagger UI at /docs)

    run async by default

--------------------------------------------------------------------------------------------------------


1. Basic app - everything in one file


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello world"}


@app.post("/chat")
def generate_chat_response():
    return {"reply": "hi"}



Run it with:   uvicorn main:app --reload

"main" = filename,  "app" = FastAPI() instance,     "--reload" = auto-restart on code change


--------------------------------------------------------------------------------------------------------


2. Real pattern - router in its OWN file, app in ANOTHER file


-- routers/chatbot.py --


from fastapi from APIRouter


router = APIRouter(prefix="/chatbot", tags=["Chatbot"])



@router.post("", response_model=ChatResponse)
async def generate_chat_response(request: ChatRequest):
    ...
    return ChatResponse(...)



-- main.py --

from fastapi import FastAPI
from routers.chatbot import router as chatbot_router


app = FastAPI(title='My API')

app.include_router(chatbot_router)


# final route becomes: POST /chatbot 


why split routers like this:

    - each router file = one feature/domain (chatbot, orders, categories, etc.)
    - main.py stall small - just creates the app and wires routers together
    - easy to test/reuse a router without loading the whole app





'''