from db import engine, Portfolios

Portfolios.__table__.create(bind=engine, checkfirst=True)
