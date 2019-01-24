#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "ENTER YOUR ACCESS TOKEN"
access_token_secret = "ENTER YOUR ACCESS TOKEN SECRET"
consumer_key = "ENTER YOUR API KEY"
consumer_secret = "ENTER YOUR API SECRET"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

	def on_data(self, data):
		#print data
		return True

	def on_error(self, status):
		#print status

if __name__ == '__main__':
#This handles Twitter authetification and the connection to Twitter Streaming API
	l = StdOutListener()
	auth = OAuthHandler(6yr5XKUCNUpBbjPtFE4JFeoTr,tjilRifkYsrKUjP0KyzTdhJgtQYqV1U4WiaN50XQVYn05x86ud)
	auth.set_access_token(1018536585091043328-dtlyqR9TzH1yk5zlGKvPPoGtlqlPO6, 38ZbyqEdCwO8KdKZayVtr2336W3VzRoyfAuMI75TfR03j)
	stream = Stream(auth, l)

	#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
	stream.filter(track=['python', 'javascript', 'ruby'])
