import crawling

page = 13296639   #최근 유저 페이지부터 순차적으로 크롤링
while page > 13295630:

    page = str(page)
    url = "http://movie.naver.com/movie/point/af/list.nhn?st=nickname&sword={}&target=after".format(page)

    crawling.do_craw(url)

    page = int(page)
    page -= 1
