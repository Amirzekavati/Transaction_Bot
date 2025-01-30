from pymongo import MongoClient
from pymongo.errors import PyMongoError

class AgentDataBase:
    def __init__(self, client='mongodb://localhost:27017/', db_name='Transactions', collection_name='stocks'):
        # initialize database
        self.client = MongoClient(client)
        self.database = self.client[db_name]
        self.collection = self.database[collection_name]

    def find_stock(self, stockName, collection_name="stock"):
        stock_doc = self.database[collection_name].find_one({'StockName': stockName})
        if stock_doc:
            print(f"volume of stock is: {stock_doc['volume']}")
        else:
            print(f"No stock found for this name: {stockName}")

    # for insert document into database
    # if document exist replace into database
    def upsert(self, message_dict ,collection_name):
        existing_doc = self.database[collection_name].find_one({
            'StockName': message_dict['StockName']
            }
        )
        # if we have disticnt data then replace
        if existing_doc:
            self.database[collection_name].replace_one({'StockName': existing_doc['StockName']}, message_dict)
            print("replace the message")
        else:
            self.database[collection_name].insert_one(message_dict)
            print("insert the message")

    # delete document
    def delete(self, message_dict, collection_name):
        result = self.database[collection_name].delete_one(message_dict)
        if result.deleted_count > 0:
            print("The message was deleted successfully")
        else:
            print("No matching document found to delete")

    #delete collection
    def remove_collection(self, collection_name):
        self.database[collection_name].drop()
        print(f"Collection '{collection_name}' dropped successfully")

    # close database
    def close(self):
        if self.client:
            self.client.close()
            self.client = None
        print("The database was closed")

    # remove all of documents
    def clear_database(self, collection_name):
        result = self.database[collection_name].delete_many({})
        print(f"Cleared the database. {result.deleted_count} documents deleted.")

    def check_connection(self):
        try:
            server_status = self.database.command("serverStatus")
            print("✅ Successfully connected to the database")
            return {"Status": "success", "Message": "Database connected successfully",
                    "Server_host": server_status["host"]}
        except PyMongoError as e:
            print(f"❌ Failed to connect to the database: {e}")
            return {"status": "error", "Message": f"Database connection failed: {e}"}
        except Exception as e:
            print(f"❌ Failed to connect to the database: {e}")
            return {"status": "error", "Message": f"Database error: {e}"}