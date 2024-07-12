from os import getenv
from github import Github
from dotenv import load_dotenv

def read_github_file(access_token, repo_name, file_path):
    g = Github(access_token)
    repo = g.get_repo(repo_name)
    file_content = repo.get_contents(file_path)
    return file_content.decoded_content.decode('utf-8')

ACCESS_TOKEN=getenv("GITHUB_TOKEN")
REPO_NAME = 'coparaoji/mayrock'
FILE_PATH = 'app.py'

content = read_github_file(ACCESS_TOKEN, REPO_NAME, FILE_PATH)
print(content)