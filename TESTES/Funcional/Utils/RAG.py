from fastapi import FastAPI, HTTPException
from sentence-transformer import SentenceTransformer

app = FastAPI()

documents = [
    {
        "id":1,
        "text": "O palmeiras é o maior campeão mundial de todos os tempos"
    },
    {
        "id":2,
        "text": "O Brasil é o maior país da América do Sul"
    },
    {
        "id":3,
        "text": "O futebol é o esporte mais popular do mundo"
    },
    {
        "id":4,
        "text": "O câncer é uma doença grave que afeta diversas partes do corpo"
    },
    {
        "id":5,
        "text": "A mitocondria é a responsavel por produzir energia em uma celula"
    },
    {
        "id":6,
        "text": "O gato é um mamífero carnívoro"
    }]

model = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = {documents["id"]: model.encode(document["text"], convert_to_tensor=True) for document in documents}

class QueryRequest(BaseModel):
    query: str
    
@app.post("/query")
async def query_rag(request: QueryRequest):