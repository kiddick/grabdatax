import cProfile
import requests

def go():
	headers = {'User-Agent': 'Mozilla/5.0'}
	r = requests.get('http://www.dotabuff.com/players/114001493/matches?page=2', headers = headers)
	# print r.content

def golist():
	s = requests.Session()
	for i in range(1, 100):
		headers = {'User-Agent': 'Mozilla/5.0'}
		# r = requests.get('http://www.dotabuff.com/players/114001493/matches?page=' + str(i), headers = headers)
		r = s.get('http://www.dotabuff.com/players/114001493/matches?page=' + str(i), headers = headers)
		# with open('htmlka' + str(i) + '.html', 'w') as of:
			# of.write(r.content)

cProfile.run('golist()')
# golist()