import requests
import fake_useragent
# import http.client

session = requests.Session()
session2 = requests.Session()
agent=fake_useragent.UserAgent().random
# print(requests.get('http://2ip.ru').text)
def get_html(url):


    # connection = http.client.HTTPSConnection("https://emgr.efsllc.com/cards/Index.action?showLoginMessage=1668381708387")
    # connection.request("GET", "/")
    # response = connection.getresponse()
    # print("Status: {} and reason: {}".format(response.status, response.reason))
    # connection.close()


    ses = session.get(url=url, headers=header)

    respa = session.post(url='https://emgr.efsllc.com/security/Logon.action', data=data, headers=header)
    cookies_dict = [{"domain": key.domain, "name": key.name, "path": key.path, "value": key.value} for key in
                    respa.cookies]  # {"domain":key.domain,"name":key.name,"path":key.path,"value":key.value}
    print(cookies_dict)


    for cookie in cookies_dict:
        session2.cookies.set(**cookie)
    print(respa.status_code)
    response=session2.get(url='https://emgr.efsllc.com/hub/', headers=header)
    # cookies_dict=[{"domain":key.domain,"name":key.name,"path":key.path,"value":key.value} for key in session.cookies]#{"domain":key.domain,"name":key.name,"path":key.path,"value":key.value}
    # session2=requests.Session()
    # for cookie in cookies_dict:
    #     session2.cookies.set(**cookie)


    # resp= session2.get('https://emgr.efsllc.com/hub/', headers=header,data=data)
    return response.text



def main():
    print(get_html('https://emgr.efsllc.com/security/Logon.action'))


if __name__ == '__main__':
    header={
'authority': 'emgr.efsllc.com',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-language': 'en-US,en;q=0.9',
'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
        'cookie':"JSESSIONID=T54vZLhShz-NRSV0aKYlWdQ+;",
'user-agent': agent
}

    data = {'userId': '5567480098040742',
            'password': '0055'
            }
    main()

