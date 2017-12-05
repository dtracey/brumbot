import explorerhat
from time import sleep
from twython import TwythonStreamer, Twython
from picamera import PiCamera
from random import randint
from auth import (
      consumer_key,
      consumer_secret,
      access_token,
      access_token_secret
  )
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )
#drive forward
def wheelfwd():
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.forward(100)
    sleep(3)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
#turn left
def wheelleft():
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.backward(100)
    sleep(5)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    
#turn right
def wheelright():
    explorerhat.motor.two.forward(100)
    explorerhat.motor.one.backward(100)
    sleep(5)
    explorerhat.motor.two.stop()
    explorerhat.motor.one.stop()
#reverse
def wheelbwd():
    explorerhat.motor.one.backward(100)
    explorerhat.motor.two.backward(100)
    sleep(3)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
#photo function
def takephoto():
    num = randint(0,100000)
    camera.start_preview(alpha=192)
    sleep(3)
    camera.capture("/home/pi/Robot{}.jpg".format(num))
    camera.stop_preview()
    return num    

#tweet function
def send_tweet():
    print('function called')
    num = takephoto()
    message = "Brumbot is here! - message id = " + str(num)
    output = "/home/pi/Robot{}.jpg".format(num)
    with open(output, 'rb') as photo:
        response = twitter.upload_media(media = photo)
        twitter.update_status(status = message, media_ids = [response['media_id']])
    print(response)

#reads twitter stream looking for commands    
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            twittertext = data['text']
            print(twittertext)
            if "forward" in twittertext:
                print("forward")
                wheelfwd()
                send_tweet()
            elif "back" in twittertext:
                print("go back")
                wheelbwd()
                send_tweet()
            elif "right" in twittertext:
                print("go right")
                wheelleft()
                send_tweet()
            elif "left" in twittertext:
                print("left")
                wheelright()
                send_tweet()
            
stream = MyStreamer(
      consumer_key,
      consumer_secret,
      access_token,
      access_token_secret
  )
camera = PiCamera()




#explorerhat.touch.four.pressed(send_tweet)




##explorerhat.touch.one.pressed(wheelfwd)
##explorerhat.touch.two.pressed(wheelleft)
##explorerhat.touch.three.pressed(wheelright)
##explorerhat.touch.four.pressed(wheelbwd)

 

                


#what we're looking for in twitter feed

print("stream created")
stream.statuses.filter(track='#brumbot')    
print("stream filtering")

