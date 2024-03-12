import discord
import random
import Values


def SongResponse(result_dict):
  #if len(passed_text) == 0:
  #  passed_text = "Nothing 🤷‍♂️"
  embed = discord.Embed(title=result_dict['title'],
                        url=result_dict['link'],
                        description=f"Duration: {result_dict['duration']}",
                        color=Values.bot_colour)
  embed.set_author(name="Song added to queue.", icon_url=Values.bot_icon)
  embed.set_thumbnail(url=result_dict['thumbnails'][0]['url'])
  return embed


def ShowQueue(songs_q):
  response = "Nothing in queue 🤷‍♂️"
  if len(songs_q) > 0:
    response = ""
    for i in songs_q:
      response += f"{i}\n"

  embed = discord.Embed(title=f"Songs Queue: Total songs {len(songs_q)}",
                        description=response,
                        color=Values.bot_colour)
  return embed


def CreatEmbed(passed_text):

  if len(passed_text) == 0:
    passed_text = "Nothing 🤷‍♂️"

  embed = discord.Embed(title=random.choice(Values.responses),
                        url=Values.replit_url,
                        description=f" you said {passed_text}",
                        color=Values.bot_colour)
  embed.set_author(name=Values.bot_name, icon_url=Values.bot_icon)
  embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
  return embed


def JokeSetup(setup):
  embed = discord.Embed(title=setup, url=Values.replit_url, description="")
  embed.set_author(name=Values.bot_name, icon_url=Values.bot_icon)
  return embed


def JokeDelivery(delivery):
  embed = discord.Embed(description=delivery)
  return embed


def Auth_non_connected():
  embed = discord.Embed(description=Values.auth_not_connected)
  return embed


def Songlenthexceeded():
  embed = discord.Embed(description=Values.songLenghtError)
  return embed


def NoSongInQueue():
  embed = discord.Embed(description=Values.NoSongInQ)
  return embed

def ShortResponse(text):
  embed = discord.Embed(description=text)
  return embed
