from datetime import datetime
from pydantic import BaseModel, Field
import pymongo


class UserMessage(BaseModel):
    user_id: str
    user_message: str
    timestamp: datetime


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db_name = 'test'
collection_name = 'user_text_message'


if __name__ == '__main__':
    # reset the mongodb
    myclient.drop_database(db_name)

