import os
import io
import requests
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaFileUpload
#TODO: Fill in Youtube API Oauth authentication credential file(json). Should be in same the same folder as the script.
client_secrets_file = 'client_secret_xxxxxxxxxxxx-53fdqpkxt7oxi0bhhb4n3it06e07pb6d.apps.googleusercontent.com.json'
#TODO: Enter your Deepl API authentication key below.
deeplkey='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
#TODO: Put in the video ID for the video that you want to process. This ID can be derived from the video URL.
youtubevideo = 'fregObNcHC8'
#TODO: Choose desired ouput languages. Current supported languages by Deepl are:
# - "DE" - German
# - "EN" - English
# - "FR" - French
# - "IT" - Italian
# - "JA" - Japanese
# - "ES" - Spanish
# - "NL" - Dutch
# - "PL" - Polish
# - "PT" - Portuguese (all Portuguese varieties mixed)
# - "RU" - Russian
# - "ZH" - Chinese
#Example for German and French: ['DE','FR']
outputlanguages = ['DE','FR','IT','JA','ES','NL','PL','PT','RU','ZH']
#TODO: Set below value to True if you want to remove existing non-English captions otherwise set to False. 
# This is required if you're replacing existing captions because the API does allow you to overwrite.
removenonenglish = False

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
api_service_name = "youtube"
api_version = "v3"

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)
# Grab caption ID from video
request = youtube.captions().list(
    videoId=youtubevideo,
    part="snippet"
)
captionid = ''
response = request.execute()
for i in response['items']:
    if i['snippet']['language'] == 'en':
        captionid = i['id']
# Download caption file.
request = youtube.captions().download(
    id=captionid
)
fh = io.FileIO('captions_EN.svb', 'wb')
download = MediaIoBaseDownload(fh, request)
complete = False
while not complete:
    status, complete = download.next_chunk()
# Read caption file
with open ('captions_EN.svb', "r") as myfile:
    input=myfile.readlines()
# Translate fucntion
def translate(langout):
    deepl_url = 'https://api.deepl.com/v2/translate?'
    data = {
        'auth_key' : 'faf44193-dec3-780a-f7dd-d20a853de4ed',
        'text' : input,
        'source_lang' : 'EN',
        'target_lang' : langout 
    }
    response = requests.post(deepl_url, data = data)
    results = json.loads(response.text)
    file = open('captions_'+langout+'.sbv', 'w' ,encoding='utf-8')
    for line in results['translations']:
        file.write(line['text'])
    file.close()
# Remove existing non-English translation
if removenonenglish == True:
    request = youtube.captions().list(
        videoId=youtubevideo,
        part="snippet"
    )
    response = request.execute()
    for i in response['items']:
        if i['snippet']['language'] == 'en':
            print(i['snippet']['language'])
            print(i['id'])
        else:
            delrequest = youtube.captions().delete(
                id=i['id']
            )
            delrequest.execute()
# Create and upload translation files.
for l in outputlanguages:
    translate(l)
    request = youtube.captions().insert(
        part='snippet',
        body={
          'snippet': {
            'language': l,
            'name': '',
            'videoId': 'bt7K3X5cG60',
            'isDraft': False
          }
        },
        media_body=MediaFileUpload('captions_'+l+'.sbv')
    )
    response = request.execute()
    print(response)