#     header_in = {
# 'authority': 'emgr.efsllc.com',
# 'accept': 'application/json, text/plain, */*',
# 'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
# 'content-type': 'application/json;charset=UTF-8',
# 'cookie': 'visid_incap_1335435=538jS6M+TJOWxwjVYIhk5LyEbmMAAAAAQUIPAAAAAADY/nGPbl6DarIR34IV9kMJ; nlbi_1335435=yoM7KTg8GyqkTCvajSEkLgAAAAC+aw0RA8r1JKa/KIA8DW+T; eaa08fab87ed1a591ac7c916a5cb49ca="ep:1:en_US"; visid_incap_2270134=IZcKYN6bTdCIvQ+h9Xrs9paFbmMAAAAAQUIPAAAAAAC6M4whfQyCtUo/pY2xMYro; nlbi_2270134=Utr2DgmaWgO16xJl95dGLQAAAABZY1vYv0dJR2dfFy5c61KS; incap_ses_1415_2270134=NrwlbMEadRW2qrfu6xejE5eFbmMAAAAAf3R7oB8Z7ax2xl4NWpV7LA==; _gcl_au=1.1.1268294058.1668187545; _ga=GA1.2.666619467.1668187547; _gid=GA1.2.1200583533.1668187547; _hjSessionUser_2315094=eyJpZCI6ImNlZjEzM2ZiLWYwMTQtNTRkOC04NjIzLTRhYThkZjExMGY1MSIsImNyZWF0ZWQiOjE2NjgxODc1NDgyNjgsImV4aXN0aW5nIjpmYWxzZX0=; _privy_8A95C28985C13B54F4717896=%7B%22uuid%22%3A%223e811521-ced6-4cd1-9e94-9a5dc090c173%22%2C%22variations%22%3A%7B%7D%2C%22country_code%22%3A%22US%22%2C%22region_code%22%3A%22US_NE%22%2C%22postal_code%22%3A%2268137%22%7D; privy_suppress_2641153=1668187549; JSESSIONID=PY3rggzgOeRvu99UKCsOkfe7; incap_ses_1420_1335435=HSzYDhPWmVfegjfA6dq0Ew6UbmMAAAAAuLg1BTLkSo5z/Mhljm8yYQ==; AWSALBTG=Kn/WEpFaDe3XQ5ImYf303g7NX8Ug8VzTcj37QmMoAMFECW6EY2yMrCrwhNXZ2QUtDFedx8p9Q/jukx+UYAtvmqXSJrZW06A8V5fXwT5qN9FNN6hocT7iJWyVDz+PJ6Nup9hXtM5Ib4GfGJOQPDH3CNVie0ikmjK8dHQI1fQJ1VNTtieQ7gQ=; AWSALBTGCORS=Kn/WEpFaDe3XQ5ImYf303g7NX8Ug8VzTcj37QmMoAMFECW6EY2yMrCrwhNXZ2QUtDFedx8p9Q/jukx+UYAtvmqXSJrZW06A8V5fXwT5qN9FNN6hocT7iJWyVDz+PJ6Nup9hXtM5Ib4GfGJOQPDH3CNVie0ikmjK8dHQI1fQJ1VNTtieQ7gQ=; AWSALB=T6oPtNuH6DqawDqY/cwvbUiuKl3rPNIhR+i+62FZ8a5mqIEyCjvDor9CZI5fAHBJF7+HhpSRkXc5l0xqT7UHGcjl0fKwWES2FkDn229+PU0b9rK7HuihxG//Fzek; AWSALBCORS=T6oPtNuH6DqawDqY/cwvbUiuKl3rPNIhR+i+62FZ8a5mqIEyCjvDor9CZI5fAHBJF7+HhpSRkXc5l0xqT7UHGcjl0fKwWES2FkDn229+PU0b9rK7HuihxG//Fzek; incap_ses_1420_1335435=1GsJPxPum36elzfA6dq0E0aUbmMAAAAAdcx/OCt7mQ3o0iI8biq9wg==; nlbi_1335435=QUxRF+RBp3LXQkDHjSEkLgAAAAC63F/ju2sWc/z/MNFTHnEW; visid_incap_1335435=Z2YP89l8T+mh+nhb6ngbJUaUbmMAAAAAQUIPAAAAAABTft6mZtvtjgBmSBwo+gvL; AWSALB=QEg3tY8GDS1lhuAqNXsuu3lWqw/Y2GbUgPpdkPkTdgbpMVdjIh8PChmq9V8IWS9fYLsvyen6VJ2qR+xLMPPD8CI4TLEHEg1b1Ef2ntOT/KPpmvsyz2+chT1bxdQe; AWSALBCORS=QEg3tY8GDS1lhuAqNXsuu3lWqw/Y2GbUgPpdkPkTdgbpMVdjIh8PChmq9V8IWS9fYLsvyen6VJ2qR+xLMPPD8CI4TLEHEg1b1Ef2ntOT/KPpmvsyz2+chT1bxdQe; AWSALBTG=i6jwxBDu1aa9waFs5oOvpdX91vrKvgDE6zddTq6UyB9MnhJA7DSwlAurpGxav/jjmtSXkBmanfaiy31sUBgeohMKdAbgd1gVFkv2sulYKpyHES+TWf9TBXLneucq16/GM50pGfEr3eOiLTOeDLRgIK6qf8yf9GSKnrEhvGFF0AWpxQ0qmB0=; AWSALBTGCORS=i6jwxBDu1aa9waFs5oOvpdX91vrKvgDE6zddTq6UyB9MnhJA7DSwlAurpGxav/jjmtSXkBmanfaiy31sUBgeohMKdAbgd1gVFkv2sulYKpyHES+TWf9TBXLneucq16/GM50pGfEr3eOiLTOeDLRgIK6qf8yf9GSKnrEhvGFF0AWpxQ0qmB0=; CeppUyl8ZywX8Qp3rM8ap83W1SQISTG1j=etBuXCJqatzT4paxglw4OZfY6xyU54UL; JSESSIONID=XwmImWW-9UkUpCrJft45V-tc; eaa08fab87ed1a591ac7c916a5cb49ca="ep:1:en_US"',
# 'origin': 'https://emgr.efsllc.com',
# 'referer': 'https://emgr.efsllc.com/priceloc/',
# 'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
# 'sec-ch-ua-mobile': '?0',
# 'sec-ch-ua-platform': '"Linux"',
# 'sec-fetch-dest': 'empty',
# 'sec-fetch-mode': 'cors',
#         'TmxSessionId': 'ee2ec650d07949338e169f47930d021cc93f9f4fb0758ed45dc73eb08fe4b288',
#         ' uuid': 'IlVSTDogaHR0cHM6Ly90bXguZWZzbGxjLmNvbS9mcC90YWdzLmpzIC0gT3JnSWQ6IGJrd2F1OXdzIC0gdG14U2Vzc2lvbklkOiBlZTJlYzY1MGQwNzk0OTMzOGUxNjlmNDc5MzBkMDIxY2M5M2Y5ZjRmYjA3NThlZDQ1ZGM3M2ViMDhmZTRiMjg4IC0gRXJyb3I6ICI =',
#         'sec-fetch-site': 'same-origin',
#         'TimeSpentOnLogin': '146',
# 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
# }


