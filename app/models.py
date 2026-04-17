#SQLAlchemyからテーブルの列定義に必要なものを読み込み
from sqlalchemy import Boolean, Column, Integer, String

#database.pyで作ったbaseを読み込み
from app.database import Base

#モデルクラスであるtodoを定義
class Todo(Base):
    __tablename__="todos"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,nullable=False)
    is_done=Column(Boolean,default=False) #何もしなければfalseという意味

    
