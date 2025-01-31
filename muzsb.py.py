import discord
from discord.ext import commands
from discord.ext import tasks, commands
import time
import random
import asyncio
import subprocess
import os
import string
import sys
import time
import re 
import json
import aiohttp

thrax = [
  "YOU\nDORK\nASS\nRUNT\nDONT\nSTEP\nTO\nYOUR\nFOUNDER\n",
  "MUZ\nMURDERD\nYOU\nLMFAO\nYOUR\nSO\nWEAK\n",
  "RETARDED\nMORON\nHAIL\nMUZ\nLOL\nUR\nFUCKING\nWORTHLESS\n",
  "YO\nCUCK\nDONT\nSTEP\nTO\nUR\nFATHER\nAGAIN\nILL\nHUMBLE\nYOU\nRETARD\n",
  "ILL\nSTEP\nON\nUR\nBITCH\nLMFAO\nCOME\nKILL\nME\nGET\nPAY\nBACK\nYOU\nWEAK\nFUCK\n",
  "COME\nHERE\nILL\nCHOKE\nYOU\n",
  "GET\nDROWNED\nBY\nUR\nGOD\n",
  "GET\nTHE\nFUCK\nDOWN",
  "ILL\nFUCKING\nMURDER\nYOU\nWEAK\nSKID",
  "SHOW\nYOUR\nFUNDS\nWEAK\nPOORON",
  "SHUT\nTHE\nFUCK\nUP\nRANDOM\nFEMBOY",
  "I\nTURN\nUR\nBITCH\nINTO\nMY\nSLUT",
  "YOUR\nMOM\nCUTS\nFOR\nME",
  "ILL\nNEVER\nFOLD\nOR\nDIE\nHAIL\nMUZ",
  "DID\nU\nDIE\nSO\nQUICK",
  "PATHETIC\nSLOW\nBOY",
  "UR\nCLIENT\nIS\nSHIT",
  "YOUR\nFUCKING\nSTRUGGLING\nTO\nLIVE",
  "BREATHE\nMY\nWEAKEST\nCHILD",
  "ILL\nRIP\nYOUR\nINTESTINES\nOUT\nAND\nFEED\nIT\nTO\nMY\nDOG",
  "YOUR\nA\nWEAK\nSKID\nASS\nNIGGA\nLOL\nUR\nFUCKING\nRETARDED\nYOU\nBUY\nSCRIPTS\nAND\nSTILL\nDIE\nYOU\nMORON",
  "YOUR\nA\nPUSSY\nASS\nKID\nWHY\nDID\nU\nSTEP\nAND\nGOT\nPUT\nTHE\nFUCK\nDOWN",
  "STEP\nTHE\nFUCK\nDOWN\nBEFORE\nA\nREAL\nSTEPPER\nMURDERS\nYOU\nUR\nMY\nLAB\nDOG\nBARK\nFOR\nUR\nGOD\nYOU\nFEMBOY\nYOU\nHAVE\nA\nCUCK\nKINK",
  "YOUR\nEGO\nDIED\nAFTER\nI\nKILLED\nUR\nSHIT\nTOKENS\nYOUR\nADDICTED\nTO\nDYING\nBY\nMUZ\nYOU\nFUCKUP\nDORK",
  "DO\nYOU\nWANT\nMY\nWORD\nLIST\n?\nLOL\nU\nMIGHT\nNEED\nIT\nU\nUSE\nCHAT\nGPT\nTO\nGIVE\nU\nWORDS",
  "SHUT\nUP\nBROKE\nASS\nKID",
  "I\nFEEL\nBAD\nBUT\nI\nHAVE\nTO\nSHOW\nYOU\nWHO\nUR\nGOD\nIS",
  "LETS\nGO\nTO\nWAR\nWATCH\nU\nDIE\nWEAK\nFUCK",
  "YOU\nWILL\nNEVER\nGET\nA\nBITCH\nAND\nIF\nU\nDO\nU\nWILL\nMAKE\nHER\nPUSSY\nDRY",
  "STFU\nYOU\n1WPM\nWARRIOR\nUR\nSAD\nAS\nSHIT",
  "ILL\nNEVER\nDIE\nKEEP\nGOING\nTILL\nYOUR\nBONES\nDECAY\nMY\nCLIENTS\nCAN\nOUTLAST\nYOUR\nWORTHLESS\nLIFE",
  "SHUT\nUP\nYOU\nLOW\nTIER\nRETARD",
  "you\ndied\nto\na\ngod\nlol\nits\nokay\njrs\nlike\nyou\nalways\nfail\nme", 
  "YOU\nDISAPOINTED\nME\nI\nWANTED\nTO\nGO\nLONGER",
  "SAY\nIT\nWITH\nYOUR\nCHEST\nYOU\nCANT\nHANDLE\nTHE\nGREATEST"
  
]




autoreplies_multi = [
    "SHUT THE FUCKUP", "UR A BITCH", "LOL", "SHUT YO LAME ASS UP NIGGA",
    "DONT FOLD", "DORK ASS CUNT", "FUCK ASS BITCH",
    "SMD HEADASS NIGGA LMFAO UR WORTH NOTHING TO ME", "UR MY BITCH",
    "FUCK ASS NIGGA", "UR MY SEED", "UR A HOE", "NIGGA U DIED TO ME",
    "IM FASTER THEN U SON", "UR A NERD", "NERD HEADASS LMFAO 🤓", "DONT STEP TO ME AGAIN",
    "NIGGA FOLDED TO ME", "PIPE THE FUCK DOWN", "I OWN U SON", "UR SLOW",
    "UR A BITCH", "LMFAO", "I DONT KNOW U", "FUCK ASS CUNT", "NIGGA TRIED STEPPING",
    "HOW DID U GET HOED LIKE THAT", "DUMB ASS BITCH", "I DONT FOLD",
    "SHUT THE FUCK UP", "TRY STEPPING AGAIN", "UR A BITCH",
    "DUMB ASS NIGGA", "DUMB ASS BITCH THOUGHT HE COULD STEP",
    "DO SUM LMFAO I RULE U", "SIGN UR LIFE AWAY TO MUZ", 
    "FOCUS UP SONNY DONT FOLD", "COME KILL ME YOU WEAK FUCK", 
    "THIS POORON CANT DO SHIT", "SHOW ME UR FUNDS", "LOLLL THIS DORK  CANT DO SHIT TO ME",
    "MY EGO BIGGER THAN YO DICK NIGGA", "LMAO ARENT U A PEDO?", "YOU STEPPED TO A GOD AND THOUGHT U WOULD MURDER ME", "WHY ARE YOU SO SLOW LMFAOOO",
     "LMFAO DONT SPEAK TO ME U EDATE SON", "LMFAO ILL TRAP U SON",
    "WHY RU FOLDING TO ME LOL", "U CANT CODE U STAND NO CHANCE AGAINST ME CRY", "LMFAO NICE DUCK KID",
    "CARVE MY NAME INTO UR SKIN MUZ OWNS ME", "LOL NICE SKID", "BOW DOWN TO ME WHORE", "I OWN U CUCK",
    "BOW DOWN TO ME", "STOP PACKING", "U LOVE SUCKING ON MY DICK", "UGLY FAN", "DONT STEP I OWN THIS",
    "IM UR GOD", "U USE GRABIFY TO DOX LMFAO", "CUT 4 ME SLUT", "UR SLOW", "U CANT DO NOTHING",
    "I OWN U WHORE", "HANG URSELF JEW", "I DONT FOLD UR MY HOE", "UR PC IS SLOW",
    "NIGGAS DUCKING LMFAO", "L FUCKING PRESS", "DORK I OWN YOU", "WHY IS THIS NIGGA CRYING LOL",
    "U CANT HARM ME", "NIGGA THINKS 764 CAN HARM LOL KILL URSELF", "STREAM UR DEATH", "ILL RAIL UR BITCH",
    "UR E GIRL CALLS ME DADDY LMFAO UR WORTHLESS", "STEP THE FUCK DOWN", "KEEP TYPING SO I CAN EXILE U",
    "BITCHLESS NIGGA HAD TO GET HIS WEAK E FRIENDS", "UR SAD AND WORTHLESS",
    "U AMOUNT TO NOTHING", "I RULE YOU", "I HOE U", "YOUR LIFE IS WORTHLESS UR PACKS ARE SLOW LOG OUT",
    "THIS NEVER STOPS", "gayest shit i seen all year", "THIS KID IS OWNED", "WHY CANT U FIGHT BACK",
    "MUZ OWNS YOU CUCK", "FUCK ASS DORK U CANT DO SHIT", "WHO THIS BITCH THINK HE IS", "WHY ARE YOU DUCKING?",
    "COME CRY TO DADDY", "NIGGAS CANT DO SHIT", "ACCEPT UR FATE", "I KILLED U", "NICE RUN",
    "KID CANT DO SHIT HES CRYING", "I OWN ALL UR E GIRLS", "IMA BEAM U", "STOP REPPING UR SHITTY CLAN",
    "SKIDS WAS MORE HARMFUL THAN THIS", "WHY ARE YOU SO UNKNOWN", "COME DO SOMETHING", "OD ON PAINKILLERS",
    "WHY ARE U SO SHITTY", "UR POOR HTML CANT DO SHIT", "COME DO SOMETHING", "I RUN THIS SHIT",
    "YOU'RE A FAILURE", "STAY SILENT, I OWN YOU", "DON'T PACK ME AGAIN", 
    "YOU'RE DONE", "KEEP TALKING JR", "MY MOM TYPES FASTER THAN THIS WHAT THE FUCK LMFAOO", 
    "YO FATASS CANT TYPE", "UR MY HOE", 
    "YOU'RE THE SLUT OF THIS SERVER", "YOU'RE PATHETIC", 
    "COME CHALLENGE ME", "YOUR WHOLE EXISTENCE IS TO SERVE ME","HOW ARE YOU USING A SKIDDED CLIENT AND STILL SLOW WTF 😂 "
]

outlast_messages = [
    "> STEP THE FUCK DOWN AND DIE TO MUZ STEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO XOMSTEP THE FUCK DOWN AND DIE TO XOMSTEP THE FUCK DOWN AND DIE TO XOMSTEP THE FUCK DOWN AND DIE TO XOMSTEP THE FUCK DOWN AND DIE TO XOMSTEP THE FUCK DOWN AND DIE TO XOMSTEP THE FUCK DOWN AND DIE TO XOMSTEP THE FUCK DOWN AND DIE TO XOMSTEP THE FUCK DOWN AND DIE TO XOMSTEP THE FUCK DOWN AND DIE TO XOMSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZSTEP THE FUCK DOWN AND DIE TO MUZ "
]

