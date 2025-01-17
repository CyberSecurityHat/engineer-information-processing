import mysql.connector
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

def setup_database():
    db_config = {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD")
    }
    
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    with open("setup.sql", "r", encoding="utf-8") as sql_file:
        sql_script = sql_file.read()
    
    for statement in sql_script.split(";"):
        if statement.strip():
            cursor.execute(statement)
    
    connection.commit()
    cursor.close()
    connection.close()
    print("✅ MySQL 데이터베이스 및 테이블이 설정되었습니다.")

if __name__ == "__main__":
    setup_database()
