#config
songAllowedLength = 12
responses = [
  "I Wuv Uh", "Henloo", "This is a random A** response", "Made by causticfartz",
  "Do you know that rabbits live in burrows",
  "I am a bot just like you in valorant", "Damn, I'm hot",
  "Go Study! how long are you gonna play?",
  "Try Raga bot 1.0 (P.S: its not good but but OK)",
  "Shower Thought: Siege is a bad game", "UwU", "*˚*(ꈍ ω ꈍ).₊̣̇", "Sleepy AF",
  "( ｡ᵘ ᵕ ᵘ ｡)", "( ͡o ꒳ ͡o )", "Bad plug but im a bot made by causticfartz. I call him DADDY", "$help"
]

playingList = ["Life at hardcore mode","with Daddy Caustic","with Fembois","with naive people","$help","with myself","with my code","Minecraft","Spotify","Soundcould","Pokemon","Music for you","Valorant","like a bot", "on Stereo","World strategies","a buggy Bethesda game","with my Bot-ussy","Dinosaur game on chrome","with feelings",""]
replit_url = "https://replit.com/@V-sivakrishnasi"
bot_colour = 0x4cb399
bot_name = "Raga Bot 2.0"
bot_icon = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR33565vSTB7gHLA0vPIo9KiZNp2ocgY3SvRbUyro0&s"
TypingSleepTimer=3
joke_blacklist = ['nsfw', 'racist']
Activity="$help"

#ydl opts
Song_bitrate = 320
ydl_opts = {
  'format': 'bestaudio',
  'preferredcodec': 'mp3',
  'preferredquality': '192',
  'verbose': True,
  'retries': 2
}
ydl_opts2 = {'format': 'bestaudio'}
FFMPEG_OPTS = {
  'before_options':
  '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
  'options': '-vn'
}

#help
help_join = "- Joins the requestor channel"
help_leave = "- Bot Will leave the channel"
help_skip = "- Bot will skip the song"
help_stop = "- Bot will stop playing music."
help_halt = "- Bot will fully stop playing music."
joke_help = "- Its gives a random Joke. ($joke)"
test_help = "- This is a test function what are you expecting? LMAO"
play_help = "- Plays the song requested (ex: $play puli tiger)"
help_queue = "- Shows the songs queue."
help_ClearQueue="- clears the queue"
help_fix="- (Preview)kill the bugs!!! Kill em all!"


#error messages
songLenghtError = "The song exceeds the allowed duration."
auth_not_connected = "Please join a voice channel"
NoSongInQ="The queue is empty 🤷‍♂️"

#Debug messages
Song_exists = "[Debug] The Song exists in the local storage."
song_isDownloading = '[Debug] The Song is being Downloaded'
fix="Bot has been fixed"

#BIN

#discord.opus.load_opus("/home/runner/Raga-20/venv/lib/python3.10/site-packages/discord/opus.py")

#await ctx.voice_client.play(discord.FFmpegOpusAudio(f'./Storage/{id}.mp3', bitrate=Values.Song_bitrate))

#ctx.voice_client.play(FFmpegPCMAudio(result_dict['link'],Values.FFMPEG_OPTS), after =lambda t: print("Finished", t))