protection_messages = [ 
    "SHUT THE FUCKUP", "UR A BITCH", "LOL", "SHUT YO LAME ASS UP NIGGA",
    "DONT FOLD", "DORK ASS CUNT", "FUCK ASS BITCH",
    "SMD HEADASS NIGGA LMFAO UR WORTH NOTHING TO ME", "UR MY BITCH",
    "FUCK ASS NIGGA", "UR MY SEED", "UR A HOE", "NIGGA U DIED TO ME",
    "IM FASTER THEN U SON", "UR A NERD", "NERD HEADASS LMFAO 🤓", "DONT STEP TO ME AGAIN",
    "NIGGA FOLDED TO ME", "PIPE THE FUCK DOWN", "I OWN U SON", "UR SLOW",
    "UR A BITCH", "LMFAO", "I DONT KNOW U", "FUCK ASS CUNT", "NIGGA TRIED STEPPING",
    "HOW DID U GET HOED LIKE THAT", "DUMB ASS BITCH", "I DONT FOLD",
    "SHUT THE FUCK UP", "TRY STEPPING AGAIN", "UR A BITCH",
    "DUMB ASS NIGGA", "DUMB ASS BITCH THOUGHT HE COULD STEP",
    "DO SUM LMFAO I RULE U", "SIGN UR LIFE AWAY TO MUZ", 
    "FOCUS UP SONNY DONT FOLD", "COME KILL ME YOU WEAK FUCK", 
    "THIS POORON CANT DO SHIT", "SHOW ME UR FUNDS", "LOLLL THIS DORK  CANT DO SHIT TO ME",
    "MY EGO BIGGER THAN YO DICK NIGGA", "LMAO ARENT U A PEDO?", "YOU STEPPED TO A GOD AND THOUGHT U WOULD MURDER ME", "WHY ARE YOU SO SLOW LMFAOOO",
     "LMFAO DONT SPEAK TO ME U EDATE SON", "LMFAO ILL TRAP U SON",
    "WHY RU FOLDING TO ME LOL", "U CANT CODE U STAND NO CHANCE AGAINST ME CRY", "LMFAO NICE DUCK KID",
    "CARVE MY NAME INTO UR SKIN MUZ OWNS ME", "LOL NICE SKID", "BOW DOWN TO ME WHORE", "I OWN U CUCK",
    "BOW DOWN TO ME", "STOP PACKING", "U LOVE SUCKING ON MY DICK", "UGLY FAN", "DONT STEP I OWN THIS",
    "IM UR GOD", "U USE GRABIFY TO DOX LMFAO", "CUT 4 ME SLUT", "UR SLOW", "U CANT DO NOTHING",
    "I OWN U WHORE", "HANG URSELF JEW", "I DONT FOLD UR MY HOE", "UR PC IS SLOW",
    "NIGGAS DUCKING LMFAO", "L FUCKING PRESS", "DORK I OWN YOU", "WHY IS THIS NIGGA CRYING LOL",
    "U CANT HARM ME", "NIGGA THINKS 764 CAN HARM LOL KILL URSELF", "STREAM UR DEATH", "ILL RAIL UR BITCH",
    "UR E GIRL CALLS ME DADDY LMFAO UR WORTHLESS", "STEP THE FUCK DOWN", "KEEP TYPING SO I CAN EXILE U",
    "BITCHLESS NIGGA HAD TO GET HIS WEAK E FRIENDS", "UR SAD AND WORTHLESS",
    "U AMOUNT TO NOTHING", "I RULE YOU", "I HOE U", "YOUR LIFE IS WORTHLESS UR PACKS ARE SLOW LOG OUT",
    "THIS NEVER STOPS", "gayest shit i seen all year", "THIS KID IS OWNED", "WHY CANT U FIGHT BACK",
    "MUZ OWNS YOU CUCK", "FUCK ASS DORK U CANT DO SHIT", "WHO THIS BITCH THINK HE IS", "WHY ARE YOU DUCKING?",
    "COME CRY TO DADDY", "NIGGAS CANT DO SHIT", "ACCEPT UR FATE", "I KILLED U", "NICE RUN",
    "KID CANT DO SHIT HES CRYING", "I OWN ALL UR E GIRLS", "IMA BEAM U", "STOP REPPING UR SHITTY CLAN",
    "SKIDS WAS MORE HARMFUL THAN THIS", "WHY ARE YOU SO UNKNOWN", "COME DO SOMETHING", "OD ON PAINKILLERS",
    "WHY ARE U SO SHITTY", "UR POOR HTML CANT DO SHIT", "COME DO SOMETHING", "I RUN THIS SHIT",
    "YOU'RE A FAILURE", "STAY SILENT, I OWN YOU", "DON'T PACK ME AGAIN", 
    "YOU'RE DONE", "KEEP TALKING JR", "MY MOM TYPES FASTER THAN THIS WHAT THE FUCK LMFAOO", 
    "YO FATASS CANT TYPE", "UR MY HOE", 
    "YOU'RE THE SLUT OF THIS SERVER", "YOU'RE PATHETIC", 
    "COME CHALLENGE ME", "YOUR WHOLE EXISTENCE IS TO SERVE ME","HOW ARE YOU USING A SKIDDED CLIENT AND STILL SLOW WTF 😂 "
]

protection_groupchat = [
"ILL RIP YOUR SPINE OUT WEAK SKID",
"YOU WEAK PUNEY FUCK I COULD STEP ON YOU AND BREAK YOUR RIBS",
"YOUR USELESS AND SHITTY",
"YOUR WPM IS 2 LMFOAOO",
"STOP STEPPING U SLOW BRAINED MORON",
"YOU SHIT MUSLIM DORK",
"FUCK UP WEAK DORK",
"YOU TRIED TO TRAP AND GOT MURDERD",
"YOUR FUCKING PATHTIC",
"USE A AUTOBEEFER AT THIS POINT PLEASE YOU RETARDED SCUM",
"YOU FALIED AND DIED TO MUZ UR NEW GOD",
]

afk_triggers = [
"weak",
]



prefix = ''
intents = discord.Intents.default()
intents.messages = True
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix=prefix, self_bot=True, intents=discord.Intents.default())


def load_tokens(file_path='token.txt'):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    return []

tokens = load_tokens()
gc_tasks = {}
kill_tasks = {}
autoreply_tasks = {}
arm_tasks = {}
outlast_tasks = {}
protection_tasks = {}
reactm_running = {}
reactm_tasks = {}
autoreact_users = {}
afkcheck_tasks = {}

