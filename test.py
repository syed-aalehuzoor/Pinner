import datetime
import requests
import wget


start_time = datetime.datetime.now()
wget.download(url='https://m.media-amazon.com/images/I/71jtBXKoTyL._AC_SX522_.jpg', out='image.jpg')
end_time =  datetime.datetime.now()
print('time consumed: ',end_time-start_time)
