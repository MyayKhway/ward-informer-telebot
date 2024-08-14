import os
from dotenv.main import load_dotenv
from pyairtable import Api

load_dotenv()
pat = os.getenv("ATTOKEN")
base_id = os.getenv("BASEID")
table_id = os.getenv("TABLEID")
cancelled_table_id = os.getenv("CANCELLEDTABLEID")

# Create a new record
api = Api(pat)
table = api.table(base_id, table_id)
# table for cancelled data
cancelled_table = api.table(base_id, cancelled_table_id)


def upload(data):
    table.create(data)


def upload_cancelled(data):
    cancelled_table.create(data)
