from request_lists import MovieLists

url_lists = ['https://www.dytt8.net/html/gndy/jddy/20160320/50523.html',
             'https://www.dytt8.net/html/gndy/jddy/20160320/50523_2.html',
             'https://www.dytt8.net/html/gndy/jddy/20160320/50523_3.html',
             'https://www.dytt8.net/html/gndy/jddy/20160320/50523_4.html']

for index, list in enumerate(url_lists):
    print(list)
    filename = './generate/page'+str(index)+'.xls'
    MovieLists(url=list, save_filename=filename)
