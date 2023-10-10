import sqlite3
from datetime import datetime

con = sqlite3.connect("data/database.db")
cur = con.cursor()
today = datetime.today()

class Database:

    @staticmethod
    def create_users_table():
        con.execute("""CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id VARCHAR(255),
                    username VARCHAR(255),
                    full_name VARCHAR(255),
                    joined_date TEXT
        )""")
        con.commit
        print("users table created")

    @staticmethod
    def add_user(user_id, username, full_name, joined_date=today):
        cur.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
        if not cur.fetchall():
            cur.execute("INSERT INTO users (user_id, username, full_name, joined_date) VALUES (?, ?, ?, ?)", (user_id, username, full_name, joined_date))
            con.commit()
            print(f"{full_name} successfully added")

    @staticmethod
    def get_word(word_id):
        cur.execute(f"SELECT * FROM words WHERE id = {word_id}")
        data = cur.fetchone()
        return data
    
    @staticmethod
    def todays_words_table():
        today = datetime.today().date().strftime("%d_%m_%Y")
        cur.execute(f"""CREATE TABLE IF NOT EXISTS day_{today}(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    word_id INTEGER,
                    time VARCHAR(255) DEFAULT CURRENT_TIME,
                    FOREIGN KEY (word_id) REFERENCES words(id)
        )""")
        con.commit()
        print("todays table created")
    
    @staticmethod
    def add_todays_word(word_id):
        today = datetime.today().date().strftime("%d_%m_%Y")
        cur.execute(f"INSERT INTO day_{today}(word_id) VALUES ({word_id})")
        con.commit()
        print("Added word")
    
    @staticmethod
    def check_word(word_id):
        today = datetime.today().date().strftime("%d_%m_%Y")
        try:    
            cur.execute(f"SELECT * FROM day_{today} WHERE word_id = {word_id}")
            if cur.fetchall():
                return True
            return False
        except Exception as err:
            print(f"Error: {err}")
            return False
    