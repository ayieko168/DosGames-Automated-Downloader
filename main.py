
import os
import urllib.request
from bs4 import BeautifulSoup
import urllib.request
import shutil

destination = r"C:\Users\royal state\Downloads"
page_to_download = "2"
os.chdir(destination)
game_site_links = []
zip_file_url_links = []

url = "https://www.dosgames.com/listing.php?sortby=popular&sterms2=&titlesonly=on&cat=all&tag=&license=all&year=all&filesize=all&developer=all&publisher=all&page={}".format(page_to_download)

print(url)

hdr = {"User-Agent": "Mozila/5.0"}
req = urllib.request.Request(url, headers=hdr)
page = urllib.request.urlopen(req)

# get the links to the individual game download sites

soup = BeautifulSoup(page, "html.parser")
so = soup.find_all("div", {"class": "col-md-4"})

for link in so:
    game_link = link.find("a").get("href")

    # real site format :: https://www.dosgames.com/game/doom/
    real_site_link = "https://www.dosgames.com{}".format(game_link)
    # print(real_site_link)

    # add all links to a list
    game_site_links.append(real_site_link)

print(game_site_links)

# get the zip link to each game download link

for url2 in game_site_links:
    req = urllib.request.Request(url2, headers=hdr)
    page = urllib.request.urlopen(req)

    soup = BeautifulSoup(page, "html.parser")
    # get the download link to each game
    so1 = soup.find_all("a", {"class": "btn btn-download"})[0].get("download")
    # print(so1)

    # real site format :: https://www.dosgames.com/files/DOSBOX_DUKE3D.ZIP
    # re-formatting the link to a url

    # zip file download link
    zip_file_url = "https://www.dosgames.com/files/{}".format(so1)
    # print(zip_file_url)
    zip_file_url_links.append(zip_file_url)

# download the zip file to downloads destination


for link in zip_file_url_links:

    try:
        print(link)
        file_name = "{}.{}".format(link.split("/")[-1].replace("-", "_").upper(), "zip")

        print("destination :: {}".format(file_name))
        print("downloading :: {}".format(file_name))

        # Download the file from `url` and save it locally under `file_name`:
        req = urllib.request.Request(link, headers=hdr)
        with urllib.request.urlopen(req) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

        print("done downloading {}".format(file_name))
    except Exception as e:

        print("Error :: {}".format(e))
        continue

















