# Simple Youtube Scraper

I built this using Selenium. You can use this to scrape Youtube comments without resorting to Youtube API. This scraper is neither slow nor fast, but it certainly will get the job done.

The scraper's main feature is that it can run multiple instances of the (headless) webdriver in parallel. This is useful if you want to scrape comments using multiple video URLs.

The configuration is simple. Inside the scraper_yt_comment.py file, you can insert the URL(s) inside the 'URL' list. The parallelizer(?) will automatically detect the number of URLs and open that many instances of webdriver when you run it.

Another important thing you should configure is 'SCROLL_NUMBERS'. This will determine how many comments the webdriver will scrape from each URL. For reference, 100 scrolls will result in around 1500 comments being scraped per URL and 10 scrolls will give you around 150-170 comments.

This scraper outputs 1 csv file per url inserted.

To use this, clone this repository to some directory, create a virtual environment and install all the required libraries using requirements.txt, and run this script.
