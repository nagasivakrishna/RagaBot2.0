import os
import discord
import time
from discord.ext import commands
import logging
import Response
import Values
import player
from jokeapi import Jokes
import queue
import asyncio
import random
from keep_alive import keep_alive

my_secret = os.environ['DiscordToken']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$',
                   intents=intents,
                   activity=discord.Game(name=Values.Activity),
                   status=discord.Status.online,
                   description="Listening to $help command")

handler = logging.FileHandler(filename=f'LOGS/{time.ctime()}.log',
                              encoding='utf-8',
                              mode='w')
last_run = time.ctime()
print(last_run)
q = queue.Queue()
songs_q = []


#@bot.command(help=Values.test_help)
#async def test2(ctx, *arg):
#  file = open("queue_persistent.txt","r")
#  for i in file:
#    await play(ctx, i)

@bot.command(help=Values.test_help)
async def test(ctx, *arg):
  passed_text = " ".join(arg)
  await ctx.send(embed=Response.CreatEmbed(passed_text))


@bot.command(help=Values.joke_help)
async def joke(ctx):
  j = await Jokes()
  joke = await j.get_joke(blacklist=Values.joke_blacklist)
  await ctx.send(embed=Response.JokeSetup(setup=joke.get('setup')))
  time.sleep(3)
  await ctx.send(embed=Response.JokeDelivery(delivery=joke.get('delivery')))


@bot.command(help=Values.play_help)
async def play(ctx, *args):
  song_requested = " ".join(args).strip()
  
  
  if song_requested == "" and ctx.voice_client is not None:
    if ctx.voice_client.is_playing() is False:
      await resume(ctx)
    else:
      ctx.voice_client.play(q.get())
      temp=songs_q.pop(0)
    return 0
  elif song_requested == "" and ctx.voice_client is None:
    await skip(ctx)

  
  
  await bot.change_presence(
    activity=discord.Game(random.choice(Values.playingList)))
  
  
  
  await join(ctx)
  if ctx.voice_client.is_playing() != True:
    result_dict = player.Search(song_requested).result()['result'][0]
    #print(result_dict)
    #print(result_dict['duration'][:-3])
    #print("\n" + result_dict['id'])
    if int(result_dict['duration'][:-3]) < Values.songAllowedLength:
      link = result_dict['link']
      id = result_dict['id']
      async with ctx.typing():
        player.download_func(link, id)
        await asyncio.sleep(Values.TypingSleepTimer)
      await ctx.send(embed=Response.SongResponse(result_dict))
      await join(ctx)
      source = await discord.FFmpegOpusAudio.from_probe(f'./Storage/{id}.mp3')
      ctx.voice_client.play(source, after=lambda t: asyncio.run_coroutine_threadsafe(ctx.voice_client.play(q.get(0), bot.loop)))
      print(f"[Debug] Playing {id}")
    else:
      await ctx.send(embed=Response.Songlenthexceeded())

  else:
    result_dict = player.Search(song_requested).result()['result'][0]
    if int(result_dict['duration'][:-3]) < Values.songAllowedLength:
      result_dict = player.Search(song_requested).result()['result'][0]
      link = result_dict['link']
      id = result_dict['id']
      async with ctx.typing():
        player.download_func(link, id)
        await asyncio.sleep(Values.TypingSleepTimer)
      await ctx.send(embed=Response.SongResponse(result_dict))
      source = await discord.FFmpegOpusAudio.from_probe(f'./Storage/{id}.mp3')
      q.put(source)
      songs_q.append(result_dict['title'])
    else:
      await ctx.send(embed=Response.Songlenthexceeded())
    print(
      f"[Debug] added to queue. Total songs in queue: {q.unfinished_tasks}\n\n({songs_q})\n\n"
    )


@bot.command(help=Values.help_join)
async def join(ctx):
  if ctx.message.author.voice is None:
    await ctx.send(embed=Response.Auth_non_connected())
  elif ctx.voice_client is None:
    await ctx.message.author.voice.channel.connect(reconnect=True,
                                                   self_deaf=True)
  elif ctx.voice_client.channel == ctx.message.author.voice.channel:
    pass

  else:
    await ctx.voice_client.disconnect()
    await ctx.message.author.voice.channel.connect(reconnect=True,
                                                   self_deaf=True)


@bot.command(help=Values.help_leave)
async def leave(ctx):
  await ctx.voice_client.disconnect()


@bot.command(help=Values.help_skip)
async def skip(ctx):
  ctx.voice_client.stop()
  await ctx.send(embed=Response.ShortResponse(f"Now playing {songs_q.pop(0)}"))
  ctx.voice_client.play(q.get(0))
  print("[debug] bot skipped song")


@bot.command(help=Values.help_stop)
async def pause(ctx):
  ctx.voice_client.pause()
  print("[debug] bot paused")


@bot.command(help=Values.help_stop)
async def resume(ctx):
  ctx.voice_client.resume()
  print("[debug] bot resumed")

@bot.command(help=Values.help_halt)
async def stop(ctx):
  ctx.voice_client.stop()

@bot.command(help=Values.help_queue)
async def queue(ctx):
  await ctx.send(embed=Response.ShowQueue(songs_q))


@bot.command(help=Values.help_ClearQueue)
async def clear(ctx):
  q.queue.clear()
  songs_q.clear()
  await ctx.send(embed=Response.ShortResponse("Your Queue has been cleared"))


@bot.command(help=Values.help_fix)
async def fix(ctx):
  q.queue.clear()
  songs_q.clear()
  await leave(ctx)
  print(Values.fix)

keep_alive()
bot.run(my_secret, log_handler=handler, log_level=logging.INFO)
