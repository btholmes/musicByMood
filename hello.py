import urllib
from bs4 import BeautifulSoup
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class MusicLyrics(Resource):
	def get(self):
		odd_words = ["</br>","<br>","<div>","</div>","<i>","</i>"]
		# song_artist = ""
		# song_title = ""
		url = 'http://www.azlyrics.com/lyrics/johnlegend/allofme.html'# + str(song_artist) +'/' + str(song_title) + '.html'

		#this error handling is important here becuase erros like Http 404 error can occur when the user enters non-existing
		# artist and song title and that will make your app not function well.Its always good to check for errors
		# even if it passes all tests.

		try:
			soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
			raw_lyrics_html = soup.find_all("div")
			lyrics = (str(raw_lyrics_html[21]))
			#print(lyrics)
			
			#this for loop will replace all html tags in the odd_word varaible with empty string.
			for word in odd_words:
				lyrics = lyrics.replace(str(word),"")

			intro ="This lyrics is brought to you by 'azlyrics.com' Enjoy"
		except Exception as e:
			lyrics=str(e)
		return {"song":lyrics}


api.add_resource(MusicLyrics, '/getlyrics')


if __name__ == "__main__":
	app.run(debug=True)