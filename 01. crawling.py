import requests
from bs4 import BeautifulSoup
import MySQLdb
import re

# 각 user가 평가한 영화의 link를 얻는 함수
def get_movie_link(url):

    res = requests.get(url)
    content = res.text
    soup = BeautifulSoup(content, 'html5lib')

    # a 태그이면서 href 속성을 갖는 경우 탐색
    movie_links = soup.select('a[href]')

    movie_links_list = []
    for link in movie_links:
        if re.search(r'st=mcode&sword' and r'&target=after$', link['href']):
            target_url = 'http://movie.naver.com/movie/point/af/list.nhn'+str(link['href'])
            movie_links_list.append(target_url)

    return movie_links_list


# get_movie_link로 부터 영화의 url을 받고, 장르를 가져오는 함수
def genre_list(url):

    movie_links_list = get_movie_link(url)

    genre_list = []
    for movie_url in movie_links_list:
        res = requests.get(movie_url)
        content = res.text
        soup = BeautifulSoup(content, 'html5lib')

        genre = soup.find_all('table', class_='info_area')

        for genre in genre:
            genre_list.append(genre.a.get_text())

    return(genre_list)


# user의 page link를 얻어오는 함수
def get_user_link(url):

    res = requests.get(url)
    content = res.text
    soup = BeautifulSoup(content, 'html5lib')

    # a 태그이면서 href 속성을 갖는 경우 탐색
    page_links = soup.select('a[href]')

    page_link_list = []
    for link in page_links:
        if re.search(r'&target=after&page', link['href']):
            target_url = 'http://movie.naver.com' + str(link['href'])
            page_link_list.append(target_url)

    # '다음' 때문에 한페이지가 더 추가되어 처리
    if len(page_link_list) != 1:
        pop_number = len(page_link_list) - 1
        page_link_list.pop(pop_number)

    return page_link_list

# url을 받아서 데이터를 크롤링 해오는 함수
def do_crawl(url):

    url_list = get_user_link(url)

    # DB 연결
    db = MySQLdb.connect(server, user, pwd, 'movie_review')
    db.set_character_set('utf8')
    cursor = db.cursor()

    # 평점을 10개 이하로 준 유저는 제외한다
    if len(url_list) >= 2:

        for url in url_list:

            genre_list_ = genre_list(url)

            res = requests.get(url)
            content = res.text
            soup = BeautifulSoup(content, 'html5lib')

            user_id = soup.find_all('a', class_='author')
            title = soup.find_all('td', class_='title') # a 태그
            score = soup.find_all('td', class_='point')

            user_id_list = []
            for user_id in user_id:
                replaced_user_id = re.sub(r'[*]', '', user_id.get_text())   #유저ID '*' 처리 된것 정규식으로 처리
                user_id_list.append(replaced_user_id)

            title_list = []
            for title in title:
                title_list.append(title.a.get_text())

            score_list = []
            for score in score:
                score_list.append(score.get_text())


            for num in range(0, len(user_id_list)):

                user_id = user_id_list[num]
                title = title_list[num]
                genre = genre_list_[num]
                score = score_list[num]

                # DB에 데이터를 넣기 위한 쿼리
                query = """INSERT INTO raw_file VALUES ('{}', '{}', '{}', '{}')""".format(user_id, title, genre, score)

                try:
                    cursor.execute(query)
                    db.commit()    # commit change
                except Exception as e:
                    print(str(e))
                    db.rollback()    # error가 생기면 rollback

        db.close()    # DB 종료
