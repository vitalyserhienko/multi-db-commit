from db.one.db_engine import engine as db_one_engine
from db.one.models import User
from db.two.db_engine import engine as db_two_engine
from db.two.models import Account
from db.two.models_broken import BrokenAccount

User.metadata.create_all(db_one_engine)
BrokenAccount.metadata.create_all(db_two_engine)
# Account.metadata.create_all(db_two_engine)
