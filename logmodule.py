import discord
import os  # Import the 'os' module

# Retrieve the log channel ID from the secret
log_channel_id = int(os.getenv("LOG_CHANNEL_ID"))


# Logging function
async def log_moderation_action(bot,
                                target,
                                action,
                                moderator=None,
                                reason=None):
  log_channel = bot.get_channel(log_channel_id)
  if log_channel:
    log_message = f"**Action**: {action}\n**Target**: {target.author.mention}\n**Moderator**: {moderator.mention if moderator else 'N/A'}\n**Reason**: {reason if reason else 'N/A'}"
    await log_channel.send(log_message)
  else:
    print("Log channel not found. Make sure the channel ID is correct.")
