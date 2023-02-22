try:
    import discord
    from discord.ext import commands
    from config import token, prefix_bot




    bot = commands.Bot(command_prefix=prefix_bot, intents=discord.Intents.all())




    @bot.event
    async def on_ready():
        await bot.load_extension("cogs.compiler")
        print(f"Compiler pret!")



        

    bot.run(token) 
    
except:
    print("Une erreur est survenue lisez bien le readme.txt")








    
    







    
    


