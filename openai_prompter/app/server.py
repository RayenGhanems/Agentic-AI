from dotenv import load_dotenv

load_dotenv()  # load .env before importing anything that needs the keys

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from app.chain import chain

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs() -> RedirectResponse:
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(app, chain, path="/openai_prompter")     # path is only for the server so when i to goole i will find a folder = path wehre everything lives inside

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

    
### TO START PAST:      langchain serve
