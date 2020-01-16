import requests
from bs4 import BeautifulSoup

for i in ("", 2, 3, 4, 5, 6, 7):
    scrap_url = "https://www.cnet.com/more-news/" + str(i)
    res = requests.get(scrap_url)
    html = res.text
    mrk = BeautifulSoup(html, "html.parser")

    dataset = {}

    story_tags = mrk.find_all("div", class_='col-8 item')
    for story_line in story_tags:
        # Block below collects the latest stories posted
        stories = story_line.find_all("h3")
        for story in stories:
            # print(story.text)
            dataset["story"] = story.text

        # Block below gives the url for article
        link_tag = story_line.findAll("a", class_="col-6")
        url = ""
        for link in link_tag:
            # print(link['href'])
            url = "https://www.cnet.com" + str(link['href'])
        # print(url)
        dataset["link"] = url

        # Block below collects the author's name
        authors = story_line.findAll("a")
        author = ""
        for list_atags in authors:
            # print(list_atags.text)
            author = str(list_atags.text)
        # print(author)
        dataset["author"] = author

        # Block below collects the information for topic
        topics = story_line.findAll(class_="topicLink")
        for topic in topics:
            # print(topic.text)
            dataset["topic"] = topic.text

        # Block below displays a dictionary of all collected information
        print(dataset)



# collect 100 entries
# collect user, category, stories, headline, time-updated, Data-source, link, Position
# Build a data model
