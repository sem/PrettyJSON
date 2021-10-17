from json.decoder import JSONDecodeError
from discord.ext import commands
import json
import os
from datetime import datetime
from datetime import timedelta
import discord
import asyncio
import requests

class Cog(commands.Cog):   
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready.')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction : discord.Reaction, user):
        if user == self.bot.user: return
        message : discord.Message = reaction.message
        if self.bot.user in await message.reactions[0].users().flatten():
            content : str = message.content
            content = content.removeprefix('```json').removesuffix('```')
            with open('output.json', 'w') as f:
                f.write(content)
            json_data = json.load(open('output.json', 'r'))
            with open('output.json', 'w') as f:
                json.dump(json_data, f, indent=4)
            await message.channel.send(file=discord.File('output.json'))
            await message.remove_reaction('\U0001f4c1', self.bot.user)

    @commands.command()
    async def pretty_print(self, ctx : commands.Context, *, args=None):
        if args != None: args = args.replace('“', '"').replace('”','"')
        if len(ctx.message.attachments) == 0 and len(args) > 0 and not args.startswith('http'):
            with open('output.json', 'w') as f:
                f.write(args)
        elif len(ctx.message.attachments) > 0 and args == None:
            await ctx.message.attachments[0].save('output.json')
        elif len(ctx.message.attachments) == 0 and len(args) > 0 and args.startswith('http'):
            try:
                out_data = requests.get(args).text
            except(requests.exceptions.MissingSchema): 
                await ctx.send('Invalid URL was inserted.')
                return
            try:
                with open('output.json', 'w') as f:
                    f.write(out_data)
                json.load(open('output.json', 'r')) # Attempting a JSON load/conversion of the current data stored in the output.json
            except(Exception):
                await ctx.send('Sorry, but valid JSON could not be obtained from that link, maybe try pretty printing with a file of JSON?')
                return
        data = open('output.json', 'r')
        try: 
            json_data = json.load(data)
        except (JSONDecodeError):
            await ctx.send('The data that was inserted could not be converted to valid JSON. Make sure your data contains the right JSON syntax.')
            return
        with open('output.json', 'w') as f:
            json.dump(json_data, f, indent=4)
        if len(data.read()) > 2000: msg_sent = await ctx.send(file=discord.File('output.json'))
        else: 
            msg_sent = await ctx.send('```json\n' + open('output.json', 'r').read() + '```')
            await msg_sent.add_reaction('\U0001f4c1')

def setup(client): client.add_cog(Cog(client))