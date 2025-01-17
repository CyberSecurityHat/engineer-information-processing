import mysql.connector
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

def connect_db():
    """MySQL 데이터베이스 연결"""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database="exam_db"  # 데이터베이스 이름을 직접 지정
    )

def insert_question(year, exam_round, subject, question_number, question, choice1, choice2, choice3, choice4, answer):
    """DB에 단일 문제를 저장"""
    conn = connect_db()
    cursor = conn.cursor()
    
    query = """
    INSERT INTO engineer_information_processing_written_exam_questions 
    (year, exam_round, subject, question_number, question, choice_1, choice_2, choice_3, choice_4, answer)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (int(year), int(exam_round), subject, int(question_number), question, choice1, choice2, choice3, choice4, int(answer))
    
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    print(f"문제 {question_number} 저장 완료.")

if __name__ == "__main__":
    while True:
        print("\n새로운 문제를 입력하세요. 종료하려면 'exit' 입력.")
        year = input("연도: ")
        if year.lower() == 'exit': break
        exam_round = input("회차: ")
        subject = input("과목명: ")
        question_number = input("문제 번호: ")
        question = input("문제 내용: ")
        choice1 = input("①: ")
        choice2 = input("②: ")
        choice3 = input("③: ")
        choice4 = input("④: ")
        answer = input("정답 (1, 2, 3, 4): ")
        
        insert_question(year, exam_round, subject, question_number, question, choice1, choice2, choice3, choice4, answer)
        print("문제가 성공적으로 저장되었습니다.")
