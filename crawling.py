import requests
from bs4 import BeautifulSoup
import MySQLdb
import re

# link를 얻어오는 함수
def get_link(url):

    res = requests.get(url)
    content = res.text
    soup = BeautifulSoup(content, 'html5lib')

    # a 태그이면서 href 속성을 갖는 경우 탐색
    links = soup.select('a[href]')

    link_list = []
    for link in links:
        if re.search(r'&target=after&page', link['href']):
            target_url = 'http://movie.naver.com' + str(link['href'])
            link_list.append(target_url)

    # '다음' 때문에 한페이지가 더 추가되어 처리
    if len(link_list) != 1:
        pop_number = len(link_list) - 1
        link_list.pop(pop_number)

    return link_list


# 유저ID, 영화제목, 평점 크롤링 함수
def do_craw(url):

    url_list = get_link(url)

    # DB 연결
    db = MySQLdb.connect(server, user, password, 'movie_review')
    db.set_character_set('utf8')
    cursor = db.cursor()

    for url in url_list:

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
            score = score_list[num]

            # DB에 데이터를 넣기 위한 쿼리
            query = """INSERT INTO review_data VALUES ('{}', '{}', '{}')""".format(user_id, title, score)

            try:
                cursor.execute(query)
                db.commit()    # commit change
            except Exception as e:
                print(str(e))
                db.rollback()    # error가 생기면 rollback

    db.close()    # DB 종료
