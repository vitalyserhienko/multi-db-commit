import argparse

from db.one.db_engine import engine as db_one_engine
from db.one.models import User
from db.two.db_engine import engine as db_two_engine
from db.two.models import Account
from db.two.models_broken import BrokenAccount


parser = argparse.ArgumentParser()
parser.add_argument("-bs", "--break-schema", action="store_true",
                    help="Break DB 2 schema",)
args = parser.parse_args()

if __name__ == "__main__":
    User.metadata.create_all(db_one_engine)
    if args.break_schema:
        BrokenAccount.metadata.create_all(db_two_engine)
    else:
        Account.metadata.create_all(db_two_engine)
