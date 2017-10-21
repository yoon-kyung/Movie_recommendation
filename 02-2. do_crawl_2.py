import crawling

page = 13295630
while page > 13295330:

    page = str(page)
    url = "http://movie.naver.com/movie/point/af/list.nhn?st=nickname&sword={}&target=after".format(page)

    crawling.do_craw(url)

    page = int(page)
    page -= 1
