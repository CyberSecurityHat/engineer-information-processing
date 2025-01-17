CREATE DATABASE IF NOT EXISTS exam_db;
USE exam_db;

-- 정보처리기사 필기 시험 문제 테이블
CREATE TABLE IF NOT EXISTS engineer_information_processing_written_exam_questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT NOT NULL,               -- 연도
    exam_round INT NOT NULL,         -- 회차
    subject VARCHAR(255) NOT NULL,   -- 과목명
    question_number INT NOT NULL,    -- 문제 번호
    question TEXT NOT NULL,          -- 문제
    choice_1 TEXT NOT NULL,          -- 선택지 1
    choice_2 TEXT NOT NULL,          -- 선택지 2
    choice_3 TEXT NOT NULL,          -- 선택지 3
    choice_4 TEXT NOT NULL,          -- 선택지 4
    answer INT NOT NULL              -- 정답 (1~4)
);