import requests
class Github:
    def __init__(self):
        self.api_url="https://api.github.com"
        self.token = 'Personal access tokens'
        

    def getUser(self, username):
        response = requests.get(self.api_url+"/users/"+username)
        ##print(self.api_url+"/users/"+username)
        return response.json()

    def getRepositories(self, username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        print(self.api_url+"/users/"+username+'/repos')
        return response.json()
    
    def  createRepository(self, name):
       headers = {'Authorization': f'Token {self.token}'}

       # curl -H 'Authorization: token my_access_token'
       response = requests.post(self.api_url+'/user/repos?',headers=headers,json={
            "name": name,
            "description": "This repository was created with python commands",
            "homepage": "https://github.com/",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })

       return response.json()



github= Github()



while True:
    choice_ =input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ")
    if choice_=="4":
        break
    else:
        if choice_=="1":
            username = input("username: ")
            result=github.getUser(username)
            print(f"name: {result['name']} public repos : {result['public_repos']} follower: {result['followers']}")
        
        elif choice_=="2":
            username = input("username: ")
            result = github.getRepositories(username)
            for repo in result:
                print(repo["name"])
        elif choice_=="3":
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result) 
        else:
            print("yanlış seçim")
