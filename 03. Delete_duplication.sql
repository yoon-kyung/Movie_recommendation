SHOW DATABASES;
USE movie_review;
SHOW tables;

# raw data의 행 갯수 확인
SELECT count(*) From review_data;
# 결과값 : 26038

# 중복된 데이터 확인
SELECT DISTINCT `UserID`, `Movie name`, `Score` FROM review_data;
SELECT COUNT(DISTINCT `UserID`, `Movie name`, `Score`) FROM review_data;
# 결과값 : 19176

# 중복된 데이터가 제거된 새로운 테이블 생성
CREATE TABLE tmp 
	SELECT DISTINCT `UserID`, `Movie name`, `Score` 
    FROM review_data;
    
# 새로운 테이블 tmp가 생성 되었는지 확인
SHOW TABLES;
DESC tmp;
SELECT count(*) FROM tmp;

# 테이블명 변경
# 1. review_data -> raw_data
# 2. tmp -> reviews
RENAME TABLE review_data TO raw_data;
RENAME TABLE tmp TO reviews;

# 테이블명 바뀌었는지 확인
SHOW TABLES;
