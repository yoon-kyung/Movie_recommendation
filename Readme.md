# Movie recommendation project

## 0. 개요
- 개인 프로젝트(기간: 2017.10.20~)

## 1. 목표
- 협업필터링을 이용하여 영화 추천 시스템을 구현한다.

## 2. Work Flow
	1. 웹 크롤링과 MySQL 쿼리를 이용하여  AWS 서버에 데이터를 수집
	2. 협업필터링(collaborative filtering)을 이용하여 추천 시스템 구현
	3. Flask Module을 활용한 영화 추천 웹페이지 구현

## 3. Explanation of File
	1. crawling.py : 네이버영화 페이지에서 유저별로 '유저의 ID', '영화제목', '장르', '평점'을 가져온다. 
	                 여기서 영화 평을 10개 이하로 한 유저는 제외한다. (crawling.py 파일은 module로 이용한다.)
	2. do_crawling.ipynb : 크롤링을 실행.
                           crawling파일을 import 하여 10,000 페이지를 크롤링 (2000페이지씩 나눠서 실행함)