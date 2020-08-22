import os
import time
import keyboard
from twitchio.ext import commands

DEFAULT_PRESS_TIME = 0.5
MAX_ALLOWED_TIME = 3
MIN_ALLOWED_TIME = 0
POSSIBLE_TIMED_COMMANDS = {
    "!fwd1": "w",
    "!fwd2": "w+q",
    "!right1": "d",
    "!right2": "d+f",
    "!left1": "a",
    "!left2": "a+e",
    "!back1": "s",
    "!back2": "s+x",
    "!cast": "alt"
}
POSSIBLE_NON_TIMED_COMMANDS = {
    "!jump": "space",
    "!map": "r",
    "!potion": "ctrl"
}

HELP_MESSAGES = {
    "!fwd1": "go forwards using 1 key-timed",
    "!fwd2": "go forwards using 2 keys-timed",
    "!right1": "go right using 1 key-timed",
    "!right2": "go right using 2 keys-timed",
    "!left1": "go left using 1 key-timed",
    "!left2": "go left using 2 keys-timed",
    "!back1": "go back using 1 key-timed",
    "!back2": "go back using 2 keys-timed",
    "!cast": "holds cast - timed",
    "!jump": "jump",
    "!map": "open the map",
    "!potion": "use a potion"
}

# set up the bot
bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

async def send_keyboard_event(ctx, command_name, timing = DEFAULT_PRESS_TIME):
    if command_name in POSSIBLE_TIMED_COMMANDS:
        keyboard.press(POSSIBLE_TIMED_COMMANDS[command_name])
        time.sleep(timing)
        keyboard.release(POSSIBLE_TIMED_COMMANDS[command_name])
    elif command_name in POSSIBLE_NON_TIMED_COMMANDS:
        keyboard.send(POSSIBLE_NON_TIMED_COMMANDS[command_name])
    else:
        await ctx.channel.send(f"Whoops @{ctx.author.name}! Looks like that's not a valid command!\n Try to use !help for more information.")

async def send_error_message(ctx):
    await ctx.channel.send(f"Whoops @{ctx.author.name}! Looks like you've entered an incorrect timing string!\n Please try using a decimal number between 0-3 (0 not included)")

async def handle_message(ctx):
    split_message_string = ctx.content.split(' ')
    command_name = split_message_string[0]
    try:
        timing = split_message_string[1]
        try:
            timing = float(timing)
            if timing > MAX_ALLOWED_TIME or timing <= MIN_ALLOWED_TIME:
                raise Exception('Number not in allowed range')
            else:
                await send_keyboard_event(ctx, command_name, timing)
        except Exception:
            await send_error_message(ctx)
    except Exception:
        await send_keyboard_event(ctx, command_name)

async def send_help_message(ctx):
    full_string = ''
    message_intro = f'@{ctx.author.name} Possible commands (timed commands default to 0.5 seconds and accept a value between 0-3):'
    full_string = full_string + message_intro
    for command in HELP_MESSAGES:
        full_string += f'{command} : {HELP_MESSAGES[command]}, '
    await ctx.channel.send(full_string[:-1])


@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    await bot.handle_commands(ctx)

    if 'hello' in ctx.content.lower():
        await ctx.channel.send(f"Hi, @{ctx.author.name}!")

@bot.command(name="help")
async def help(ctx):
    await send_help_message(ctx)

@bot.command(name='test')
async def test(ctx):
    keyboard.press('alt')

@bot.command(name="fwd1")
async def fwd1(ctx):
    await handle_message(ctx)

@bot.command(name="fwd2")
async def fwd2(ctx):
    await handle_message(ctx)

@bot.command(name="right1")
async def right1(ctx):
    await handle_message(ctx)

@bot.command(name="right2")
async def right2(ctx):
    await handle_message(ctx)

@bot.command(name="left1")
async def left1(ctx):
    await handle_message(ctx)

@bot.command(name="left2")
async def left2(ctx):
    await handle_message(ctx)

@bot.command(name="back1")
async def back1(ctx):
    await handle_message(ctx)

@bot.command(name="back2")
async def back2(ctx):
    await handle_message(ctx)

@bot.command(name="map")
async def map(ctx):
    await handle_message(ctx)

@bot.command(name="potion")
async def potion(ctx):
    await handle_message(ctx)

@bot.command(name="jump")
async def jump(ctx):
    await handle_message(ctx)

@bot.command(name="cast")
async def cast(ctx):
    await handle_message(ctx)

if __name__ == "__main__":
    bot.run()