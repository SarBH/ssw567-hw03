import json
import requests


def gitRepoAPI(ID):
    repoAPI = "https://api.github.com/users/" + ID + "/repos"
    repos = requests.get(repoAPI)

    userRepos = repos.json()

    repoDict = {}

    for repo in userRepos:
        print(repo["name"])
        commitsAPI = "https://api.github.com/repos/" + ID +"/" + repo["name"] +"/commits"
        commits = requests.get(commitsAPI)
        commitsContent = json.loads(commits.content.decode('utf-8'))

        # print("User ID: " + ID + " Repo name: " + repo["name"] + " Number of Commits: " + str(len(commitsContent)))

        repoDict[(str(repo["name"]))] = len(commitsContent)
    print(repoDict)
    return repoDict



if __name__ == "__main__":
    gitRepoAPI("SarBH")