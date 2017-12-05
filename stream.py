from twython import TwythonStreamer

from auth import (
      consumer_key,
      consumer_secret,
      access_token,
      access_token_secret
  )

 
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            twittertext = data['text']
            print(twittertext)
            if "forward" in twittertext:
                print("go fwd")
            elif "back" in twittertext:
                print("go back")
            elif "left" in twittertext:
                print("go left")
            elif "right" in twittertext:
                print("go right")
                


stream = MyStreamer(
      consumer_key,
      consumer_secret,
      access_token,
      access_token_secret
  )

print("stream created")
stream.statuses.filter(track='#brumbot')    
print("stream filtering")
