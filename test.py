import os
import requests

os.environ["HTTPS_PROXY"] = "http://proxyint.intra.bca.co.id:8080"


def get_repo():
    uri = 'https://api.github.com/repos/filipushandi23/BIA/contents/index.php'

    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": 'application/json'
    }
    response = requests.get(headers=headers, url=uri, verify=False)
    return response.json()
