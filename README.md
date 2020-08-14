# YouTube caption translator

This script allows you to leverage both the YouTube and Deepl API to:
1.  Download English captions from a YouTube video.
2.  Translate these into any language Deepl supports.
3.  Upload the translated captions to the YouTube video.

## Requirements

    -Deepl API authentication key
    -YouTube API Oauth authentication credential file(json)

### Deepl API authentication key

A DeepL API authentication key can be obtained here: (https://www.deepl.com/pro#developer)

You need the plan "For developers" that at this time of writing\(August 2020) costs:
    -€4,99 per month for connectivity
    -€20.00 per 1.000.000 translated characters

### YouTube API Oauth authentication credential file(json)

You need a YouTube API Oauth authentication credential file(json). To obtain one please follow instructions here: (https://developers.google.com/youtube/v3/quickstart/python)