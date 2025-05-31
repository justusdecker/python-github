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
    
class GitHubAPI:
    
    def get_user_repositorys(user: str) -> dict:
        html = rqget(f"https://github.com/{user}?tab=repositories")
        
        bs = BeautifulSoup(html.content,'html.parser')
        bs_1 = bs.find(id = "user-repositories-list")
        bs_2 = bs_1.find_all(attrs={"class":"color-border-muted"})
        
        ret = []

        for i in range(len(bs_2)):
            
            name = bs_2[i].find(attrs={"itemprop":"name codeRepository"})# text
            
            description = bs_2[i].find(attrs={"itemprop":"description"})# text
            
            repo_lang_color = bs_2[i].find(attrs={"class":"repo-language-color"})# .attrs['style'].split(' ')[1]
            
            lang = bs_2[i].find(attrs={"itemprop":"programmingLanguage"})# text
            name = name.text.lstrip() if name else "undefined"
            description = description.text.strip() if description else "undefined"
            repo_lang_color = repo_lang_color.attrs['style'].split(' ')[1].lstrip() if repo_lang_color else "#000000"
            lang = lang.text.lstrip() if lang else "undefined"
            
            # get the license, stars, forks & last updated from repo site
            current = {
                'name': name,
                'lang': lang,
                'repo_lang_color': repo_lang_color,
                'description': description
            }
            ret.append(current)
        return ret
        
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
        """
        commit count
        tags
        license
        forks
        name
        description
        last commit id
        last commit text
        """
        if star:
            stars = star.text
        else:
            stars = ustar.text
        ret = {
            'stars': stars,
            'langs': langs
        }
        print(ret)

def cret(text: str, color: tuple[int,int,int]) -> None:
    color = hex_to_rgb(color)
    return f"\033[38;2;{color[0]};{color[1]};{color[2]}m{text}\033[39m"
def hex_to_rgb(text: str) -> tuple[int,int,int]:
    return int(text[1:3],16),int(text[3:5],16),int(text[5:7],16)

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
    """
    commit count
    tags
    license
    forks
    name
    description
    last commit id
    last commit text
    """
    if star:
        stars = star.text
    else:
        stars = ustar.text
    ret = {
        'stars': stars,
        'langs': langs
    }
    print(ret)
    
def get_user_repositorys(user: str):
    html = rqget(f"https://github.com/{user}?tab=repositories")
    
    bs = BeautifulSoup(html.content,'html.parser')
    bs_1 = bs.find(id = "user-repositories-list")
    bs_2 = bs_1.find_all(attrs={"class":"color-border-muted"})
    
    ret = []

    for i in range(len(bs_2)):
        
        name = bs_2[i].find(attrs={"itemprop":"name codeRepository"})# text
        
        description = bs_2[i].find(attrs={"itemprop":"description"})# text
        
        repo_lang_color = bs_2[i].find(attrs={"class":"repo-language-color"})# .attrs['style'].split(' ')[1]
        
        lang = bs_2[i].find(attrs={"itemprop":"programmingLanguage"})# text
        name = name.text.lstrip() if name else "undefined"
        description = description.text.strip() if description else "undefined"
        repo_lang_color = repo_lang_color.attrs['style'].split(' ')[1].lstrip() if repo_lang_color else "#000000"
        lang = lang.text.lstrip() if lang else "undefined"
        
        # get the license, stars, forks & last updated from repo site
        current = {
            'name': name,
            'lang': lang,
            'repo_lang_color': repo_lang_color,
            'description': description
        }
        ret.append(current)
    return ret


#print(get_user_repositorys('justusdecker'))

gur = GitHubAPI.get_user_repositorys("justusdecker")
print(gur)
gr = GitHubAPI.get_repository("justusdecker",'pygame-engine')
print(gr)