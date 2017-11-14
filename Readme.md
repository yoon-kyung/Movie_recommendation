# Movie recommendation project

## 0. 개요
- 영화 리뷰 페이지의 데이터를 활용하여 사용자 기반의 협업 필터링을 구현한다.
- 개인 프로젝트 (기간: 2017.10.20~2017.11.06)

## 1. 목표

- 사용자 기반의 협업필터링(User-based collaborative filtering)을 이용하여 영화 추천 시스템을 구현한다.

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

	4. Movie_recommendation_system : 사용자 기반 협업 필터링 알고리즘을 이용하여 추천시스템을 구현함 (수정완료 2017.11.14)
	       
## 4. URL
[[[ Movie recommendation ]]](https://render.githubusercontent.com/view/ipynb?commit=dd894be7ed168031342c42ea723c7849827f1b0b&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f596f6f6f6e6b79756e672f4d6f7669655f7265636f6d6d656e646174696f6e2f646438393462653765643136383033313334326334326561373233633738343938323766316230622f30342e2532304d6f7669655f7265636f6d6d656e646174696f6e5f73797374656d2e6970796e62&nwo=Yooonkyung%2FMovie_recommendation&path=04.+Movie_recommendation_system.ipynb&repository_id=107040258&repository_type=Repository#%EC%82%AC%EC%9A%A9%EC%9E%90-%EA%B8%B0%EB%B0%98-%ED%98%91%EC%97%85%ED%95%84%ED%84%B0%EB%A7%81%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%98%81%ED%99%94-%EC%B6%94%EC%B2%9C-%EC%8B%9C%EC%8A%A4%ED%85%9C)