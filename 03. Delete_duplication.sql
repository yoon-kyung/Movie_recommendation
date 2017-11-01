SHOW DATABASES;
USE movie_review;
SHOW TABLES;

# raw_file row 갯수 확인
SELECT COUNT(*) FROM raw_file;
# 결과값 : 140021

# 중복된 데이터 확인
DESC raw_file;
SELECT DISTINCT `user`, `title`, `genre`, `score` FROM raw_file;
SELECT COUNT(DISTINCT `user`, `title`, `genre`, `score`) FROM raw_file;
# 결과값 : 90152

# 중복된 데이터가 제거된 새로운 테이블 생성
CREATE TABLE data_set
		SELECT DISTINCT `user`, `title`, `genre`, `score` FROM raw_file;
        
# 새로운 테이블 data_set이 생성되었는지 확인
SHOW TABLES;
DESC data_set;
SELECT COUNT(*) FROM data_set;
# 결과값 : 90152