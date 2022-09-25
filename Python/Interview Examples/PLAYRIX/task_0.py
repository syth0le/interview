import sys
import requests

from typing import Dict, Union, List

BASE_URL = "https://my-api.com"


def print_api_error(status_code: int, text: str):
    print(f"Error with status code {status_code}, message: {text}")


def print_decorator(func):
    def print_result(this: BaseRequest):
        print(f"{this.TITLE}:")
        if this.get():
            func(this)
        else:
            print("No data")
        print("\n")
    return print_result


class BaseRequest:
    TITLE: str
    API_PATH: str

    def __init__(self, user: str, project: str) -> None:
        super().__init__()
        self.user = user
        self.project = project

        self.data = []

    @property
    def api_url(self) -> str:
        path = self.API_PATH.format(user=self.user, project=self.project)
        return BASE_URL + path

    def get(self, page: int = 0) -> Union[List[Dict], List]:
        params = self.params()
        params.update(page=page, per_page=100)
        res = requests.get(self.api_url, params=params)
        if res.status_code == 200:
            response_data = res.json()
            self.data += response_data
            if len(response_data) == 100:
                self.get(page + 1)
        elif res.status_code != 404:
            print_api_error(res.status_code, res.text)
        return self.data

    def params(self):
        return {}

    def print(self):
        raise NotImplementedError()


class Comments(BaseRequest):
    TITLE = "Comments"
    API_PATH = "/{project}/activity"

    @print_decorator
    def print(self):
        result: Dict[str, int] = {}
        for item in self.data:
            if user_data := item.get('user'):
                user_name: str = user_data.get('name')
                if user_name not in result.keys():
                    result[user_name] = 1
                result[user_name] += 1
        print("{:<20} {:<10}".format('User', 'Amount'))
        sorted_result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}
        for user_name, amount in sorted_result.items():
            print("{:<20} {:<10}".format(user_name, amount))

    def params(self):
        params = {
            'mode': 'all',
        }
        return params


class Completed(BaseRequest):
    TITLE = "Completed"
    API_PATH = "/{project}/tasks"

    def params(self):
        return {
            'user': self.user,
        }

    @print_decorator
    def print(self):
        data = {
            'open': 0,
            'closed': 0,
        }
        for item in self.data:
            if item.get('state') == 'closed':
                data['closed'] += 1
                continue
            if item.get('state') == 'open':
                data['open'] += 1
        for result_name, amount in data.items():
            print(f"\t{result_name}: {amount}")


def main():
    params = {
        'user': sys.argv[1],
        'project': sys.argv[2],
    }
    Comments(**params).print()
    Completed(**params).print()


if __name__ == '__main__':
    args = sys.argv
    main()
