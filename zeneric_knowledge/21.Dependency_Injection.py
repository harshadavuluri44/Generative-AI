'''
What is Dependency Injection in FastAPI?


Dependency Injection (DI) in FastAPI is a system that let declare the things a route (or another dependency) needs - like a DB session, current user, 
config - as function parameters, and have FastAPI automatically resolve and supply them at request time.


Core mechanism: Depends()

Write a regular function (or callable class) that returns/yields the thing we need, then user Depends() to wire it into our endpoint.
-----------------------------------------------------------------------------------------------------------------------------------------------------------


EXAMPLE:

from fastapi import FastAPI, Depends

app = FastAPI()



def get_db():
    db = SessionLocal()
    
    try:
        yeild db
    finally:
        db.close()


@app.get("users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user.id).first()


FastAPI calls get_db for you, injects the result into db as Session.
-----------------------------------------------------------------------------------------------------------------------------------------------------------


Key Benefits of DI:


1. Reusability - write the logic once (e.g. get_db, get_current_user), reuse across many routes.

'''