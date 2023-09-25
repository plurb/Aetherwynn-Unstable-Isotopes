import requests


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    url = "https://5e.tools/classes.html#artificer_tce,state:feature=s1-0"

    html_response = requests.get(url=url, headers=headers)
    text = html_response.text
    f = open("dump.html", 'w')
    f.write(text)
    f.close()

