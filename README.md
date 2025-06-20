# GitHub Api Webscraper Project

## Things that will be added in the future

- [x] Get all repos from a user
- [x] Get data from a specific repo
- [ ] https://github.com/justusdecker/python-github/issues/1
- [ ] https://github.com/justusdecker/python-github/issues/2
- [ ] https://github.com/justusdecker/python-github/issues/3
- [ ] https://github.com/justusdecker/python-github/issues/4
- [ ] https://github.com/justusdecker/python-github/issues/5

## Requirements

> [!IMPORTANT]
> Compatibility list
> | Software or Lib | Value |
> |-|-|
> | Python | 3.13.3 |
> | requests | 2.32.3 |
> | bs4 | 0.0.2 |
> | json | 2.0.9 |
> | OS | Windows 10 | 
> 
> Other versions may work but are not tested!

## Methods

> [!WARNING]
> Some things may be not work currently & some functions might crash!

#### Get all repositorys from a specific user

```
GitHubAPI.get_user_repositorys("{username}")
```
##### for each repository you get:
> - repo-name
> - repo-description
> - repo language color
> - all langs in percent & color
> - stars
> - all repo commits
> - last commit id
##### On top:
> - user
> - total stars
> - total commits

> [!NOTE]
> You can only get public repositories!




#### Get a repository
```
GitHubAPI.get_repository("{username}",'{repo}')
```

##### you get:
> - user
> - repo-name
> - stars
> - all repo commits
> - last commit id


## Formats
```
{
  "name": "python-github",
  "lang": "Python",
  "repo-lang-color": "#3572A5",
  "description": "undefined"
}
```