# 'cookie': 'visid_incap_1335435 = r9DWm9lvSO2QTUMAGHlmNQczcWMAAAAAQUIPAAAAAAB9TRr5WDBacYE6m8A5qdE6;'
#                   'incap_ses_767_1335435 = dDhSAEr / 7j'
#                   'Z3nGNEnu6kCgczcWMAAAAAIg7R8RlkYzM48tuLAy25uw ==;'
#                   'JSESSIONID = DjjhDyOCHBdCQPwvl1VGXi0C;'
#                   'nlbi_1335435 = RS1iBvALjBpwzhqrjSEkLgAAAACaE666Aw / lFY0JymuCii6f;'
#                   '_gid = GA1'
#                   '.2'
#                   '.1878168386'
#                   '.1668363021;'
#                   'eaa08fab87ed1a591ac7c916a5cb49ca = "ep:1:en_US";'
#                   'CeppUyl8ZywX8Qp3rM8ap83W1SQISTG1j = ZE47JBt50vDJ9UiyTykejPwAI3HZ7kL3;'
#                   '_ga_34B604LFFQ = GS1'
#                   '.1'
#                   '.1668363021'
#                   '.1'
#                   '.1'
#                   '.1668364576'
#                   '.38'
#                   '.0'
#                   '.0;'
#                   '_ga = GA1'
#                   '.1'
#                   '.219501923'
#                   '.1668363021;'
#                   'AWSALBTG = kCn4GSZWEFIqRwysHENfmv1zSlzDQuW6MQU238Djg4SjxG7dHm33w0Xj5XkMvYpY1mi4UuJGr43ljEzhURzsX1zai4tXMkqTyOwxGpVywGseHklp1 / wZOM1DUI1mlM / ngy3xrTB0Eh / p929Vy9 / 2l'
#                   'EgeebvYvODs8VwaJoDPiUWxp4reQFk =;'
#                   'AWSALBTGCORS = kCn4GSZWEFIqRwysHENfmv1zSlzDQuW6MQU238Djg4SjxG7dHm33w0Xj5XkMvYpY1mi4UuJGr43ljEzhURzsX1zai4tXMkqTyOwxGpVywGseHklp1 / wZOM1DUI1mlM / ngy3xrTB0Eh / p929Vy9 / 2l'    'EgeebvYvODs8VwaJoDPiUWxp4reQFk =;'
#                   'AWSALB = BOVs7KVOnNB1DN9BMGLY724A + IODvtEQT / N9wWC / KEt7cBM835rNqEgEDajyis3xMHRcDhkqgNc1Ueyh6JDJxhS6mEwlSDAfoDQNLVRByEsrg3oxFcYphZKbCcJu;'
#                   'AWSALBCORS = BOVs7KVOnNB1DN9BMGLY724A + IODvtEQT / N9wWC / KEt7cBM835rNqEgEDajyis3xMHRcDhkqgNc1Ueyh6JDJxhS6mEwlSDAfoDQNLVRByEsrg3oxFcYphZKbCcJu'

