import sqlite3


async def create_db():
    global cur,db 
    db = sqlite3.connect("data.db")
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS GAMEHUB_DATA (user_id,user_name,phone_number,platform,console,problem)")
    db.commit()

async def create_profile(user_id,user_name):
    user = (user_id,user_name)
    cur.execute("INSERT INTO GAMEHUB_DATA (user_id,user_name) VALUES (?,?)", user,)
    db.commit()


async def get_user(user_id):
    a = cur.execute("SELECT user_name FROM GAMEHUB_DATA WHERE user_id = ?", (user_id,)).fetchone()
    return a