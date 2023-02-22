import os
import json
import requests
import discord
from discord.ext import commands
from discord import app_commands


class Compiler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(name="run")
    async def run(self, ctx, *, args=None):
        code = args
        if not code: return
        async def transforme(ctx, code):
            code = code.split("\n")
            #print(code)
            if code[0] == '```' or code[0] == '```py':
                del code[0]
                e = len(code)
                e -= 1
                del code[e]

            mess = ""
            for a in code:
                mess = mess+a+"\n"
            await compiler(ctx, mess)

        
        


        async def compiler(ctx, code):
            from config import client_id, client_secret
            post_url = 'https://api.jdoodle.com/v1/execute'

            resultat = json.loads(requests.post(
                post_url,
                json={
                    "script": code,
                    "language": "python3",
                    "versionIndex": "3",
                    "clientId": client_id,
                    "clientSecret": client_secret
                }
            ).content)
            
            
            
            
            
            try:
                erreur = False 
                general = resultat['output']
            except:
                erreur = True
                 
            if "error" in general.lower():
                
                
                erreur = True
                
                
            if erreur:
                emoji = "❌"
                titre = "❌Erreur❌"
                color = 0xff0000
                
            else:
                emoji = "✅"
                titre="✅Valide✅"
                color=0x80ff80
            
            
            from datetime import datetime
            embed = discord.Embed(title=titre, timestamp=datetime.now(), description=f"```shell\n{general}\n```", color=color)
            mess = await ctx.send(embed=embed)
            await mess.add_reaction(emoji)
            return
            
            
            
        await transforme(ctx, code)

async def setup(bot):
    await bot.add_cog(Compiler(bot))

        


