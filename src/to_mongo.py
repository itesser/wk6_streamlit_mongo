from base import Base
from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv


class ToMongo(Base):
    """
    transports info from our base class to a mongo db instance

    initializes an instance of the inherited class

    defined methods:
    upload_one_by_one: uploads pieces of information to a database one by one over an iterable structure
    upload_collections: uploads an entire collecton of documents to mongoDB
    delete_collection: drops an entire collection of data from the database
    """

    def __init__(self):
        # initialize an instance of our inherited class
        Base.__init__(self)
        load_dotenv()
        self.__mongo_url = os.getenv("MONGO_URL")
        # connect to Mongo
        self.client = MongoClient(self.__mongo_url)
        # create/connect to database
        self.db = self.client.db
        # create/connect to collection
        self.cards = self.db.cards
        # set dataframe index to id column
        self.df.set_index("id", inplace=True)

    def upload_one_by_one(self):
        """
        uploads all items in dataframe to mongoDB one by one
        this method will take longer, but will ensure all our data is correctly uploaded
        """
        for i in self.df.index:
            self.cards.insert_one(self.df.loc[i].to_dict())

    def upload_collection(self):
        """
        uploads an entire collection of documents to mongoDB
        max upload size is 16777216 bytes
        """
        self.cards.insert_many(self.df.to_dict())

    def drop_collection(self, coll_name: str = "cards"):
        self.db.drop_collection(coll_name)


if __name__ == "__main__":
    c = ToMongo()
    print("Successful Connection!")
    c.drop_collection()
    print("dropped old collection")
    c.upload_one_by_one()
    print("sucessfully uploaded collection to mongoDB")
