# NewsFeed
A web application which displays currently published headlines and articles from a wide range of news sources using NewsAPI.

## Prerequisities
You need to have [Python (3.7+)](https://www.python.org/downloads/) installed to run this project

## Setup
- clone this repository
```
git clone https://github.com/bahmi/NewsFeed.git
```
-  After cloning the repo, go to its root directory and run the following command to install required packages
```
pip install -r requirements.txt
```
- Once all the packages are installed, create a `.env` file at the root directory and fill out with your 
credentials.
```
SECRET_KEY = django_secret_key
api_key = your_api_key
DEBUG = True
ALLOWED_HOSTS = localhost
```
- Finally, to run the project simply do 
```
python manage.py runserver
```

## Live Demo
Check out the live demo at [bnews.herokuapp.com](https://bnews.herokuapp.com)  
Note: The site may take a few seconds to load since it is running on a free [Heroku Dyno](https://www.heroku.com/dynos).

## Video Walkthrough
Here's a walkthrough of implementation:  

![neesfeed](./walkthrough/newsfeed.gif)

## Challenges Encountered
- Initially, the project was named 'newsportal'. But after working on it for a while, I thought 'newsfeed' sounds better. I 
went into PyCharm's refactor menu and renamed it. But when I ran it, it threw bunch of errors, did not work anymore! 
I tried few more times but it would not work. So, I googled the issue and visited few sites. Nothing made sense! After a while, I 
stumbled upon [this article](https://stackoverflow.com/questions/18293875/easy-way-to-rename-a-django-project/18293906) 
on Stack Overflow. Followed the steps but it still would not work. At this point, i had probably spent about couple of hours trying to fix the issue. Finally, I came across 
[this post](https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000792670--solved-Project-Interpreter-Error-Please-Specify-a-different-SDK-Name) 
on PyCharm community. The issue was that the new name had conflict with the previous project name in the virtual environment.
I followed the steps and removed the previous virtual environment, it resolved the issue. Software engineering is not 
really about writing code all the time. Rather, most of the time I had to do was deal with unexpected behaviour of coding environment and tools.   

- When the API was called using `sources` endpoint, it returned really long description of sources. The bootstrap cards started to appear in random sizes as there 
was no consistent length of the description. It made the homepage look terrible. I looked up for solution in google but did not know the right keywords to look for. 
Wondered around the web for a couple of hours looking for answer. Luckily, I came across 
[this article](https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#truncatechars) which described how to truncate the long description. 
Finally, the issue was resolved.

- Another issue worth mentioning is the fetched images had random height and width. Due to this, the articles page became really messy. In order to fix that I had 
to customize the bootstrap cards. I am mostly interested in the business logic side, never been great at design. It took me a few hours of looking at the screen to get it right.

- I had a huge issue deploying because the application ran perfectly on local development server but when I pushed it into heroku it started throwing errors. 
The homepage would not even load. I went through heroku CLI error logs and it showed "no web process running" message. I googled the error message and found some articles 
where they mentioned that heroku needs a Procfile specifying how we want to run it. So, I added the Procfile and pushed into heroku again. Well, it still would not work! 
The issue was that I had not added config variables in heroku. After adding the keys, I thought now it'll work smoothly. But to my utter surprise, it was not working! 
Now, I forgot to add the url of the heroku app to `ALLOWED_HOSTS`. At long last, the app was successfully deployed. It took me 4-5 hours of troubleshooting 
to get the deployment done.
 
## Things I Learned
The biggest takeaway from this project is to navigate through the unexpected issues a software engineer faces on a daily basis. I hope to 
build up on that in the future. In term of technical ability, I learned to work with API endpoints, extract data from JSON and display them on the page. 
I also picked up template inheritance. It reduced the codebase by half, will be a powerful tool for the future. 
I acquired the knowledge of deploying web application on heroku. The deployment phase was frustrating, to be honest. :-) 

## Built With
- [Django](https://www.djangoproject.com/) - Server-side Web Framework
- [pip](https://pypi.org/project/pip/) - Package Manager
- [Bootstrap](https://getbootstrap.com/) - Front-End Framework
- [PyCharm](https://www.jetbrains.com/pycharm/) - IDE
- [NewsAPI](https://newsapi.org/) - API Provider
- [JSON](https://www.json.org/) - Data-interchange Format
- [Heroku](https://www.heroku.com/) - Deployment Platform

## To Do
- Implement caching to reduce the amount of request to API 