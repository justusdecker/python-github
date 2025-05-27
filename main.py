"""

Get HTML

FETCH:
https://github.com/justusdecker?tab=repositories

FROM:
user-repository-list

title
description


"""

def get_user_repositorys(user: str):
    html = rqget(f"https://github.com/{user}?tab=repositories")
    
    bs = BeautifulSoup(html.content,'html.parser')
    bs_1 = bs.find(id = "user-repositories-list")
    bs_2 = bs_1.find_all(attrs={"class":"color-border-muted"})
    
    ret = []

    for i in range(len(bs_2)):
        
        name = bs_2[i].find(attrs={"itemprop":"name codeRepository"})# text
        
        
        
        description = bs_2[i].find(attrs={"class":"color-fg-muted"})# text
        
        repo_lang_color = bs_2[i].find(attrs={"class":"repo-language-color"})# .attrs['style'].split(' ')[1]
        
        lang = bs_2[i].find(attrs={"itemprop":"programmingLanguage"})# text
        name = name.text.lstrip() if name else "undefined"
        description = description.text.lstrip() if description else "undefined"
        repo_lang_color = repo_lang_color.attrs['style'].split(' ')[1].lstrip() if repo_lang_color else "undefined"
        lang = lang.text.lstrip() if lang else "undefined"
    #lic = bs_2[i].find_all(attrs={"class":"mr-3"})[1].text
        print(f"{name} in {lang} {repo_lang_color}\n{description}\n", "*" * 25, '\n')
        #print(namerepo_lang_color,lang,name,description)

from requests import get as rqget
from bs4 import BeautifulSoup

get_user_repositorys('justusdecker')

