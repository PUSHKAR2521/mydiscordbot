import os
import discord
from discord.ext import commands
import moderation
import logmodule
from keep_alive import keep_alive
import contextlib

keep_alive()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Retrieve the log channel ID from the secret
log_channel_id = int(os.getenv("LOG_CHANNEL_ID"))

bad_words = ["badword1", "badword2", "badword3"]


@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  
  if message.content.lower() in ["hello", "hy", "hi", "hii", "hlo"]:
    await message.channel.send(
        f'Hello Kya Loge Chai,  Coffee, Lemon Tea Ya Fir Dudh?{message.author.mention}!'
    )

  if message.content.lower() in ["chai", "coffee", "lemon tea", "dudh"]:
    await message.channel.send(
        f'To Jao Kudh janake Pilo and Hame bhi pila do {message.author.mention}!'
    )

  if message.content.lower() in ["ok"]:
    await message.channel.send(f'Hmm {message.author.mention}!')

  if moderation.check_caps_spam(message):
    await logmodule.log_moderation_action(bot, message, "Caps Spam")
    try:
      await message.delete()
    except discord.NotFound:
      pass
    await message.channel.send(
        f"{message.author.mention}, please avoid excessive caps usage.")

  if moderation.check_link_spam(message):
    await logmodule.log_moderation_action(bot, message, "Link Spam")
    try:
      await message.delete()
    except discord.NotFound:
      pass
    await message.channel.send(
        f"{message.author.mention}, please do not post links in this channel.")

  await bot.process_commands(message)


try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  bot.run(token)
except discord.HTTPException as e:
  if e.status == 429:
    print(
        "The Discord servers denied the connection for making too many requests"
    )
    print(
        "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
    )
  else:
    raise e

  print()
