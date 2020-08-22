# Twitch Chat Plays Harry Potter Bot

# Additions by Gilad Sher

Expanded on the functionality of the bot by implementing additional methods for sending messages related to the added features!

* !help command: lists all of the possible commands to use with the bot
* all of the methods in the file are completely scale-able for additional keys if needed, and uses descriptive variable names for easy extendability of the code!
* Sending multiple events should queue up automatically (haven't tested concurrent messages and large load yet, might need to add rate limiting)

## Possible Future Features
1. More complicated inputs such as combined keys, delays etc...
2. Rate limiting if needed

# Written Using Barebones Twitch Bot in Python

>**This is my expansion on a Twitch bot using Python inspired by this [tutorial](https://dev.to/ninjabunny9000/let-s-make-a-twitch-bot-with-python-2nd8) on dev.to**

## Getting Started

Should be quick & easy to get up and running but, ofc, if you ever have questions about the specifics, please feel free to ask me during streams or post an issue above.

### Prerequisites
- [Python 3.6](https://www.python.org/downloads/release/python-368/)
- PIPENV -> `python -m pip install pipenv`
- [oauth token](https://twitchapps.com/tmi/) & [client-id](https://dev.twitch.tv/console/apps/create) for a Twitch account for your bot

### Installing
1. Clone the repo, unzip it somewhere
2. Open up a console window and navigate to the directory you unzipped it in
3. Install requirements with `pipenv install`
4. Copy & rename `.env-example` to `.env`
5. Pop in all your secrets into the respective areas in `.env`
6. Back to the console, `pipenv run python bot.py` to start the bot

## Bot Interaction
Right now, you can only interact with the bot via the single command, `!test`. You can create similar commands pretty easily, just copy the function and change out the function name decorator arguement...

```python
@bot.command(name='likethis', aliases=['this'])
async def likethis(ctx):
    await ctx.send(f'Asuh, @{ctx.author.name}!')
```

Test is out with `!likethis` in chat! :D

## Events

There are 2 events that are used in the code right now.. `on_ready` and `on_event`.

### on_ready
This executes when the bot comes online, and will print out to the console. 
```python
@bot.event
async def event_ready():
    print(f'Ready | {bot.nick}')
```

### event_message
This function executes once per event (or message) sent. You can make it handle input from chat that *aren't* necesarily commands, and fun stuff like that.

```python
@bot.event
async def event_message(message):
    print(message.content)
    await bot.handle_commands(message)
```

You can find more info in [TwitchIO's official documentation](https://twitchio.readthedocs.io/en/rewrite/twitchio.html).


## Progress & Development Info

### Contributors & Licenses

[NinjaBunny9000](https://github.com/NinjaBunny9000) - _Author, Project Manager_ - [Twitch](https://twitch.tv/ninjabunny9000) //  [Twitter](https://twitter.com/ninjabunny9000)

### Special Thanks
Literally everyone that's helped even the smallest bit during streams. Thank you so much, y'all!
