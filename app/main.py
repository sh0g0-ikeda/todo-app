from fastapi import FastAPI

app=FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

from app.database import Base, engine

from app.models import Todo
Base.metadata.create_all(bind=engine)
#baseに登録されているすべてのモデルについて対応するテーブルをDBに作成


