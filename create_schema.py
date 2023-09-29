from postgres1_session import engine as postgres1_engine
from postgres2_session import engine as postgres2_engine
from models import User


User.metadata.create_all(postgres1_engine)
User.metadata.create_all(postgres2_engine)
