from pydriller import RepositoryMining
import requests
import base64
import datetime

class UpdateManager():
    def __init__(self):
        self.current_version_date = self.__read_version().split(', ')
        self.current_version = self.current_version_date[0]
        self.current_date = self.current_version_date[1]
        self.current_date = datetime.datetime.strptime(
            self.current_date,'%Y-%m-%d %H:%M:%S%z')

    def __read_version(self):
        with open('./version', 'r') as file:
            return file.read()

    def watch_version(self):
        content = requests.get(
            'https://api.github.com/repos/Yokotes/MangaWatcher/contents/version').json()
        version_and_date = base64.b64decode(content['content']).decode('utf-8').split(', ')
        new_version = version_and_date[0]
        new_date = version_and_date[1]
        
        if self.current_version != new_version:
            repo = RepositoryMining('https://github.com/Yokotes/MangaWatcher',
                since=self.current_date)

            for commit in repo.traverse_commits():
                for mod in commit.modifications:
                    try:
                        with open('./'+mod.new_path, 'w', encoding='utf-8') as file:
                            file.write(mod.source_code)
                    except:
                        return None