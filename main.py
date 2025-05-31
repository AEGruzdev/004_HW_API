import requests
import json
from tqdm import tqdm
from pprint import pprint
import configparser

class SaveToYD:
    def init(self, token):
        self.token = token
        self.dict_photo = {}
    

    def create_folder(self, folder_name):
        url_ya = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path' : f'{folder_name}'}
        headers = {"Authorization": f'OAuth {self.token}'}
        requests.put(url_ya, params = params, headers = headers)


    def create_dogs_dict(self):
        url_breeds = 'https://dog.ceo/api/breeds/list/all'

        response_breeds = requests.get(url_breeds)
        breeds = response_breeds.json()['message']

        breeds_dict = {}
        for breed in breeds:
            if breeds[breed] == []:
                pass
            else:
                breeds_dict[breed] = breeds[breed]
        return breeds_dict