# Python studies
============

Yes, Yes. Yet another new year resolution if you want to call it that. It's just about time for me to get acclimated to Python.
I find python being quite a nice language but I never coded any real application, so this is the beginnings.

## Extra
The list below is to count the days I'm coding in python but not in this repository.

### day 13
Started a simple python app hosted on Heroku to sale my motorcycle
[commit](https://github.com/weblancaster/fz09-sale/commit/64baaabb2b03702a03a243d26cb5aeca87d7c79c)

### Day 14
Started using Flask/Jinja2 for cache busting, and setup requirements
[commit](https://github.com/weblancaster/fz09-sale/commit/79e857a4bc5332583fa809b98a684d0ddc07f240)
[commit](https://github.com/weblancaster/fz09-sale/commit/f1c8c3c475ed927baffcd42ba0596bd20c64abec)

### Day 17
Migrating solshal.com scrapping stack from JS (Scraperjs) to a service where I'm using Python (Scrapy)

### Day 18
After some experimentation and research I have decided that Scrapy is much more robust than what I need, now I'm experimenting with BeautifulSoup4 and seems like that's what I'm going with for now

### Day 19
Continued using BeautifulSoup4 and did some more testing to make sure will perform as todays Nodejs scrapper or beter

### Day 20
Finished up writing the solshal-scrapper service in Python using BeautifulSoup4, next I will move it to Docker

### Day 21
I haven't been feeling well since last night, painful headache that kept annoying me all day.
For that reason I'm not spending too much time on computer tonight and decided to only setup the virtualenv  for solshal-scrapper service which was something I haven't done yet.

### Day 22
Today I dockerized the solshal-scrapper written in python and started the integration solshal-app and solshal-scrapper

### Day 23
Kept working on the integration of the services Solshal and solshal-scrapper, trying some security options and going through some cases python the scrapper can fail
and how the main will handle the failures

### Day 24
Finished testing solshal and solshal-scrapper, added solshal-scrapper to docker and released the image on DockerHub.
Started working on solshal main docker compose file to accommodate solshal-scrapper service