outlast_running = False
status_changing_task = None
bold_mode = False
cord_user = False
protection_running = False
antiafk_enabled = False
mping_running = False


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def multilast(ctx, user: discord.User):
    global outlast_running
    outlast_running = True
    
    # Create a shared counter object
    class SharedCounter:
        def __init__(self):
            self.value = 1
            self.lock = asyncio.Lock()
        
        async def increment(self):
            async with self.lock:
                current = self.value
                self.value += 1
                return current
    
    shared_counter = SharedCounter()

    async def send_message(token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        
        # Each token keeps its own message counter
        token_counter = 1
        
        while outlast_running:
            message = random.choice(outlast_messages)
            # Get the shared counter value
            global_count = await shared_counter.increment()
            
            payload = {
                'content': f"{message}\n{user.mention}```{global_count}```"
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(f'https://discord.com/api/v9/channels/{ctx.channel.id}/messages', 
                                      headers=headers, json=payload) as resp:
                    if resp.status == 200:
                        print(f"Message sent with token: {token}")
                        token_counter += 1
                    elif resp.status == 429:
                        print(f"Rate limited with token: {token}. Retrying...")
                        await asyncio.sleep(1)
                    else:
                        print(f"Failed to send message with token: {token}. Status code: {resp.status}")

            await asyncio.sleep(0.1)

    tasks = [send_message(token) for token in tokens]
    await asyncio.gather(*tasks)

@bot.command()
async def stoplast(ctx):
    global outlast_running
    if outlast_running:
        outlast_running = False  
        await ctx.send("```outlast has been stopped```")
    else:
        await ctx.send("")

@bot.command()
async def ar(ctx, user: discord.User, *, prefix_message: str = ""):


    channel_id = ctx.channel.id
    last_message_time = 0
    backoff_time = 0.1 

    async def send_autoreply(message):
        nonlocal last_message_time, backoff_time
        try:
            current_time = time.time()
            time_since_last = current_time - last_message_time
            
            if time_since_last < backoff_time:
                await asyncio.sleep(backoff_time - time_since_last)
            
            
            reply_message = f"{prefix_message}"
            await ctx.send(f"#  _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n   _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n _ _\n {reply_message}\n {user.mention} ")
            
            last_message_time = time.time()
            backoff_time = max(0.1, backoff_time * 0.95)
            
        except discord.HTTPException as e:
            if e.status == 429:  # Rate limit hit
                retry_after = float(e.response.headers.get('retry_after', 1.0))
                print(f"Rate limited in ar command. Waiting {retry_after}s...")
                backoff_time = min(2.0, backoff_time * 1.5)
                await asyncio.sleep(retry_after)
                await send_autoreply(message)
            else:
                print(f"HTTP Error in ar command: {e}")
                await asyncio.sleep(1)
        except Exception as e:
            print(f"Error in ar command: {e}")
            await asyncio.sleep(1)

    async def reply_loop():
        def check(m):
            return m.author == user and m.channel == ctx.channel

        while True:
            try:
                message = await bot.wait_for('message', check=check)
                # Add small random delay before responding
                await asyncio.sleep(random.uniform(0.1, 0.3))
                await send_autoreply(message)
            except Exception as e:
                print(f"Error in ar reply loop: {e}")
                await asyncio.sleep(1)

    task = bot.loop.create_task(reply_loop())
    autoreply_tasks[(user.id, channel_id)] = task


@bot.command()
async def arend(ctx):
    channel_id = ctx.channel.id
    tasks_to_stop = [key for key in autoreply_tasks.keys() if key[1] == channel_id]
    
    if tasks_to_stop:
        for user_id in tasks_to_stop:
            task = autoreply_tasks.pop(user_id)
            task.cancel()



@bot.command()
async def kill(ctx, user_id: str):
    channel_id = ctx.channel.id

    async def send_message(token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        random_sentence = random.choice(thrax)
        payload = {
            'content': f"# {random_sentence}\n{user_id}"
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=payload) as resp:
                if resp.status == 200:
                    print(f"Message sent with token: {token}")
                elif resp.status == 429:
                    print(f"Rate limited with token: {token}. Retrying...")
                    await asyncio.sleep(0.1)
                else:
                    print(f"Failed to send message with token: {token}. Status code: {resp.status}")

    async def kill_loop():
        while True:
            tasks = [send_message(token) for token in tokens]
            await asyncio.gather(*tasks)
            await asyncio.sleep(0.1)

    task = bot.loop.create_task(kill_loop())
    kill_tasks[(user_id, channel_id)] = task

@bot.command()
async def killend(ctx):
    channel_id = ctx.channel.id
    tasks_to_stop = [key for key in kill_tasks.keys() if key[1] == channel_id]
    
    if tasks_to_stop:
        for user_id in tasks_to_stop:
            task = kill_tasks.pop(user_id)
            task.cancel()

@bot.command()
async def fill(ctx):
    tokens_file_path = 'token.txt'
    tokens = load_tokens(tokens_file_path)
    group_channel = ctx.channel

    for token in tokens:
        user_client = discord.Client(intents=intents)

        @user_client.event
        async def on_ready():
            print(f'Logged in as {user_client.user} using token {token[-4:]}.')
            try:
                await group_channel.add_recipients(user_client.user)
                print(f'Added {user_client.user} to the group chat')
            except discord.errors .Forbidden:
                print("Bot doesn't have permission to add to the group chat.")
            except discord.errors.HTTPException as e:
                if e.status == 429:
                    retry_after = int(e.response.headers.get('Retry-After', 1))
                    print(f"Token {token[-4:]} is being rate limited. Waiting for {retry_after} seconds...")
                    await asyncio.sleep(retry_after)
                elif e.status == 401:
                    print(f"Token {token[-4:]} is invalid. Skipping...") 
                else:
                    print(f"HTTP error occurred: {e}")
            await user_client.close()

        await user_client.start(token, bot=False)

def read_tokens(filename='token.txt'):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    return []

async def update_presence1(token, details):
    if token.strip() == "":
        print("Skipping empty token")
        return

    client = discord.Client()

    @client.event
    async def on_ready():
        activity = discord.Streaming(
            name=details, 
            url='https://www.twitch.tv/ex'
        )
        await client.change_presence(activity=activity)

    try:
        await client.start(token, bot=False)  
    except discord.LoginFailure:
        print(f"Failed to login with token: {token} - Invalid token")
    except Exception as e:
        print(f"An error occurred with token: {token} - {e}")

async def streamall(ctx, messages):
    tokens = read_tokens('token.txt')  
    details = [random.choice(messages) for _ in range(len(tokens))]

    tasks = [update_presence1(token, detail) for token, detail in zip(tokens, details)]
    await asyncio.gather(*tasks)
    await ctx.send(f"Statuses updated for all tokens")


async def rename_display_name(token, new_name):

    try:
        # Create a temporary client for the token
        user_client = discord.Client()

        @user_client.event
        async def on_ready():
            print(f'Logged in as {user_client.user} using token {token[-4:]}.')
            try:
                # Iterate over all guilds (servers) the bot is in
                for guild in user_client.guilds:
                    # Find the member object (the bot itself) in the guild
                    member = guild.get_member(user_client.user.id)
                    if member:
                        # Change the display name (nickname) for the member in this guild
                        await member.edit(nick=new_name)
                        print(f"Renamed display name to {new_name} in server {guild.name} for token {token[-4:]}")
                    else:
                        print(f"Member not found in server {guild.name} for token {token[-4:]}")
                
            except discord.errors.Forbidden:
                print(f"Token {token[-4:]} doesn't have permission to change the display name in some servers.")
            except discord.errors.HTTPException as e:
                if e.status == 429:
                    retry_after = int(e.response.headers.get('Retry-After', 1))
                    print(f"Token {token[-4:]} is being rate limited. Waiting for {retry_after} seconds...")
                    await asyncio.sleep(retry_after)
                elif e.status == 401:
                    print(f"Token {token[-4:]} is invalid. Skipping...")
                else:
                    print(f"HTTP error occurred with token {token[-4:]}: {e}")
            except Exception as e:
                print(f"Error occurred with token {token[-4:]}: {e}")
            finally:
                await user_client.close()


        await user_client.start(token, bot=False)

    except Exception as e:
        print(f"Failed to process token {token[-4:]}: {str(e)}")


@bot.command()
async def rename(ctx, *, new_name: str):

    tokens_file_path = 'token.txt'
    

    if not os.path.exists(tokens_file_path):

        return
    
    with open(tokens_file_path, 'r') as file:
        tokens = [line.strip() for line in file if line.strip()]
    
    if not tokens:
        await ctx.send("No tokens found in `token.txt`.")
        return


    for token in tokens:
        await rename_display_name(token, new_name)
    






@bot.command()
async def rpcall(ctx, *, message: str):  
    messages = message.split(',')  
    await streamall(ctx, messages)

async def change_status():
    await bot.wait_until_ready()
    while True:
        for status in statuses:
            await bot.change_presence(activity=discord.Streaming(name=status, url="https://www.twitch.tv/ex"))
            await asyncio.sleep(10) 

@bot.command()
async def rpc(ctx, *, statuses_list: str):
    global status_changing_task
    global statuses
    
    statuses = statuses_list.split(',')
    statuses = [status.strip() for status in statuses]
    
    if status_changing_task:
        status_changing_task.cancel()
    
    status_changing_task = bot.loop.create_task(change_status())

@bot.command()
async def stoprpc(ctx):
    global status_changing_task
    
    if status_changing_task:
        status_changing_task.cancel()
        status_changing_task = None
        await bot.change_presence(activity=None)  
        await ctx.send(f'status rotation stopped')
    else:
        await ctx.send(f'status rotation is not running')

@bot.command()
async def token(ctx):
    tokens_list = load_tokens()
    if not tokens_list:
        await ctx.send("No tokens found in token.txt")
        return
    
    async def get_username(token):
        try:
            intents = discord.Intents.default()
            client = commands.Bot(command_prefix='.', self_bot=True, intents=intents)
            
            username = None
            
            @client.event
            async def on_ready():
                nonlocal username
                username = f"{client.user.name}#{client.user.discriminator}"
                await client.close()
            
            await client.start(token, bot=False)
            return username
            
        except discord.LoginFailure:
            return f"Invalid token ending in {token[-4:]}"
        except Exception as e:
            return f"Error with token {token[-4:]}: {str(e)}"

    message = await ctx.send("```fetching token usernames..```")
    
    usernames = []
    for i, token in enumerate(tokens_list, 1):
        username = await get_username(token)
        if username:
            usernames.append(f"{i}. {username}")
    
    formatted_message = "```\n T O K E N S\n" + "\n".join(usernames) + "\n```"
    await message.edit(content=formatted_message)

@bot.command()
async def bold(ctx):
    global bold_mode
    bold_mode = True
    await ctx.send("```enabling bold```")

@bot.command()
async def unbold(ctx):
    global bold_mode
    bold_mode = False
    await ctx.send("```disabling bold```")

@bot.command()
async def exile(ctx, user: discord.User):
    global protection_running
    protection_running = True
    channel_id = ctx.channel.id

    class SharedCounter:
        def __init__(self):
            self.value = 1
            self.lock = asyncio.Lock()
        
        async def increment(self):
            async with self.lock:
                current = self.value
                self.value += 1
                return current

    shared_counter = SharedCounter()

    async def send_message(token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        
        last_send_time = 0
        backoff_time = 0.1
        
        while protection_running:
            try:
                current_time = time.time()
                time_since_last = current_time - last_send_time
                
                if time_since_last < backoff_time:
                    await asyncio.sleep(backoff_time - time_since_last)
                
                message = random.choice(protection_messages)
                count = await shared_counter.increment()
                
                payload = {
                    'content': f"{user.mention} {message}\n```{count}```"
                }

                async with aiohttp.ClientSession() as session:
                    async with session.post(
                        f'https://discord.com/api/v9/channels/{ctx.channel.id}/messages', 
                        headers=headers, 
                        json=payload
                    ) as resp:
                        if resp.status == 200:
                            print(f"Protection message sent with token: {token[-4:]}")
                            backoff_time = max(0.1, backoff_time * 0.95)
                            last_send_time = time.time()
                        elif resp.status == 429:
                            retry_after = float((await resp.json()).get('retry_after', 1))
                            print(f"Rate limited with token: {token[-4:]}. Waiting {retry_after}s...")
                            backoff_time = min(2.0, backoff_time * 1.5)
                            await asyncio.sleep(retry_after)
                        else:
                            print(f"Failed to send message with token: {token[-4:]}. Status: {resp.status}")
                            await asyncio.sleep(1)

                await asyncio.sleep(random.uniform(0.1, 0.3))
                
            except Exception as e:
                print(f"Error in send_message for token {token[-4:]}: {str(e)}")
                await asyncio.sleep(1)

    async def change_name(token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        
        last_change_time = 0
        backoff_time = 0.5
        
        while protection_running:
            try:
                current_time = time.time()
                time_since_last = current_time - last_change_time
                
                if time_since_last < backoff_time:
                    await asyncio.sleep(backoff_time - time_since_last)
                
                gc_name = random.choice(protection_groupchat)
                count = await shared_counter.increment()
                
                payload = {
                    'name': f"{gc_name} {count}"
                }

                async with aiohttp.ClientSession() as session:
                    async with session.patch(
                        f'https://discord.com/api/v9/channels/{channel_id}', 
                        headers=headers, 
                        json=payload
                    ) as resp:
                        if resp.status == 200:
                            print(f"GC name changed with token: {token[-4:]}")
                            backoff_time = max(0.5, backoff_time * 0.95)
                            last_change_time = time.time()
                        elif resp.status == 429:
                            retry_after = float((await resp.json()).get('retry_after', 1))
                            print(f"Rate limited with token: {token[-4:]}. Waiting {retry_after}s...")
                            backoff_time = min(5.0, backoff_time * 1.5)
                            await asyncio.sleep(retry_after)
                        else:
                            print(f"Failed to change GC name with token: {token[-4:]}. Status: {resp.status}")
                            await asyncio.sleep(1)

                await asyncio.sleep(random.uniform(0.5, 1.0))
                
            except Exception as e:
                print(f"Error in change_name for token {token[-4:]}: {str(e)}")
                await asyncio.sleep(1)

    message_tasks = [send_message(token) for token in tokens]
    name_tasks = [change_name(token) for token in tokens]
    all_tasks = message_tasks + name_tasks
    
    combined_task = asyncio.gather(*all_tasks)
    protection_tasks[channel_id] = combined_task
    


@bot.command()
async def stopexile(ctx):
    global protection_running
    channel_id = ctx.channel.id
    
    if channel_id in protection_tasks:
        protection_running = False
        task = protection_tasks.pop(channel_id)
        task.cancel()
        await ctx.send("```exile ended```")
    else:
        await ctx.send("")

@bot.command()
async def antitrap(ctx):
    global antiafk_enabled
    antiafk_enabled = True
    await ctx.send("```afk mode enabled```")

@bot.command()
async def afkoff(ctx):
    global antiafk_enabled
    antiafk_enabled = False
    await ctx.send("```afk mode disabled```")

cord_mode = False  # Change to True if you want it active by default
cord_user = None  # Set to a specific user if needed

@bot.event
async def on_message(message):
    try:
        await bot.process_commands(message)

        if message.author.bot:
            return

        # Handle auto-reaction
        emoji = autoreact_users.get(message.author.id)
        if emoji:
            try:
                await message.add_reaction(emoji)
            except discord.HTTPException:
                print(f"Failed to add reaction {emoji} to message from {message.author}")

        # Handle message editing and translation for the bot's own messages
        if message.author.id == bot.user.id:
            content = message.content
            should_edit = False

            
            if not content.startswith('.'):
                print("Content does not start with a command prefix.")

                # Apply bold mode
                if bold_mode and not (content.startswith('**') and content.endswith('**')):
                    content = f"# {content}"
                    should_edit = True
                    print("Bold mode applied to the content.")

                # Apply cord mode (ensure cord_mode and cord_user are defined)
                if cord_mode and cord_user:
                    content = f"# {content} {cord_user.mention}"
                    should_edit = True
                    print("Cord mode applied to the content.")

                # Edit the message if conditions are met
                if should_edit:
                    print(f"Editing message to: {content}")
                    await message.edit(content=content)
                else:
                    print("No conditions met for editing the message.")

        elif antiafk_enabled and isinstance(message.channel, discord.DMChannel):
            msg_content = message.content.lower()
            if any(trigger in msg_content for trigger in afk_triggers):
                await asyncio.sleep(random.uniform(0.3334445, .3434343433434))
                await message.channel.send("here")

    except Exception as e:
        print(f"Error in on_message: {e}")

@bot.command()
async def afkcheck(ctx, user: discord.User, count: int):

    if count <= 0 or count > 1000: 
        await ctx.send("```number through 100 - 1000s```")
        return

    task_key = (user.id, ctx.channel.id)
    if task_key in afkcheck_tasks:
        afkcheck_tasks[task_key].cancel()
        del afkcheck_tasks[task_key]

    current_count = 1
    running = True

    async def check_response():
        nonlocal running
        def check(m):
            return m.author.id == user.id and any(trigger in m.content.lower() for trigger in ['here', 'im here', 'here.'])

        try:
            await bot.wait_for('message', check=check, timeout=None)
            running = False
            await ctx.send(f"```welcome back you didnt fold kid```")
        except Exception as e:
            print(f"Error in response checker: {e}")

    async def counter():
        nonlocal current_count, running
        
        while running and current_count <= count:
            try:
                await asyncio.sleep(random.uniform(0.5, 0.75))
                
                await ctx.send(f"{user.mention} AFK CHECK SAY HERE\n```{current_count}```")
                current_count += 1

                if current_count > count:
                    running = False
                    await ctx.send(f"```dork folded to xom```\n{user.mention}")
                    
            except Exception as e:
                print(f"Error in counter: {e}")
                await asyncio.sleep(1)  

    response_task = bot.loop.create_task(check_response())
    counter_task = bot.loop.create_task(counter())
    
    afkcheck_tasks[task_key] = asyncio.gather(response_task, counter_task)






    
@bot.command()
async def reload(ctx):
    await ctx.send("```Reloading bot...```")
    os.execv(sys.executable, ['python'] + sys.argv)



current_song = None
is_pr_active = False
snipe_messages = {}
pl_task = None
pressure_task = None
current_prefix = prefix
mimic_users = {}
status_rotate_task = None
rpc = None
rpc_task = None
status_changing_task = None 
massdm_task = None
massgc_task = None
ar_task = None
status_messages = []  
rotate_task = None  
ldr_tasks = {}  
CLIENT_ID = "1309769248746246194"
ldr_task = None
ladder_mode = False
bold_mode = False
reacting = False















  












@bot.command(name='spam')
async def say(ctx, times: int=None, *, message=None):
    await ctx.message.delete()
    if times is None:
        await ctx.send(f'```[Invalid]: Command: {bot.command_prefix}say <times> <message>```')
        return
        if message is None:
            await ctx.send(f'```[Invalid]: Command: {bot.command_prefix}say <times> <message>```')
            return
    for _ in range(times):
        await ctx.send(message)  















bane = [
    "SHUT THE FUCKUP", "UR A BITCH", "LOL", "SHUT YO LAME ASS UP NIGGA",
    "DONT FOLD", "DORK ASS CUNT", "FUCK ASS BITCH",
    "SMD HEADASS NIGGA LMFAO UR WORTH NOTHING TO ME", "UR MY BITCH",
    "FUCK ASS NIGGA", "?", "UR MY SEED", "UR A HOE", "NIGGA U DIED TO ME",
    "IM FASTER THEN U SON", "UR A NERD", "🤓", "DONT STEP TO ME AGAIN",
    "NIGGA FOLDED TO ME", "PIPE THE FUCK DOWN", "I OWN U SON", "UR SLOW",
    "UR A BITCH", "LMFAO", "I DONT KNOW U", "FUCK ASS CUNT", "NIGGA TRIED STEPPING",
    "HOW DID U GET HOED LIKE THAT", "DUMB ASS BITCH", "I DONT FOLD",
    "SHUT THE FUCK UP", "TRY STEPPING AGAIN", "UR A BITCH",
    "DUMB ASS NIGGA", "DUMB ASS BITCH THOUGHT HE COULD STEP",
    "DO SUM LMFAO I RULE U", "SIGN UR LIFE AWAY TO XOM", "I DONT FOLD ILL GO FOREVER",
    "WHY RU DUCKING?", "UR NOT FAST COME AUTO AND STILL DIE", "ONE CLIENT CAN STILL CUCK U",
    "THIS POORON CANT DO SHIT", "1 2 3 4 5 6 7 8 9 10 LMFAO U FUCKING DIED", "SHOW ME UR FUNDS", "LOLLL THIS DORK  CANT DO SHIT TO ME",
    "MY EGO BIGGER THAN YO DICK NIGGA", "LMAO ARENT U A PEDO?", "SHOW ME UR HARDRIVE PEDOO", "WHY ARE YOU SO FAT LOOL",
    "KID IS GETTING RATE LIMTED", "LMFAO DONT SPEAK TO ME U EDATE SON", "LMFAO ILL TRAP U SON",
    "WHY RU FOLDING TO ME LOL", " U STAND NO CHANCE AGAINST ME CRY", "LMFAO NICE DUCK KID", 
    "CARVE MY NAME INTO UR SKIN", "LOL NICE FOLD", "BOW DOWN TO ME WHORE", "I OWN U CUCK", 
    "BOW DOWN TO ME", "STOP PACKING", "U LOVE SUCKING ON MY DICK", "UGLY FAN", "DONT STEP I OWN THIS",
    "IM UR GOD", "U USE GRABIFY TO DOX LMFAO", "CUT 4 ME SLUT", "UR SLOW", "U CANT DO NOTHING",
    "I OWN U WHORE", "HANG URSELF JEW", "I DONT FOLD UR MY HOE", "I NEVER FOLD OR DIE ILL MAKE YOU BLEED I RUN YOU",
    "NIGGAS DUCKING LMFAO", "L FUCKING PRESS ", "DORK ASS NIGGA", "WHY IS THIS NIGGA CRYING LOL",
    "U CANT HARM ME", "YOUS A BITCH LOL KILL URSELF", "STREAM UR DEATH", "ILL RAIL UR BITCH",
    "UR E GIRL DONT FW U ", "U FINGER URSELF", "KEEP TYPING SO I CAN EXILE U", 
    "WHY ARE YOU SO SLOW IM USING 1 ACC LOL", "BITCHLESS NIGGA HAD TO GET HIS E FRIENDS", "UR SAD AND WORTHLESS",
    "U AMOUNT TO NOTHING", "I RULE YOU", "I HOE U", "YOUR LIFE IS WORTHLESS UR PACKS ARE SLOW LOG OUT",
    "THIS NEVER STOPS", "gayest shit i seen all year", "THIS KID IS OWNED", "WHY CANT U FIGHT BACK",
    "XOM OWNS YOU CUCK", "FUCK ASS DORK U CANT DO SHIT", "WHO THIS BITCH THINK HE IS", "WHY ARE YOU DUCKING?",
    "COME CRY TO DADDY", "NIGGA CANT DO SHIT", "ACCEPT UR FATE", "I KILLED U", "NICE RUN", 
    "KID CANT DO SHIT HES CRYING", "I OWN ALL UR E GIRLS", "IMA BEAM U", "STOP REPPING UR SHITTY CLAN",
    "2779 WAS MORE HARMFUL THAN THIS", "WHY ARE YOU SO UNKNOWN", "COME DO SOMETHING", "OD ON PAINKILLERS",
    "WHY ARE U SO SHITTY", "UR POOR HTML CANT DO SHIT", "COME DO SOMETHING", "I RUN THIS SHIT",
    "YOU'RE A FAILURE", "STAY SILENT, I OWN YOU", "DON'T PACK ME AGAIN", 
    "I HOE YOU UR SHITTY CORD CANT OUTLAST ME I DONT DIE", "KEEP TALKING JR", "MY MOM TYPES FASTER THAN THIS WHAT THE FUCK LMFAOO", 
    "YO FATASS CANT TYPE", "UR MY HOE", "KEEP CRYING", "I'LL TAKE EVERYTHING FROM YOU",
    "YOU'RE EMBARRASSING YOURSELF", "YOUR FUCKING ASS", "BOW DOWN AND ACCEPT DEFEAT",
    "YOU'RE A NOBODY",  "SIT DOWN AND SHUT UP",
    "EVERYONE'S TIRED OF YOUR BS", "I'M YOUR GOD CUCK", "YOU ALR LOST LMFAOP",
    "NOTHING YOU DO WILL WORK", "KEEP HIDING BEHIND YOUR SCREEN", "YOUR LIFE'S A JOKE",
    "I'M UR OWNER, YOU'RE ASS", "SAY SOMETHING",
    "COME CHALLENGE ME", "YOUR WHOLE EXISTENCE IS TO SERVE ME","HOW ARE YOU USING A SKIDDED CLIENT AND STILL SLOW WTF 😂 "
    "SHUT THE FUCKUP", "UR A BITCH", "LOL", "SHUT YO LAME ASS UP NIGGA",
    "DONT FOLD", "DORK ASS CUNT", "FUCK ASS BITCH",
    "SMD HEADASS NIGGA LMFAO UR WORTH NOTHING TO ME", "UR MY BITCH",
    "FUCK ASS NIGGA", "?", "UR MY SEED", "UR A HOE", "NIGGA U DIED TO ME",
    "IM FASTER THEN U SON", "UR A NERD", "🤓", "DONT STEP TO ME AGAIN",
    "NIGGA FOLDED TO ME", "PIPE THE FUCK DOWN", "I OWN U SON", "UR SLOW",
    "UR A BITCH", "LMFAO", "I DONT KNOW U", "FUCK ASS CUNT", "NIGGA TRIED STEPPING",
    "HOW DID U GET HOED LIKE THAT", "DUMB ASS BITCH", "I DONT FOLD",
    "SHUT THE FUCK UP", "TRY STEPPING AGAIN", "UR A BITCH",
    "DUMB ASS NIGGA", "DUMB ASS BITCH THOUGHT HE COULD STEP",
    "OUT LAST ME I NEVER DIE", "COME DIE TO ME NIGGA", 
]

@bot.command(name='ladder')
async def ldr(ctx, member: discord.Member = None):
    global ldr_task


    target = member if member else ctx.author


    await ctx.message.delete()




    async def send_messages():
        while True:
            try:
                
                random.shuffle(bane)

                
                for line in bane:
                   
                    formatted_message = '\n'.join([f"# {word}" for word in line.split()]) + f"\n{target.mention}\n ```DONT FOLD```"

                    
                    if isinstance(ctx.channel, discord.DMChannel): 
                        await ctx.author.send(formatted_message)
                    else:  # Group Chats and Servers
                        await ctx.send(formatted_message)

                    
                    await asyncio.sleep(0.1)

               
                random.shuffle(bane)  

            except asyncio.CancelledError:
                
                print("Task has been canceled.")
                break
            except Exception as e:
                
                print(f"An error occurred: {e}")
                await asyncio.sleep(1)  


    ldr_task = bot.loop.create_task(send_messages())



@bot.command(name='ladderend')
async def stop_ldr(ctx):
    global ldr_task

    if ldr_task and not ldr_task.done():

        ldr_task.cancel()
        await ctx.send("```ladder has been ended```")
    else:
        await ctx.send("```ladderend havent been active```")


insults = [
    "SHUT THE FUCKUP", "UR A BITCH", "LOL", "SHUT YO LAME ASS UP NIGGA",
    "DONT FOLD", "DORK ASS CUNT", "FUCK ASS BITCH",
    "SMD HEADASS NIGGA LMFAO UR WORTH NOTHING TO ME", "UR MY BITCH",
    "FUCK ASS NIGGA", "?", "UR MY SEED", "UR A HOE", "NIGGA U DIED TO ME",
    "IM FASTER THEN U SON", "UR A NERD", "🤓", "DONT STEP TO ME AGAIN",
    "NIGGA FOLDED TO ME", "PIPE THE FUCK DOWN", "I OWN U SON", "UR SLOW",
    "UR A BITCH", "LMFAO", "I DONT KNOW U", "FUCK ASS CUNT", "NIGGA TRIED STEPPING",
    "HOW DID U GET HOED LIKE THAT", "DUMB ASS BITCH", "I DONT FOLD",
    "SHUT THE FUCK UP", "TRY STEPPING AGAIN", "UR A BITCH",
    "DUMB ASS NIGGA", "DUMB ASS BITCH THOUGHT HE COULD STEP",
    "DO SUM LMFAO I RULE U", "SIGN UR LIFE AWAY TO XOM", "EW WHOS THIS UGLY RANDOM ON MY REPLYS?",
    "WHY RU DUCKING?", "COME PACK ME UR SLOW", "USING 1 TOK AND STILL FUCKING THIS DORK LMFAOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "THIS POORON CANT DO SHIT", "SHOW ME UR FUNDS", "LOLLL THIS DORK  CANT DO SHIT TO ME",
    "MY EGO BIGGER THAN YO DICK NIGGA", "LMAO ARENT U A PEDO?", "SHOW ME UR HARDRIVE PEDOO", "WHY ARE YOU SO SLOW LMFAOOO",
    "IM CRYING THIS KID IS GETTING RATE LIMTED", "LMFAO DONT SPEAK TO ME U EDATE SON", "LMFAO ILL TRAP U SON",
    "WHY RU FOLDING TO ME LOL", "U CANT CODE U STAND NO CHANCE AGAINST ME CRY", "LMFAO NICE DUCK KID",
    "CARVE MY NAME INTO UR SKIN CMD OWNS ME", "LOL NICE SKID", "BOW DOWN TO ME WHORE", "I OWN U CUCK",
    "BOW DOWN TO ME", "STOP PACKING", "U LOVE SUCKING ON MY DICK", "UGLY FAN", "DONT STEP I OWN THIS",
    "IM UR GOD", "U USE GRABIFY TO DOX LMFAO", "CUT 4 ME SLUT", "UR SLOW", "U CANT DO NOTHING",
    "I OWN U WHORE CMD29", "HANG URSELF JEW", "I DONT FOLD UR MY HOE", "UR PC IS SLOW",
    "NIGGAS DUCKING LMFAO", "L FUCKING PRESS CUTWHORE", "DORKS I OWN THIS CHAT", "WHY IS THIS NIGGA CRYING LOL",
    "U CANT HARM ME",  "STREAM UR DEATH", "ILL RAIL UR BITCH",
    "UR E GIRL CALLS ME DADDY LMFAO UR WORTHLESS", "OH MY GOOD LOOKING WHORE", "KEEP TYPING SO I CAN EXILE U",
    "WHY ARE YOU SO SLOW IM USING 1 ACC LOL", "BITCHLESS NIGGA HAD TO GET HIS E FRIENDS", "UR SAD AND WORTHLESS",
    "U AMOUNT TO NOTHING", "I RULE YOU", "I HOE U", "YOUR LIFE IS WORTHLESS UR PACKS ARE SLOW LOG OUT",
    "THIS NEVER STOPS", "gayest shit i seen all year", "THIS KID IS OWNED", "WHY CANT U FIGHT BACK",
    "CMD29 OWNS YOU CUCK", "FUCK ASS DORK U CANT DO SHIT", "WHO THIS BITCH THINK HE IS", "WHY ARE YOU DUCKING?",
    "COME CRY TO DADDY", "NIGGAS CANT DO SHIT", "ACCEPT UR FATE", "I KILLED U", "NICE RUN",
    "KID CANT DO SHIT HES CRYING",  "IMA BEAM U", "STOP REPPING UR SHITTY CLAN",
    "WHY ARE YOU SO UNKNOWN", "COME DO SOMETHING", "OD ON PAINKILLERS",
    "WHY ARE U SO SHITTY", "UR POOR AND CANT DO SHIT", "COME DO SOMETHING", "I RUN THIS SHIT",
    "YOU'RE A FAILURE", "STAY SILENT, I OWN YOU", "DON'T PACK ME AGAIN", 
    "YOU'RE DONE", "KEEP TALKING JR", "MY MOM TYPES FASTER THAN THIS WHAT THE FUCK LMFAOO", 
    "YO FATASS CANT TYPE", "UR MY HOE", 
    "YOU'RE THE SLUT OF THIS SERVER", "YOU'RE PATHETIC", 
    "YOU'LL NEVER BE GOOD ENOUGH", "KEEP CRYING", "I'LL TAKE EVERYTHING FROM YOU",
    "YOU'RE EMBARRASSING YOURSELF", "YOUR BEST IS STILL TRASH", "BOW DOWN AND ACCEPT DEFEAT",
    "YOU'RE A NOBODY",  "SIT DOWN AND SHUT UP",
    "EVERYONE'S TIRED OF YOUR BS", "I'M YOUR GOD CUCK", "YOU ALR LOST LMFAOP",
    "NOTHING YOU DO WILL WORK", "KEEP HIDING BEHIND YOUR SCREEN", "YOUR LIFE'S A JOKE",
    "I'M UR OWNER, YOU'RE ASS", "SAY SOMETHING",
    "COME CHALLENGE ME", "YOUR WHOLE EXISTENCE IS TO SERVE ME","HOW ARE YOU USING A SKIDDED CLIENT AND STILL SLOW WTF 😂 "
]

import discord
import asyncio
import random
from discord.ext import commands

# Sample list of insults (you can replace this with your actual list of insults)
insults = [
    "You're so dumb, you make a rock look like a genius.",
    "Is that your face, or is your neck blowing a bubble?"
]

# Task to continuously send insults
async def pl_task_function(channel, target):
    """
    Continuously send insults to the target in the given channel.
    """
    while True:
        try:
            # Prepare a batch of 10 insults
            batch = random.sample(insults, 10)

            # Format messages for the target
            messages = [
                f"# _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n  #  {insult} \n {target.mention if hasattr(target, 'mention') else target}"
                for insult in batch
            ]

            
            await asyncio.gather(*(channel.send(message) for message in messages))

           
            await asyncio.sleep(0.5)  

        except Exception as e:
            print(f"Error occurred during insult loop: {e}")
            await asyncio.sleep(0.01)  

@bot.command(name='flood')
async def pack(ctx, target: str = None):
    await ctx.message.delete()

    if target is None:
        await ctx.send('```mention a user to flood```')
        return

    global pl_task
    if pl_task and not pl_task.done():
        await ctx.send("```flood is already active```")
        return

    # Determine the target member
    if isinstance(ctx.channel, discord.DMChannel): 

        member = ctx.author
        channel = ctx.channel  
    elif isinstance(ctx.channel, (discord.TextChannel, discord.GroupChannel)):  
        try:
            # Try to convert the target into a member
            member = await commands.MemberConverter().convert(ctx, target)
            channel = ctx.channel  # Use the current text channel
        except commands.MemberNotFound:
            await ctx.send('[Invalid]: Could not find the specified user.')
            return
    else:
        await ctx.send('[Invalid]: Unsupported channel type.')
        return

    # Start the task to flood insults in the specified channel
    pl_task = asyncio.create_task(pl_task_function(channel, member))
    await ctx.send(f"Started flooding {member.mention if hasattr(member, 'mention') else member} with insults.")



@bot.command(name='prefix')
async def prefix(ctx, new_prefix=None):
    await ctx.message.delete()
    if new_prefix is None:
        await ctx.send(f'```[Invalid]: Its {bot.command_prefix}prefix <prefix>```')
        return
    bot.command_prefix = str(new_prefix)
    await ctx.send(f'```Prefix changed to {new_prefix}```')

@bot.command(name='floodend')
async def sa(ctx):
    global pl_task

    if pl_task and not pl_task.done():
        pl_task.cancel()
        pl_task = None
        await ctx.send("```flood has been stopped```")













ladder_messages = [
"https://media.discordapp.net/attachments/1306742094529826886/1307776610585542686/caption.gif?ex=676aff61&is=6769ade1&hm=38e79e5a0e8018e4e3ec94dbe64e80aa359b3e524c5d63d56eda63cad7e0d8d2&=&width=312&height=586"
]
message_index = 0  


@bot.command(name='ping')
async def pr(ctx):
    global is_pr_active

    
    if is_pr_active:
        await ctx.send("")
        return

    # Activate the PR command
    is_pr_active = True
    await ctx.send("```ping responder is online```")

    def check_interaction(message):
        
        return (
            (ctx.author.mentioned_in(message) or message.reference and message.reference.resolved.author == bot.user)
            and message.author != bot.user
        )

    while is_pr_active:
        try:
            # Wait for a ping or a reply
            message = await bot.wait_for('message', check=check_interaction)
            global message_index

            # Respond with the next message in the ladder and ping the triggering user
            await message.channel.send(f"{ladder_messages[message_index]} {message.author.mention}")
            message_index = (message_index + 1) % len(ladder_messages) 

        except asyncio.CancelledError:
            break


@bot.command(name='endping')
async def ps(ctx):
    global is_pr_active

    if is_pr_active:
        is_pr_active = False
        await ctx.send("```ping responder is offline```")
    else:
        await ctx.send("```ping responder is offline```")



@bot.command()
async def stopstream(ctx):

    try:
        await bot.change_presence(activity=None)  
        await ctx.send("```stopped successfully```")
    except Exception as e:
        await ctx.send(f"Failed to stop streaming: {e}")

@bot.command()
async def stream(ctx, *, activity: str):
    
    try:
        
        await bot.change_presence(activity=discord.Streaming(name=activity, url="https://www.twitch.tv/aa"))
        await ctx.send(f"```stream started as: {activity}```")
    except Exception as e:
        await ctx.send(f"Failed to set streaming status: {e}")




@bot.command()
async def playing(ctx, *, activity: str):

    try:
        await bot.change_presence(activity=discord.Game(name=activity))
        await ctx.send(f"Playing: {activity}")
    except Exception as e:
        await ctx.send(f"Failed to set playing status: {e}")


async def set_streaming_status(message):

    formatted_message = "\n".join(message.split(",")[:10]) 
    await bot.change_presence(
        activity=discord.Streaming(name=formatted_message, url="https://twitch.tv/aa")
    )




@bot.command()
async def av(ctx, user: discord.User = None):
    
    try:
        user = user or ctx.author
        await ctx.send(user.avatar_url) 
    except Exception as e:
        await ctx.send(f"Failed to fetch avatar: {e}")










@bot.command(name='afk')
async def af(ctx, member: discord.Member):

    
    for i in range(10, -1, -1):
        await ctx.send(f"{member.mention} u died to xom say here kid")
        await ctx.send(i)
        await asyncio.sleep(0.1)  


    await ctx.send(f"LMFAO U FOLDED {member.mention}")



@bot.remove_command('help') 






@bot.command()
async def menu(ctx):
    # Send the first part of the menu (loading part)
    menu_message = await ctx.send("""```
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⣆⠀⠀⠀⠀⠀⣠⡀ ᶻ 𝗓 𐰁 .ᐟ ⣼⣿⡗⠀⠀⠀⠀
⠀⠀⠀⣠⠟⠀⠘⠷⠶⠶⠶⠾⠉⢳⡄⠀⠀⠀⠀⠀⣧⣿⠀⠀⠀⠀⠀
⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣤⣤⣤⣤⣤⣿⢿⣄⠀⠀⠀⠀
⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠙⣷⡴⠶⣦
⠀⠀⢱⡀⠀⠉⠉⠀⠀⠀⠀⠛⠃⠀⢠⡟⠀⠀⠀⢀⣀⣠⣤⠿⠞⠛⠋
⣠⠾⠋⠙⣶⣤⣤⣤⣤⣤⣀⣠⣤⣾⣿⠴⠶⠚⠋⠉⠁⠀⠀⠀⠀⠀⠀
⠛⠒⠛⠉⠉⠀⠀⠀⣴⠟⢃⡴⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    
                             version 1.1

                        welcome to muz's client.
    
    ```""")
    
    await ctx.send(f"```hello {ctx.author.name} welcome to muzs client enter your current device down below ```\n``` pc   or   mobile  ```")


    def check(m):
        return m.author == ctx.author


    message = await bot.wait_for('message', check=check)

    if message.content.lower() == 'pc':
        await ctx.send(f"""``` 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⠂⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⠂⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⠉⠛⢿⡏⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⢀⠀⢠⠀⠀⠀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣍⠙⠶⣦⣸⣷⣿⣤⡾⠿⢋⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣷⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠉⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠈⠙⠛⠻⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢻⣿⣿⣿⣿
⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿
⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠋⣁⣴⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠈⠙⠻⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿
⣿⠁⡄⠀⠀⠀⠀⠀⢀⣠⣶⡟⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠛⠁⣀⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⡈⠙⠓⠄⠀⠀⠀⠀⠀⠀⠀⢠⣀⡀⠀⠀⠀⠀⠀⠀⢧⡈⣿
⣿⣾⠁⠀⠀⠀⣠⣶⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⣠⡴⠚⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠙⠲⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⣶⣤⣀⠀⠀⢸⣿⣿
⣿⣿⠀⠀⢠⣾⣿⣿⣿⠏⢀⡀⠀⠀⠀⠀⠀⠀⣠⡶⠋⠁⠀⠀⠀⠀⠙⠿⣿⣿⣿⠉⠉⠉⢹⣿⣿⡿⠛⠁⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣶⣜⣿⣿
⣿⣿⣆⣴⣿⣿⣿⣿⣷⣾⣿⠏⠀⠀⠀⢀⣴⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⣀⣹⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⢀⣴⣿⡟⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣧⡀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
``````                                       the city needs me...```
""")
        await ctx.send(f"""

```
                                           x1   [multiclients]
                                           x2   [singleclient]
                                           x3   [richpresence]
                                           x4    [trollings]
                                           x5    [reactions]
                                           x6     [support]
                                           x7     [utility]
                                           x8      [mass]                ``````
    
                          ⠁⠀⠀⠀⠀⠀⠀⢸⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⡀⠀⣰⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣤⣴⣶⣾⣿⣿⣿⣿⣿⡿⠁⠀⠈⠻⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⣴⢟⣶⡿⢿⣿⣿⣿⣿⣆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠙⣿⡏⠀⠀⠘⣯⡉⠉⠹⣧⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣾⣯⠟⠀⢰⣿⠀⠀
⠀⠀⠀⠀⡀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣤⣿⡃⠀⠀
⠀⠀⠀⠈⠉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⠉⠀
⠀⠀⠀⠀⣤⠴⣿⣿⣿⣿⣿⣿⣌⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠉⣨⣿⣿⣿⣿⣿⡿⠤⡤⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡟⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠛⢻⣿⣿⣿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠞⠛⠙⢿⣿⣷⠀⠀⠀⠀⠀⠈⠉⠛⠟⠛⠉⠁⠀⠀⠀⠀⠀⣾⣿⠿⠋⠛⠒⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢻⣷⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣤⣾⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡿⠛⢻⣿⠛⠛⢛⡿⠛⢛⠛⢿⡛⠋⠙⢿⡟⠻⢷⣦⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣿⠁⠀⢰⡿⠁⠀⠾⠿⡿⢶⣿⣶⡿⠿⠶⠀⠈⢷⡀⠀⠙⣿⣷⣄⠀⠀⠀
⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣦⣿⠁⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠸⣧⣴⣿⣿⣿⢿⣧⠀⠀
⠀⠀⠀⢀⣿⣿⣟⠿⣿⣿⣿⣿⣉⣉⣟⣉⣉⣹⣋⣉⣹⣏⣉⣉⣏⣉⣹⣿⣿⣿⣿⢟⣿⣿⣧⠀
⠀⠀⠀⣸⣿⣿⣿⣿⣶⣿⣹⡿⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⢿⡟⣦⣶⣿⣿⣿⣿⡆
⠀⠀⠀⣿⠿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢠⡀⠀⠙⢻⣿⠟⠉⠀⢀⠀⠀⠀⢸⣷⣿⣿⣿⣿⣿⢿⡇
⠀⠀⠀⠉⠀⡿⠁⠀⢻⡿⢿⣧⣤⣴⣿⣷⣦⣤⣴⣿⣤⣤⣴⣾⣷⣤⣤⣼⡿⣿⡏⢻⡏⣿⠘⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠈⡃⠀⠁⠋⠀⠀       
                                                   ```                     
""")
    elif message.content.lower() == 'mobile':
        await ctx.send(f"""
```made by muz i love all of you <3``````
[x1]      (multi clients)
[x2]      (single client)  
[x3]      (rich prencese) 
[x4]       (trollings) 
[x5]       (reactions)
[x6]        (support) 
[x7]        (utility) 
[x8]        (profile)```                      
 """)
        await ctx.send(f"""https://media.discordapp.net/attachments/1327820121992855573/1327836013694943354/d22df5da1c7be7401dd981db899d9f85.gif?ex=67848327&is=678331a7&hm=ebca000f494720f5cc0a1023fe5e5240e982f27478c1c3c3feb0aa448572804f&=&width=525&height=350""")

    await message.delete()


    await menu_message.delete()

@bot.command()
async def x1(ctx):
    await ctx.send(f"""
```x1 (multi clients)``````
[1]  multilast
[2]  stoplast
[3]  exile
[4]  stopexile
[5]  fill
[6]  kill
[7]  killend
[8]  rpcall
[9]  token
[10] rename```
""")

@bot.command()
async def x2(ctx):
    await ctx.send(f"""```x2  (single client)``````
[1]  flood
[2]  floodend        
[3]  ar                 
[4]  arend
[5]  ladder                                   
[6]  ladderend                  
[7]  outlast                   
[8]  endlast                  
[9]  ping
[10] endping
[11] spam
[12] antitrap
[13] afkoff
[14] afkcheck
[15] afk  - second afkcheck
[16] ap  - working on
[17] apoff                                                                                                                                                                    
[18] deltrap  - working on
[19] enddel                                  ```""")


@bot.command()
async def x3(ctx):
    await ctx.send(f"""```x3  (rich prencese) ``````
[1]  rpc
[2] stoprpc
[3] stream
[4] stopstream
[5] playing
```""")


@bot.command()
async def x4(ctx):
    await ctx.send(f"""```x4    (trollings) ``````
[1]  swat                   
[2]  hack                   
[3]  dick                 
[4]  gay                                   
                   ```""")


@bot.command()
async def x5(ctx):
    await ctx.send(f"""```x5    (reactions)``````
[1]  react      <@user> <emoji>           
[2]  stop
react                                 
                   ```""")


@bot.command()
async def x6(ctx):
    await ctx.send("```contact muz for help issues or questions```")

@bot.command()
async def x7(ctx):
    await ctx.send(f""""```x7     [utility]``````
[1]  prefix
[2]  reload                
[3]  av
[4]  banner - not working idk why
[5]  python - only used  by  muz
[6]  purge ```""")

@bot.command()
async def x8(ctx):
    await ctx.send(f"""```x8     [massdm]``````
[1]  massdm - use only on mobile and use the cmd on a priv server or gc not dms                
[2]  massgc                 
[3]  massunadd                                    
                   ```""")














outlast_active = False
outlast_task = None

# Wordlist
wordlist = [
"hey\nweak\ndork\nboy\nwya\ni\ncant\nhear\nyou\nspeak\na\nbit\nfaster\nson",
"YO\nQUEER\nARE\nYOU\nSTEPPING\nTO\nDIE\nTO\nME?\nMOVE\nFUCKBOY",
"ILL\nBLOW\nUR\nGIRLS\nSPINE\nOUT\nFAT\nCUCK",
"LLMFAO\nISNT\nUR\nMOTHER\nA\nSTRIPPER?\nLOLLLLLLLLLLL",
"KID\nDONT\nFOLD\nGET\nUP\nAND\nCOME\nKILL\nME\nUR\nFUCKING\nDYING\nRIGHT\nNOW\nDORK",
"I\nSAID\nSTEP\nTHE\nFUCK\nUP\nUR\nBORING\nME\nU\nWEAK\nMUTT",
"POORON\nU\nDIED\nTO\nA\nCLIENT\nAND\nWILL\nDIE\nIN\nMANAUL\nIF\nYOU\nNEED\nSOME\nHELP\nDM\MUZ\nLMFAO\nHE\nMIGHT\nHELP\nUR\nWEAK\nASS",
"YO\nFEMBOY\nSHUT\nTHE\nFUCK\nUP",
"MORON\nUR\nMY\nFUCKING\nJR\nU\nWILL\nNEVER\nBE\nFASTER\nTHAN\nME\nLOL",
"TALK\nUR\nSHIT\nU\nWEAK\nASS\nRANDOM\nILL\nFUCKING\nKILL\nYOU",
"I\nCAN\nTURN\nUR\nWHOLE\nFAMILY\nINTO\nMY\nSLAVES",
"THIS\nPOOR\nKID\nLIVES\nIN\nA\n5FT\nHOUSE\nLMFAOOOOOOOOOO",
"STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n STFU U DIED TO ME GET FLOODED DORK BOY\n ",
"NICE\nRUN\nJRR",
"YOU\nDIED\nLAST\nWORD.",
  "YOU\nDORK\nASS\nRUNT\nDONT\nSTEP\nTO\nYOUR\nFOUNDER\n",
  "MUZ\nMURDERD\nYOU\nLMFAO\nYOUR\nSO\nWEAK\n",
  "RETARDED\nMORON\nHAIL\nMUZ\nLOL\nUR\nFUCKING\nWORTHLESS\n",
  "YO\nCUCK\nDONT\nSTEP\nTO\nUR\nFATHER\nAGAIN\nILL\nHUMBLE\nYOU\nRETARD\n",
  "ILL\nSTEP\nON\nUR\nBITCH\nLMFAO\nCOME\nKILL\nME\nGET\nPAY\nBACK\nYOU\nWEAK\nFUCK\n",
  "COME\nHERE\nILL\nCHOKE\nYOU\n",
  "GET\nDROWNED\nBY\nUR\nGOD\n",
  "GET\nTHE\nFUCK\nDOWN",
  "ILL\nFUCKING\nMURDER\nYOU\nWEAK\nSKID",
  "SHOW\nYOUR\nFUNDS\nWEAK\nPOORON",
  "SHUT\nTHE\nFUCK\nUP\nRANDOM\nFEMBOY",
  "I\nTURN\nUR\nBITCH\nINTO\nMY\nSLUT",
  "YOUR\nMOM\nCUTS\nFOR\nME",
  "ILL\nNEVER\nFOLD\nOR\nDIE\nHAIL\nMUZ",
  "DID\nU\nDIE\nSO\nQUICK",
  "PATHETIC\nSLOW\nBOY",
  "UR\nCLIENT\nIS\nSHIT",
  "YOUR\nFUCKING\nSTRUGGLING\nTO\nLIVE",
  "BREATHE\nMY\nWEAKEST\nCHILD",
  "ILL\nRIP\nYOUR\nINTESTINES\nOUT\nAND\nFEED\nIT\nTO\nMY\nDOG",
  "YOUR\nA\nWEAK\nSKID\nASS\nNIGGA\nLOL\nUR\nFUCKING\nRETARDED\nYOU\nBUY\nSCRIPTS\nAND\nSTILL\nDIE\nYOU\nMORON",
  "YOUR\nA\nPUSSY\nASS\nKID\nWHY\nDID\nU\nSTEP\nAND\nGOT\nPUT\nTHE\nFUCK\nDOWN",
  "STEP\nTHE\nFUCK\nDOWN\nBEFORE\nA\nREAL\nSTEPPER\nMURDERS\nYOU\nUR\nMY\nLAB\nDOG\nBARK\nFOR\nUR\nGOD\nYOU\nFEMBOY\nYOU\nHAVE\nA\nCUCK\nKINK",
  "YOUR\nEGO\nDIED\nAFTER\nI\nKILLED\nUR\nSHIT\nTOKENS\nYOUR\nADDICTED\nTO\nDYING\nBY\nMUZ\nYOU\nFUCKUP\nDORK",
  "DO\nYOU\nWANT\nMY\nWORD\nLIST\n?\nLOL\nU\nMIGHT\nNEED\nIT\nU\nUSE\nCHAT\nGPT\nTO\nGIVE\nU\nWORDS",
  "SHUT\nUP\nBROKE\nASS\nKID",
  "I\nFEEL\nBAD\nBUT\nI\nHAVE\nTO\nSHOW\nYOU\nWHO\nUR\nGOD\nIS",
  "LETS\nGO\nTO\nWAR\nWATCH\nU\nDIE\nWEAK\nFUCK",
  "YOU\nWILL\nNEVER\nGET\nA\nBITCH\nAND\nIF\nU\nDO\nU\nWILL\nMAKE\nHER\nPUSSY\nDRY",
  "STFU\nYOU\n1WPM\nWARRIOR\nUR\nSAD\nAS\nSHIT",
  "ILL\nNEVER\nDIE\nKEEP\nGOING\nTILL\nYOUR\nBONES\nDECAY\nMY\nCLIENTS\nCAN\nOUTLAST\nYOUR\nWORTHLESS\nLIFE",
  "SHUT\nUP\nYOU\nLOW\nTIER\nRETARD",
  "you\ndied\nto\na\ngod\nlol\nits\nokay\njrs\nlike\nyou\nalways\nfail\nme", 
  "YOU\nDISAPOINTED\nME\nI\nWANTED\nTO\nGO\nLONGER",
  "SAY\nIT\nWITH\nYOUR\nCHEST\nYOU\nCANT\nHANDLE\nTHE\nGREATEST",
]


@bot.command()
async def outlast(ctx, *args):
    global outlast_active, outlast_task

    
    if not args:
        await ctx.send("```Please mention a user or provide a valid user ID.```")
        return

    
    user_mentioned = None

    if len(args) == 1:
        arg = args[0]
        
        
        if arg.startswith("<@") and arg.endswith(">"):
            user_mentioned = arg  
        else:
          
            user_mentioned = f"<@{arg}>"

    if not user_mentioned:
        await ctx.send("```Could not resolve user mention or ID. Please try again.```")
        return

 
    if outlast_active:
        await ctx.send("```Outlast is already active```")
        return

   
    outlast_active = True

    async def outlast_messages():
        while outlast_active:
            try:
                response = random.choice(wordlist)

        
                await ctx.send(f"{response}\n{user_mentioned}")

                await asyncio.sleep(0.1)

            except asyncio.CancelledError:
                break
            except Exception as e:
                print(f"Error: {e}")

    
    outlast_task = asyncio.create_task(outlast_messages())

@bot.command()
async def endlast(ctx):
    global outlast_active, outlast_task

    if outlast_active:
        outlast_active = False
        if outlast_task:
            outlast_task.cancel()
            await ctx.send("```Outlast has been stopped.```")



@bot.command()
async def purge(ctx, amount: int):
    if amount < 1 or amount > 100:
        await ctx.send("```Please provide a number between 1 and 100 for the number of messages to delete.```")
        return

    await ctx.message.delete()


    if isinstance(ctx.channel, discord.TextChannel):
      
        messages = await ctx.channel.history(limit=amount + 1).flatten()

        
        await ctx.channel.bulk_delete(messages)

        confirmation_message = await ctx.send(f"```Deleted {amount} messages.```")
        await asyncio.sleep(0.1)
        await confirmation_message.delete()


    elif isinstance(ctx.channel, discord.DMChannel):
     
        messages = await ctx.channel.history(limit=amount).flatten()

        bot_messages = [msg for msg in messages if msg.author == bot.user]
        for msg in bot_messages:
            await msg.delete()

        confirmation_message = await ctx.send(f"```Deleted {len(bot_messages)} messages.```")
        await asyncio.sleep(0.1)
        await confirmation_message.delete()

    elif isinstance(ctx.channel, discord.GroupChannel):
  
        messages = await ctx.channel.history(limit=amount).flatten()

        deleted_count = 0
        for message in messages:
            if message.author == bot.user:
                await message.delete()
                deleted_count += 1

        confirmation_message = await ctx.send(f"```Deleted {deleted_count} bot messages in the group chat.```")
        await asyncio.sleep(0.1)
        await confirmation_message.delete()









@bot.command()
async def massdm(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'```[Invalid]: It\'s, {bot.command_prefix}massdm <message>```')
        return  
    for friend in bot.user.friends:
        try:
            await friend.send(message)
            print(f"message sent to {friend.name}#{friend.discriminator}")
        except discord.Forbidden:
            print(f"Failed to send message to {friend.name}#{friend.discriminator} (blocked or dms are off)")
        except Exception as e:
            print(f"error sending message to {friend.name}#{friend.discriminator}: {e}")
        await asyncio.sleep(4.0)

@bot.command()
async def massgc(ctx, *, message: str):

    global massgc_task

    if massgc_task and not massgc_task.done():
        await ctx.send("```use stopmass to cancel```")
        return

    async def dm_group_chats():
        try:
            group_chats = [gc for gc in bot.private_channels if isinstance(gc, discord.GroupChannel)]
            for gc in group_chats:
                try:
                    await gc.send(message)
                    await asyncio.sleep(0.50)  
                except Exception as e:
                    print(f"Could not send message to group chat {gc}: {e}")
            await ctx.send("Mass GC DM completed.")
        except Exception as e:
            await ctx.send(f"Error during mass GC DM: {e}")

    massgc_task = asyncio.create_task(dm_group_chats())
    await ctx.send("```message sending to all groupchats.```")


@bot.command(name='massunadd')
async def massunadd(ctx):

    try:
        
        friends = bot.user.friends

        if not friends:
            await ctx.send("```You have no friends to unadd.```")
            return

        await ctx.send(f"```Starting to unfriend {len(friends)} users...```")

        
        for friend in friends:
            await friend.remove_friend() 
            await asyncio.sleep(1)  
        
        await ctx.send("```Successfully unfriended all users.```")

    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")   

@bot.command()
async def stopmass(ctx):

    global massdm_task, massgc_task

    if massdm_task and not massdm_task.done():
        massdm_task.cancel()
        await ctx.send("```massdm pasued```")
    else:
        await ctx.send("```no massdm command is running```")

    if massgc_task and not massgc_task.done():
        massgc_task.cancel()
        




@bot.command()
async def swat(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author

    gender = ["Male", "Female", "Non-Binary", "Other"]
    age = str(random.randint(18, 50))
    height = ['5\'5\"', '5\'8\"', '6\'0\"', '6\'2\"']
    location = ["1305 Tarragon Dr Flower Mound, Texas(TX), 75028", "28261 W Thome Rd Rock Falls, Illinois(IL), 61071", "1508 2nd St NW Bowman, North Dakota(ND), 58623", "60 Gertrude Rd Dalton, Massachusetts(MA), 01226",]
    occupation = ["Software Engineer", "Artist", "Teacher", "Chef"]
    name = ['Alex Johnson', 'Jamie Lee', 'Taylor Smith', 'Jordan Brown']

    await ctx.send(f"swatting {user.mention}...\n")
    await asyncio.sleep(1)

    await ctx.send(f"```📞 *9-1-1: Hello, what is ur emergency*```")
    await asyncio.sleep(1)

    await ctx.send(f"{user.mention} my name is {random.choice(name)} i am very scared my parents were fighting and then i heard a big band like a bomb. . . .")
    await asyncio.sleep(1)
    
    await ctx.send(f"📞 okay calm down and get somewhere safe were do you live?")
    await asyncio.sleep(1)

    await ctx.send(f"i- i live at {random.choice(location)} please hurrry ")
    await asyncio.sleep(1)

    await ctx.send(f"📞 SWAT is coming shortly remain safe we will arrive soon")
    await asyncio.sleep(1)


    await ctx.send(f"🚓 SWAT: starts breaking down {user.mention} door ")
    await asyncio.sleep(1)

    await ctx.send(f"https://media.discordapp.net/attachments/1310177406732075101/1312274470504890421/b9b7b37cb0cf5e495d6512d30c56a4fb.gif?ex=674be656&is=674a94d6&hm=139874281c9b4d402eab13afd0669cd07505a18147aea95fa75277706ca32da5&=")
    await asyncio.sleep(1)
                        
    await ctx.send(f"🚓 SWAT: YOUR UNDERARRESTRED {user.mention}  ")
    await asyncio.sleep(1)

    await ctx.send(f"🚓 SWAT: targets {user.mention}")
    await asyncio.sleep(1)

    await ctx.send(f"{user.mention} I DIDN'T DO ANYTHING HELP \n")
    await asyncio.sleep(1)

    await ctx.send(f"🚓 SWAT: GET DOWN ON THE FLOOR {user.mention}")
    await asyncio.sleep(1)

    await ctx.send(f"{user.mention} I DIDNT DO ANYTHING HELP \n")
    await asyncio.sleep(1)


    await ctx.send(f"*🚓 SWAT: locks up {user.mention}*")
    await asyncio.sleep(1)

    await ctx.send(f"Successfully swatted {user.mention} \n")
    await asyncio.sleep(1)
    
    await ctx.send(f"```Details:```"
                   f"```Name: {random.choice(name)}\n"
                   f"Gender: {random.choice(gender)}\n"
                   f"Age: {age}\n"
                   f"Height: {random.choice(height)}\n"
                   f"Location: {random.choice(location)}\n"
                   f"Occupation: {random.choice(occupation)}\n```")


@bot.command()
async def nitro(ctx, amount: int=None):
    await ctx.message.delete()
    if amount is None:
        await ctx.send(f'{bot.command_prefix}nitro <amount>')
        return
    for _ in range(amount):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        await ctx.send(f'https://discord.gift/{code}')
        await asyncio.sleep(0.50)


 



@bot.command()
async def dick(ctx, member: discord.Member = None):
    # If no member is mentioned, it will simply continue without mentioning anyone
    member = member or ctx.author  # Default to the author if no member is provided

    length = random.randint(1, 20)

    pp_string = "3" + "=" * length + "D"

    await ctx.send(f"```{pp_string} {member.mention}  {length} inches```")


@bot.command() 
async def gay(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("```mention a user for the command to work properly```")
        return

    gay_percent = random.randint(1, 100)  # Generate a random percentage
    response = f"`{member.mention} is {gay_percent}% gay`"
    await ctx.send(response)

@bot.command()
async def hack(ctx, user: discord.Member=None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
    content=f"```Successfully hacked {user}\n"
            f"Name: {random.choice(name)}\n"
            f"Gender: {random.choice(gender)}\n"
            f"Age: {age}\n"
            f"Height: {random.choice(height)}\n"
            f"Weight: {weight}\n"
            f"Hair Color: {random.choice(hair_color)}\n"
            f"Skin Color: {random.choice(skin_color)}\n"
            f"DOB: {dob}\n"
            f"Location: {random.choice(location)}\n"
            f"Phone: {phone}\n"
            f"E-Mail: {user.name + random.choice(email)}\n"
            f"Passwords: {', '.join(random.choices(password, k=3))}\n"
            f"Occupation: {random.choice(occupation)}\n"
            f"Annual Salary: {random.choice(salary)}\n"
            f"Ethnicity: {random.choice(ethnicity)}\n"
            f"Religion: {random.choice(religion)}\n"
            f"Sexuality: {random.choice(sexuality)}\n"
            f"Education: {random.choice(education)}\n"
            "```"
)






@bot.command()
async def python(ctx, *, script_name: str):
    
    try:

        if not script_name.endswith('.py'):
            await ctx.send("```add .py at the end```")
            return
       
        if not os.path.isfile(script_name):
            await ctx.send(f"```Script {script_name} isnt in vsc```")
            return

        
        subprocess.Popen(["python", script_name])
        await ctx.send(f"```starting {script_name}```")

    except Exception as e:
        await ctx.send(f"Failed to start script: {e}")

@bot.command()
async def banner(ctx, user: discord.User):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://discord.com/api/v9/users/{user.id}', headers={'Authorization': bot.http.token}) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    banner_id = data.get('banner')
                    if banner_id:
                        banner_url = f'https://cdn.discordapp.com/banners/{user.id}/{banner_id}.{"gif" if banner_id.startswith("a_") else "png"}?size=1024'
                        await ctx.send(banner_url)
                    else:
                        flags = data.get('public_flags', 0)
                        has_nitro = flags & (1 << 9)
                        
                                                
                        if has_nitro:
                            default_banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{user.discriminator}.gif"
                            await ctx.send(default_banner_url)
                        else:
                            await ctx.send("This user doesn't have a banner.")
                else:
                    await ctx.send(f"Failed to fetch user data. Status code: {resp.status}")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")      




react_targets = {}

@bot.command()
async def react(ctx, user: discord.User, emoji: str):
    react_targets[user.id] = emoji
    await ctx.send(f"```Started reacting to {user.mention} with {emoji}```")


@bot.command()
async def stopreact(ctx):
    react_targets.clear()
    await ctx.send("```stopped reacting to user```")


@bot.event
async def on_message(message):

    if message.author.bot:
        return


    if message.author.id in react_targets:
        await message.add_reaction(react_targets[message.author.id])


    await bot.process_commands(message)









bot.run('', bot=False) 