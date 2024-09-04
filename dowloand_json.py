import requests

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8,uk-UA;q=0.7,uk;q=0.6',
    # 'content-length': '0',
    'origin': 'https://www.asiafruitlogistica.com',
    'priority': 'u=1, i',
    'referer': 'https://www.asiafruitlogistica.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

response = requests.post('https://ems.asiafruitlogistica.com/PortalWebCatalogue/SearchByCompanyName', headers=headers)

with open('data.json', 'w') as f:
    f.write(response.text)