#
# url = "https://emgr.efsllc.com/priceloc/locations/search"
#
# payload_searches = [
#     "{\r\n  \"showPrice\": \"DISCOUNT\",\r\n  \"searchRange\": 80,\r\n  \"latitude\":34.2665,\r\n  \"longitude\": -79.7321,\r\n  \"drid\": \"0055\",\r\n  \"_mt691917882\": \"9074597774479768396\"\r\n}"
# ]
#
# headers = {
#     'authority': 'emgr.efsllc.com',
#     'accept': 'application/json, text/plain, */*',
#     'accept-language': 'en-US,en;q=0.9',
#     'cache-control': 'no-cache',
#     'content-type': 'application/json;charset=UTF-8',
#     'dnt': '1',
#     'origin': 'https://emgr.efsllc.com',
#     'pragma': 'no-cache',
#     'referer': 'https://emgr.efsllc.com/priceloc/',
#     'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
#     # 'Cookie': 'incap_ses_1011_1335435=eUlTB1o43XJypCgOyssHDuWQ/GIAAAAASr/amZ37RveQJIdnzCN53w==; nlbi_1335435=SSMIIJ2kmUPJMtasjSEkLgAAAACDFV4CtUmHZLSXGTXSAIK0; visid_incap_1335435=b6Jo7zQ9RtKArS8DyuVDgtmH+2IAAAAAQUIPAAAAAAC9WmBgoljIVomiiIwfRZeR; AWSALB=BPT1+rxdzi7Om2jlPoGKlz1f6XnR3zYMiy11ZGEhcB2blyOOSU1wNLolDQk20HRC2YjbvrpPbW94GcLW45V/7Fn62chiktb1EE+/GQXGBOFNnXepDC/aFGYNJkOE; AWSALBCORS=BPT1+rxdzi7Om2jlPoGKlz1f6XnR3zYMiy11ZGEhcB2blyOOSU1wNLolDQk20HRC2YjbvrpPbW94GcLW45V/7Fn62chiktb1EE+/GQXGBOFNnXepDC/aFGYNJkOE; AWSALBTG=t7gPZaVaPFD0yByTPB5Q+q7Kvod1vT01MDZhxOqDtdFTB0M3FPbAO/XdwJofKCjWmpQxVgS9orX2eOD0vCZ4Nq77nrReAS9NGBXvGyjy7Wc3eUyg2fDqrGqOr31HjZt0vPh8x7FfDfIWxTIsVPte4KpOBn3l2oEbOVgTds8isWJCeKRC8as=; AWSALBTGCORS=t7gPZaVaPFD0yByTPB5Q+q7Kvod1vT01MDZhxOqDtdFTB0M3FPbAO/XdwJofKCjWmpQxVgS9orX2eOD0vCZ4Nq77nrReAS9NGBXvGyjy7Wc3eUyg2fDqrGqOr31HjZt0vPh8x7FfDfIWxTIsVPte4KpOBn3l2oEbOVgTds8isWJCeKRC8as=; CeppUyl8ZywX8Qp3rM8ap83W1SQISTG1j=K7zfjmTTnkSXDbvy0RMRGlgmKKWG5ewJ; JSESSIONID=hsLzp4phTETIuKbAHcNFRs6l; eaa08fab87ed1a591ac7c916a5cb49ca="ep:1:en_US"'
# }
#
# # for latitude, longitude in df_search_points.itertuples(index=False):
# session = requests.Session()
# session.post(url, headers=headers, data=payload_searches)