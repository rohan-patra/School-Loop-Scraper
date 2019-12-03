import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/78.0.3904.97 Safari/537.36',
}
passwords = []

login_data = {
    'login_name': '###put username here###',
    'password': '#put password here#',
    'form_data_id': '49429767250096166',
    'event_override': 'login'
}
with requests.Session() as s:
    print("user: "+str(login_data['login_name'])+" pass: "+str(login_data['password']),)
    url = "https://dvhs.schoolloop.com/portal/login/portal/login?etarget=login_form"
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    login_data['form_data_id'] = soup.find('input', attrs={'name': 'form_data_id'})['value']
    r = s.post(url, data=login_data, headers=headers)
    if "Logout" in str(r.content):
        print(" success\n")
    else:
        print(" fail\n")
