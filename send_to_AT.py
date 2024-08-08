import os
from dotenv.main import load_dotenv
from pyairtable import Api

load_dotenv()
pat = os.getenv("ATTOKEN")
base_id = os.getenv("BASEID")
table_id = os.getenv("TABLEID")

# Create a new record
api = Api(pat)
table = api.table(base_id, table_id)


def upload(data):
    table.create(data)
