# YouTube caption translator

This script allows you to leverage both the YouTube and Deepl API to:
1.  Download English captions from a YouTube video.
2.  Translate these into any language Deepl supports.
3.  Upload the translated captions to the YouTube video.

# 1.   Requirements

- Deepl API authentication key
- YouTube API Oauth authentication credential file(json)
- Python 3

## 1.1 DeepL API authentication key

A DeepL API authentication key can be obtained here: (https://www.deepl.com/pro#developer)

You need the plan "For developers" that at this time of writing\(August 2020) costs:

- €4,99 per month for connectivity
- €20.00 per 1.000.000 translated characters

## 1.2 YouTube API Oauth authentication credential file(json)

You need a YouTube API Oauth authentication credential file(json). To obtain one please follow instructions here: (https://developers.google.com/youtube/v3/quickstart/python)

## 1.3 Python 3

Python 3 has to be installed. It can be downloaded here: (https://www.python.org/downloads/)

# 2.   How to use it

- Install required python modules
- Edit script variables
- Run the script

## 2.1 Install required python modules

A couple of python modules are required to run the script. Please install them using this command:

`pip3 install --upgrade google-auth-oauthlib google-auth-httplib2 google-api-python-client requests`

## 2.2 Edit script variables

A couple of variables in the script need to be adjusted. You can use your prefered text editor for this although I recommend [Visual Studio Code](https://code.visualstudio.com/download). The variables can be found in the beginning of the script.

### Onetime variables

These variables need to be edited only the first time you run the script:

**client_secrets_file**
Here you need to fill in the name of your Youtube API Oauth authentication credential file(json) which you aquired in 1.2. This file should be put in same the same folder as the script.

`client_secrets_file = 'client_secret_xxxxxxxxxxxx-53fdqpkxt7oxi0bhhb4n3it06e07pb6d.apps.googleusercontent.com.json'`

**deeplkey**
Here you need to enter your Deepl API authentication key which you aquired in 1.1.

`deeplkey='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'`

### Everytime variables

**youtubevideo**
Here you need to fill in the YouTube video ID. This id can be derived from the video url. They are the bold characters from this example: www.youtube.com<n/>/watch?v=**fregObNcHC8**

`youtubevideo = 'fregObNcHC8'`

**outputlanguages**
Here you choose the output languages you want to the video to be translated into. These languages have to be supported to DeepL ofcourse. At his time of writing (August 2020) these languages are supported:
- "DE" - German
- "EN" - English
- "FR" - French
- "IT" - Italian
- "JA" - Japanese
- "ES" - Spanish
- "NL" - Dutch
- "PL" - Polish
- "PT" - Portuguese (all Portuguese varieties mixed)
- "RU" - Russian
- "ZH" - Chinese

`outputlanguages = ['DE','FR','IT','JA','ES','NL','PL','PT','RU','ZH']`

**removenonenglish**
Set below value to True if you want to remove existing non-English captions otherwise set to False. This is required if you're replacing existing captions because the API does allow you to overwrite.

`removenonenglish = False`

## 2.3 Run the script

When everything is setup you can run the script.
- In Visual Studio Code you press the green "play" button in the top right.
- From a commandline/terminal you can execute the script using" `python translatev3.py`

1.  After execusting the script it will display a message like this:

`Please visit this URL to authorize this application:` `https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=708070221486-53fdqpkpt7o6i03hhv4ndit06e07pb6d.appsgoogleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fyoutube.force-ssl&state=lHUus8DRFhqdYsmh6wcbFu7UU7JPRKprompt=consent&access_type=offline`
`Enter the authorization code:`

2.  Open the URL with your browser and authenticate with YouTube. 
3.  Copy the authorization code, paste it after "Enter the authorization code:" and press enter.