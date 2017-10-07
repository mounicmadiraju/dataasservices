# dataasservices
🔌📦 We're team of technical geeks with passion in building apps, data and web services on all platforms and we do Analytics using Data Science. We are mastered in Artificial Intelligence(AI), Machine Learning(ML), Deep Learning
To know more, visit our website http://www.dataasservices.com/

# Facebook-Sentiment-Analysis
Simple script to retrieve and perform Sentiment Analysis on Facebook Posts.


<b>Dependencies</b>
* facebook-sdk
* NLTK
* TextBlob
* Facebook Access Token

<b>Setup</b>

* Install NLTK: 
 - http://www.nltk.org/install.html
 
* Download the corpora files and trained model:
```bash
$ python
>>> import nltk
>>> nltk.download('all')
```

* install facebook-sdk and TextBlob:
```bash
$ sudo pip install facebook-sdk TextBlob
```

* Get your ACCESS_TOKEN:
https://developers.facebook.com/docs/graph-api/overview

<b>Usage</b>
```bash
$ python facebook-sentiment-analysis.py --access_token YOUR_ACCESS_TOKEN --profile=profilename
```

Tests for ChatterBot examples
=============================

This directory contains tests for the ChatterBot example programs
to make sure that things don't break and continue to work as
expected as changes are made to the chatterbot package.
