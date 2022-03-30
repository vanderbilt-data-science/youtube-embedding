# CREATED BY SAAD AKHTAR
# To make this code work you must do three pipinstall the first is 
#
# pip install youtube-transcript-api
# pip3 install requests_html bs4
# pip install beautifulsoup4
#
# These are the exact pip installs that you can copy and paste to your terminal
# Make sure you have python installed with pip feature if you dont know how to do that 
# follow this link 
#
# https://www.alphr.com/pip-is-not-recognized-as-an-internal-or-external-command/

from turtle import clear
from youtube_transcript_api import YouTubeTranscriptApi
import youtube_transcript_api

from requests_html import HTMLSession 
from bs4 import BeautifulSoup as bs # importing BeautifulSoup

# READ_ME
# THIS IS THE CODE FOR ONE VIDEO, IF WE WANT TO DO ALL VIDEOS
# MAKE THE CODE BELOW A FUNCTION THAT IS CALLED IN A LOOP AND IS UPDATING
# THE vid_id VARIABLE, CAN DO IF NEED


# THIS IS THE CODE FOR THE DESCRIPTIONS/TITLES

# unique id for the video
vid_id = "zb9q0eKoIo4"

# url needed
video_url = "https://www.youtube.com/watch?v=" + vid_id
# init an HTML Session
session = HTMLSession()
# get the html content
response = session.get(video_url)
# execute Java-script
response.html.render(sleep=1)
# create bs object to parse HTML
soup = bs(response.html.html, "html.parser")

file = open ("test.txt", 'w')

# writing title to the file
# file.write(soup.find("meta", itemprop="name")["content"])
# file.write("\n")

# writing description to the file
file.write(soup.find("meta", itemprop="description")['content'])
file.write("\n")


# THIS IS THE CODE FRO THE TRANSCRIPTS

data = YouTubeTranscriptApi.get_transcript(vid_id)

transcript = ''
for value in data: 
    for key, val in value.items():
        if key == 'text':
            transcript += val 

splitlist = transcript.split(' ')
final_tra = ' '.join(splitlist)

# writing transcript to the file
file.write(final_tra)
file.write("\n\n")
file.close()