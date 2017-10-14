#!/usr/bin/env python
from urllib.parse import urlparse
from urllib.request import urlopen
from os.path import expanduser
import os, sys, re, pyperclip, datetime

new = pyperclip.paste()
parsed_url = urlparse(new)
desktop = expanduser("~") + '/Desktop'

if len(sys.argv) < 2:
	if bool(parsed_url.scheme):
		print('Clipboard URL is valid.')
		url = new
	else:
		print('Stream URL need to be provided as parameter.')
		exit(0)
elif len(sys.argv) < 3:
	url = sys.argv[1]

def chatturbate_find_playlist(url):
	# connect to a URL
	website = urlopen(url)

	# read html code
	html = website.read()
	html = str(html)

	items = re.findall('https://edge(.*?)/playlist.m3u8',html,re.DOTALL)
	if '[]' in str(items):
		return False
	else:
		item = 'https://edge' + items[0] + '/playlist.m3u8'
		return item

def xhamster_find_playlist(url):
	pass

def myfreecams_find_playlist(url):
	pass

def stream(url):
	print('ffmpeg stream mp4')
	now = datetime.datetime.now()
	#format_string = '/Users/hummingbird/Desktop/moon/scripts/ffmpeg/ffmpeg_stream_mp4.sh ' + str(url)
	format_string = 'ffmpeg  -i ' + url + ' -c copy -bsf:a aac_adtstoasc ' + desktop + '/' + str(now.hour) + str(now.minute) + str(now.second) + '.mp4'
	command = str(format_string)
	os.system(command)
	return


if __name__ == '__main__':
	if 'chaturbate.com/' in url:
		m3u8 = chatturbate_find_playlist(url)
	elif 'xhamster.com' in url:
		m3u8 = xhamster_find_playlist(url)
	elif 'myfreecams.com' in url:
		m3u8 = myfreecams_find_playlist(url)

	if m3u8 is not False:
		print(m3u8)
		stream(m3u8)
	else:
		print('playlist.m3u8 not found')