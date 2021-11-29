import os
import keyboard
from twitchio.ext import commands

DEFAULT_PRESS_TIME = 0.5
MAX_ALLOWED_TIME = 3
MIN_ALLOWED_TIME = 0
POSSIBLE_TIMED_COMMANDS = {
    "!fwd1": "w",
    "!fwd": "w",
    "!up": "w",
    "!fwd2": "w+q",
    "!right1": "d",
    "!right": "d",
    "!right2": "d+f",
    "!left1": "a",
    "!left": "a",
    "!left2": "a+e",
    "!back1": "s",
    "!back": "s",
    "!down": "s",
    "!back2": "s+x",
    "!turnr": "p",
    "!turnl": "o",
    "!viewup": "b+w",
    "!viewdown": "b+s",
    "!skip": "tab",
    "!cast": "b",
    "!tlcast": "b+o",
    "!trcast": "b+p"
}
POSSIBLE_NON_TIMED_COMMANDS = {
    "!jump": "space",
    "!map": "r",
    "!potion": "ctrl",
    "!esc": "esc"
}

# set up the bot
bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

allowed_user = None


def send_keyboard_event(ctx, command_name, timing=DEFAULT_PRESS_TIME):
    if command_name in POSSIBLE_TIMED_COMMANDS:
        keyboard.press(POSSIBLE_TIMED_COMMANDS[command_name])
        keyboard.call_later(lambda: keyboard.release(
            POSSIBLE_TIMED_COMMANDS[command_name]), delay=timing)

    elif command_name in POSSIBLE_NON_TIMED_COMMANDS:
        keyboard.send(POSSIBLE_NON_TIMED_COMMANDS[command_name])


async def send_error_message(ctx):
    await ctx.channel.send(f"Whoops @{ctx.author.name}! Looks like you've entered an incorrect timing string!\n Please try using a decimal number between 0-3 (0 not included)")


async def handle_message(ctx):
    split_message_string = ctx.content.split(' ')
    command_name = split_message_string[0]
    try:
        timing_string = split_message_string[1]
        try:
            timing_float = float(timing_string)
            if timing_float > MAX_ALLOWED_TIME or timing_float <= MIN_ALLOWED_TIME:
                raise Exception('Number not in allowed range')
            else:
                send_keyboard_event(ctx, command_name, timing=timing_float)
                return
        except ValueError:
            await send_error_message(ctx)
            return
    except Exception:
        send_keyboard_event(ctx, command_name)
        return


@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'
    if allowed_user is not None and ctx.author.name.lower() is not allowed_user or not ctx.author.is_mod:
        return

    await bot.handle_commands(ctx)


@bot.command(name="changeuser")
async def change_user(ctx):
    split_message_string: str = ctx.content.split(' ')
    global allowed_user
    try:
        _, user = split_message_string
        if user.startswith('@'):
            user = user[1:]
        user = user.lower()
        if user == 'all':
            allowed_user = None
        else:
            allowed_user = user
    except:

        return


@bot.command(name="fwd1")
async def fwd1(ctx):
    await handle_message(ctx)


@bot.command(name="fwd")
async def fwd(ctx):
    await handle_message(ctx)


@bot.command(name="up")
async def up(ctx):
    await handle_message(ctx)


@bot.command(name="fwd2")
async def fwd2(ctx):
    await handle_message(ctx)


@bot.command(name="right1")
async def right1(ctx):
    await handle_message(ctx)


@bot.command(name="right")
async def right(ctx):
    await handle_message(ctx)


@bot.command(name="right2")
async def right2(ctx):
    await handle_message(ctx)


@bot.command(name="left1")
async def left1(ctx):
    await handle_message(ctx)


@bot.command(name="left")
async def left(ctx):
    await handle_message(ctx)


@bot.command(name="left2")
async def left2(ctx):
    await handle_message(ctx)


@bot.command(name="back1")
async def back1(ctx):
    await handle_message(ctx)


@bot.command(name="back")
async def back(ctx):
    await handle_message(ctx)


@bot.command(name="down")
async def down(ctx):
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


@bot.command(name="esc")
async def esc(ctx):
    await handle_message(ctx)


@bot.command(name="turnr")
async def turnr(ctx):
    await handle_message(ctx)


@bot.command(name="turnl")
async def turnl(ctx):
    await handle_message(ctx)


@bot.command(name="tlcast")
async def tlcast(ctx):
    await handle_message(ctx)


@bot.command(name="trcast")
async def trcast(ctx):
    await handle_message(ctx)


@bot.command(name="skip")
async def skip(ctx):
    await handle_message(ctx)


@bot.command(name="viewup")
async def viewup(ctx):
    await handle_message(ctx)


@bot.command(name="viewdown")
async def viewdown(ctx):
    await handle_message(ctx)

if __name__ == "__main__":
    bot.run()
