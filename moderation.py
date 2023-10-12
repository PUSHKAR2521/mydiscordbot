import discord

# Define moderation checks

def check_caps_spam(message):
    consecutive_caps = 0
    max_consecutive_caps = 5  # Adjust this threshold as needed

    for char in message.content:
        if char.isupper():
            consecutive_caps += 1
        else:
            consecutive_caps = 0

        if consecutive_caps > max_consecutive_caps:
            return True  # Caps spam detected

    return False  # No caps spam detected

def check_link_spam(message):
    # Define a regular expression to check for URLs in the message content
    import re
    url_pattern = r'https?://\S+'
    if re.search(url_pattern, message.content):
        return True  # Link spam detected
    return False  # No link spam detected
