# Python studies
============

Yes, Yes. Yet another new year resolution if you want to call it that. It's just about time for me to get acclimated to Python.
I find Python being quite a nice language but I never wrote any real application, so this is my notes while I go trough some studies and real things I'm building with Python.

## Summary
The list of days below is to log the days I'm coding in python mainly not in this repository.
The days not logged here are in the commits.

### day 13
Started a simple python app hosted on Heroku to sell my motorcycle.
[commit](https://github.com/weblancaster/fz09-sale/commit/64baaabb2b03702a03a243d26cb5aeca87d7c79c)

### Day 14
Started using Flask/Jinja2 for cache busting, and setup requirements.
[commit](https://github.com/weblancaster/fz09-sale/commit/79e857a4bc5332583fa809b98a684d0ddc07f240)
[commit](https://github.com/weblancaster/fz09-sale/commit/f1c8c3c475ed927baffcd42ba0596bd20c64abec)

### Day 17
Migrating solshal.com scrapping stack from JS (Scraperjs) to a service where I'm using Python (Scrapy).

### Day 18
After some experimentation and research I have decided that Scrapy is much more robust than what I need, now I'm experimenting with BeautifulSoup4 and seems like that's what I'm going with for now.

### Day 19
Continued using BeautifulSoup4 and did some more testing to make sure will perform as todays Nodejs scraper or beter.

### Day 20
Finished up writing the solshal-scraper service in Python using BeautifulSoup4, next I will move it to Docker.

### Day 21
I haven't been feeling well since last night, painful headache that kept annoying me all day.
For that reason I'm not spending too much time on computer tonight and decided to only setup the virtualenv  for solshal-scraper service which was something I haven't done yet.

### Day 22
Today I dockerized the solshal-scraper written in python and started the integration solshal-app and solshal-scraper.

### Day 23
Kept working on the integration of the services Solshal and solshal-scraper, trying some security options and going through some cases python the scraper can fail
and how the main will handle the failures.

### Day 24
Finished testing solshal and solshal-scraper, added solshal-scraper to docker and released the image on DockerHub.
Started working on solshal main docker compose file to accommodate solshal-scraper service.

### Day 25
Update the docker-compose file to accommodate the changes and decided the improve and update the entire docker
infra and images dependencies.
Rewriting the scraper in python made the docker infra much simpler because the node scraper had some dependencies on native modules.

### Day 26
Went through some problems updating to latest MongoDB and connecting/linking solshal service to solshal-scraper service.
Pushed a minor change to the scraper service https://github.com/Solshal/solshal-scraper/pull/1.

### Day 27
Went back to try fixing the linking between solshal and solshal-scraper when running with docker-compose, still haven't figure it out.

### Day 28
Started looking at writing solsha-digest service in python, more especifically cron jobs in python.

### Day 29
Unit tests in python using pytest, at first I just want to run a simple test.

### Day 30
Started adding unit test to solshal-scraper using pytest and I will probably need something to mock methods,
request lib and flask lib.

### Day 33
Stayed up until late (started the day/night) fixing/improving/updating the docker-compose so the services solshal-web and solshal-scraper can communicate to each other.
I also pushed a good amount of improvements/fixes to solshal-scraper https://github.com/Solshal/solshal-scraper/pull/2.

### Day 34
Started building another service in Python for solshal.com, now bookmark importer service where users will be able to import from browsers (Chrome) to Solshal.com.
This is the setup and start https://github.com/weblancaster/solshal-bookmark-importer.

### Day 35
Started writing the code to import get the data from chrome and format to Solshal collection format