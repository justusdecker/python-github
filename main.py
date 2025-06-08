"""

Get HTML

FETCH:
https://github.com/justusdecker?tab=repositories

FROM:
user-repository-list

title
description


"""
from requests import get as rqget
from bs4 import BeautifulSoup
from json import dumps,loads

def cret(text: str, color: tuple[int,int,int]) -> None:
    color = hex_to_rgb(color)
    return f"\033[38;2;{color[0]};{color[1]};{color[2]}m{text}\033[39m"

def hex_to_rgb(text: str) -> tuple[int,int,int]:
    return int(text[1:3],16),int(text[3:5],16),int(text[5:7],16)

class DataManagement:
    def json_walk(js: dict,path:str):
        actual_js = js
        for sub in path.split('/'):
            if not actual_js: return actual_js
            actual_js = actual_js.get(sub,{})
        return actual_js
            
    def write_n(file_path: str,data:str) -> None:
        
        with open(file_path,'w') as file:
            file.write(data)
    def write(file_path: str,data:dict | list) -> None:
        style = 'style="background-color:#242424;"'
        p_style = 'style="color:#FFFFFF;"'
        data = f"<html><body {style}><p {p_style}>{dumps(data,indent = 4).replace('\n','\n<br>')}</p></body></html>"
        with open(file_path,'w') as file:
            file.write(data)
            
class GitHubAPI:
    
    def get_user_repositorys(user: str) -> dict:
        html = rqget(f"https://github.com/{user}?tab=repositories")
        
        bs = BeautifulSoup(html.content,'html.parser')
        bs_1 = bs.find(id = "user-repositories-list")
        bs_2 = bs_1.find_all(attrs={"class":"color-border-muted"})
        
        ret = []
        all_stars = 0
        all_commits = 0
        for i in range(len(bs_2)):
            
            name = bs_2[i].find(attrs={"itemprop":"name codeRepository"})# text
            print(f"fetching repo:  {name.text.lstrip() if name is not None else 'FAILURE'}")
            description = bs_2[i].find(attrs={"itemprop":"description"})# text
            
            repo_lang_color = bs_2[i].find(attrs={"class":"repo-language-color"})# .attrs['style'].split(' ')[1]
            
            lang = bs_2[i].find(attrs={"itemprop":"programmingLanguage"})# text
            name = name.text.lstrip() if name else "undefined"
            description = description.text.strip() if description else "undefined"
            repo_lang_color = repo_lang_color.attrs['style'].split(' ')[1].lstrip() if repo_lang_color else "#000000"
            lang = lang.text.lstrip() if lang else "undefined"
            
            # get the license, stars, forks & last updated from repo site
            
            # get repo details
            
            repo_data = GitHubAPI.get_repository(user,name)
            all_stars += int(repo_data['stars'])
            all_commits += int(repo_data['commits'])
            current = {
                'name': name,
                'lang': lang,
                'repo_lang_color': repo_lang_color,
                'description': description,
                'stars': repo_data['stars'],
                'langs': repo_data['langs'],
                'commits': repo_data['commits'],
                'last_commit_id': repo_data['last_commit_id']
            }
            ret.append(current)
        return {
            'user': user,
            'all_stars': all_stars,
            'all_commits': all_commits,
            'repo': ret
        }
        
        
    def get_repository(user:str,repo:str):
        html = rqget(f"https://github.com/{user}/{repo}")
        bs = BeautifulSoup(html.content,'html.parser')
        ustar = bs.find(id = "repo-stars-counter-unstar")
        star = bs.find(id = "repo-stars-counter-star")
        langs = [] 
        for lang_element in bs.find_all(attrs={'data-ga-click':"Repository, language stats search click, location:repo overview"}):
            color = lang_element.find(attrs={'class':'octicon'}).attrs['style'].split(':')[1].replace(';','').lstrip()
            temp = [p.text for p in lang_element.find_all('span')]
            temp.append(color)
            langs.append(temp)
        for element in bs.find_all(attrs={"class":"fgColor-default"}):
            if 'Commit' in element.text:
                commits = int(element.text.split(' ')[0])
                break
        else:
            commits = -1
        element = bs.find(attrs={"data-testid":"latest-commit-details"})
        c = 0
        last_commit_id = ""
        for a in bs.find_all('script',attrs={"data-target":"react-partial.embeddedData"}):
            c += 1
            #print(a.text)
            e = loads(a.text)
            val = DataManagement.json_walk(e,'props/initialPayload/refInfo/currentOid')
            if val: last_commit_id = val[:7]
        """
        tags in class f6 / sub a tags
        license in initialPayload
        forks
        last commit text
        """
        if star:
            stars = star.text
        else:
            stars = ustar.text
        #if stars is None:
        #    stars = 0
        return {
            'stars': stars,
            'langs': langs,
            'commits': commits,
            'last_commit_id': last_commit_id
        }


gur = GitHubAPI.get_user_repositorys("justusdecker")
print(gur)
#gr = GitHubAPI.get_repository("justusdecker",'pygame-engine')
DataManagement.write("test.html",gur)
print(gur)