from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

# Example FAQ knowledge base
demo_faq = {
    "what is mosdac": "MOSDAC stands for Meteorological and Oceanographic Satellite Data Archival Centre. It provides earth observation data from Indian satellites.",
    "how to download data": "You can download data from https://www.mosdac.gov.in by registering and logging in to your account.",
    "contact support": "For support, reach out via the 'Contact Us' section on the MOSDAC portal.",
}

@app.post("/chat")
async def chat(req: QueryRequest):
    query = req.query.lower().strip()
    for key, answer in demo_faq.items():
        if key in query:
            return {"answer": answer}
    return {"answer": f"Sorry, I couldn't find an answer for: {req.query}"}

@app.get("/")
def read_root():
    return {"message": "MOSDAC AI Help Bot backend is running."}
