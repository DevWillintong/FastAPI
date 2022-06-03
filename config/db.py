from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://paco:pamisolo97*@localhost:3306/kibo")
meta = MetaData()
conn = engine.connect()

