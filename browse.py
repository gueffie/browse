import requests





query = input("que Recherchez-Vous ?")
starts = list(x for x in range(1,100,10))
for start in starts:
    API_KEY = "AIzaSyB9Ybuhj2mimH0AWLweV9ljVA4S_oOCX44"
    SEARCH_ENGINE_ID = "014463886005110263066:h5g73seoq-8"
    url = (f"https://www.googleapis.com/customsearch/v1?key={API_KEY}"
           f"&cx={SEARCH_ENGINE_ID}&q={query}")
    params = {'num': 10, 'start': start}
    res = requests.get(url, params=params).json()



items = res['items']
for item in items:
    title = item['title']
    print(title)

