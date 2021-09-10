from pprint import pprint

import requests

class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }


    def get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()


    def upload_file_to_disk(self, filename):
        href = self.get_upload_link(file_path=filename).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")



if __name__ == '__main__':

    path_to_file = 'text.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload_file_to_disk(path_to_file)
    pprint(result)