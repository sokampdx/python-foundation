import urllib

def read_text():
  quotes = open("/Users/anthonyso/Documents/programs/udacity/python-foundation/movie_quotes.txt")
  content = quotes.read()
  print(content)
  quotes.close()
  check_profanity(content)

def check_profanity(text):
  connect = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
  response = connect.read()
  print(response)
  connect.close()

read_text()
