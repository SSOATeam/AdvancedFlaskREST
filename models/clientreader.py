      import urllib, json
      startDate = ""
      endDate = ""
      url = "https://api.thingspeak.com/channels/1064835/feeds.json?api_key=NXFNWLO0P5QWMEKS&start=2020-05-23%2002:15:00&end=2020-05-23%2002:16:00"
      response = urllib.urlopen(url)
      data = json.loads(response.read())
      print data