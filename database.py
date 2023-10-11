import os
from dotenv import load_dotenv
from deta import Deta  

# Load the environment variables
load_dotenv(".env")
DETA_KEY = "NO-SQL-KEY"

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("expenses_report")


def insert_period(period, incomes, expenses, comment):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items

def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)