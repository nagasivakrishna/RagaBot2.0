import youtube_dl as yt_dl
import Values
from youtubesearchpython import VideosSearch
import os


def Search(song_requested):
  search_result = VideosSearch(f'{song_requested} song', limit=1)
  return search_result


def download_func(url, id):
  if os.path.isfile(f'./Storage/{id}.mp3'):
    print(f'{Values.Song_exists} ({id})')
    return
  else:
    print(f'{Values.song_isDownloading} ({id})')
    ydl_opts = {
      'format': 'bestaudio',
      'extractaudio': True,
      'preferredcodec': 'mp3',
      'preferredquality': Values.Song_bitrate,
      'verbose': True,
      'outtmpl': f'Storage/{id}.mp3',
      'fragment_retries': 3,
      'restrictfilenames': True,
      'noplaylist': True,
      'nocheckcertificate': True,
      'ignoreerrors': False,
      'logtostderr': False,
      'quiet': True,
      'no_warnings': True,
      'default_search': 'auto',
    }

    yt_dl.YoutubeDL(ydl_opts).download([url])

    #yt_dl.YoutubeDL(ydl_opts).download([search_result.result()['result'][0]['link']])
