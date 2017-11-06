# Movie recommendation project

## 0. 개요
- 영화 리뷰 페이지의 데이터를 활용하여 사용자 기반의 협업 필터링을 구현한다.
- 개인 프로젝트 (기간: 2017.10.20~2017.11.06)

## 1. 목표

- 협업필터링을 이용하여 영화 추천 시스템을 구현한다.

## 2. Work Flow

	1. 웹 크롤링과 MySQL 쿼리를 이용하여  AWS 서버에 데이터를 수집
	2. 협업필터링(collaborative filtering)을 이용하여 추천 시스템 구현

## 3. Explanation of File
	1. crawling.py : 네이버영화 페이지에서 유저별로 '유저의 ID', '영화제목', '장르', '평점'을 가져온다. 
	                 여기서 영화 평을 10개 이하로 한 유저는 제외한다. (crawling.py 파일은 module로 이용한다.)

	2. do_crawling.ipynb : 크롤링을 실행.
                           crawling파일을 import 하여 10,000 페이지를 크롤링 (2000페이지씩 나눠서 실행함)

	3. Delete_duplication.sql : sql을 통해 중복된 행을 제거한 후 data_set이라는 새로운 데이터를 생성
	                            (한 아이디당 여러개의 페이지를 가질 수 있기 때문에 중복값이 여러개 생기기 때문)

	4. Movie_recommendation_system : 사용자 기반 협업 필터링 알고리즘을 이용하여 추천시스템을 구현함
	                                 (더 효율적으로 사용할 수 있도록 함수를 정리중입니다.)
	                                 