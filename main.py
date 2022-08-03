import json
import requests

def run():
    url = 'https://reqres.in/api/users'
    r = requests.get(url)
    print(f'{r.text} - {r.status_code}')
    r = r.json()
    print(r)

if __name__ == "__main__":
    run()