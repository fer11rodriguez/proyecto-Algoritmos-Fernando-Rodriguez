import requests
def api():
    url = 'https://saman-caribbean.vercel.app/api/cruise-ships'

    response = requests.request ("GET", url)
    return response.json
