import sqlite3


async def create_db():
    global cur,db 
    db = sqlite3.connect("data.db")
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS GAMEHUB_DATA (user_id,user_name,phone_number,platform,console,problem)")
    db.commit()


