#importing discord and other modules from discord
import discord
from discord.ext import commands
import requests


#creating client
intents = discord.Intents.default()
intents.members=True
client = commands.Bot(command_prefix ="#", intents=intents)


#used openweather for the the weather info
api_key = "Enter API key"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


#client function(commands: can be used as an inbuilt function)

#client functions(on getting ready)
@client.event
async def on_ready():
    potato=client.get_channel(857989327702327336)
    await potato.send("Hey, I'm POTATO")


#Help command(green)
@client.command(name="Help")
async def help(ctx):
    
    myEmbed1=discord.Embed(title="Commands available", colour=0x00ff00)
    
    myEmbed1.add_field(name="#Bot", value="Information about the bot", inline=False)
    myEmbed1.add_field(name="#Server", value="Information about the server", inline=False)
    myEmbed1.add_field(name="#WhoIs", value="Information about the person", inline=False)
    myEmbed1.add_field(name="#Weather", value="Information about the weather", inline=False)
    myEmbed1.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    
    await ctx.send(embed=myEmbed1)


#Bot command(blue)
@client.command(name="Bot")
async def botinfo(ctx):
   
    myEmbed2=discord.Embed(title="POTATO", description="Helper Bot", colour=0x0000ff)
   
    myEmbed2.add_field(name="Version", value="Version 1", inline=False)
    myEmbed2.add_field(name="Bulit using", value="Python 3.8.5", inline=False)
    myEmbed2.add_field(name="Builder", value="vinaydesai", inline=False)
    myEmbed2.add_field(name="Created", value=ctx.bot.user.created_at, inline=False)
    myEmbed2.set_thumbnail(url=ctx.bot.user.avatar_url)
    myEmbed2.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    
    await ctx.send(embed=myEmbed2)


#Server command(golden)
@client.command(name="Server")
async def member(ctx):
    
    total_members=len(ctx.guild.members)
    total_bots=len(list(filter(lambda m: m.bot, ctx.guild.members)))
    actual_members=total_members-total_bots
    
    total_voice=len(ctx.guild.voice_channels)
    total_text=len(ctx.guild.text_channels)
    total_roles=len(ctx.guild.roles)
    
    myEmbed3=discord.Embed(title=ctx.guild.name, colour=0xf1c40f)
    
    myEmbed3.add_field(name="Owner", value=ctx.guild.owner, inline=False)
    
    myEmbed3.add_field(name="Members", value=total_members, inline=True)
    myEmbed3.add_field(name="Bots", value=total_bots, inline=True)
    myEmbed3.add_field(name="Real_Members", value=actual_members, inline=True)
    
    myEmbed3.add_field(name="Roles", value=total_roles, inline=True)
    myEmbed3.add_field(name="Voice Channels", value=total_voice, inline=True)
    myEmbed3.add_field(name="Text Channels", value=total_text, inline=True)
    myEmbed3.set_thumbnail(url=ctx.guild.icon_url)
    myEmbed3.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    
    await ctx.send(embed=myEmbed3)


#WhoIs command(orange)
@client.command()
async def WhoIs(ctx, member:discord.Member):
    
    myEmbed5=discord.Embed(title=member.name, description=member.mention, colour=0xe67e22)
    
    myEmbed5.add_field(name="ID", value=member.id, inline=False)
    myEmbed5.set_thumbnail(url=member.avatar_url)
    myEmbed5.add_field(name="Joined", value=member.joined_at, inline=False)
    myEmbed5.add_field(name="Top role", value=member.top_role, inline=False)
    myEmbed5.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    
    await ctx.send(embed=myEmbed5)


#Weather command(purple)
@client.command()
async def Weather(ctx, *, city: str):
    
    #collecting info from openweather
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    y = x["main"]
    current_temperature = y["temp"]
    current_temperature_celsiuis = str(round(current_temperature - 273.15))
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    
    myEmbed6 = discord.Embed(title=f"Weather in {city_name}",color=0x9b59b6)            
    
    myEmbed6.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
    myEmbed6.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
    myEmbed6.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
    myEmbed6.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
    myEmbed6.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
    myEmbed6.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    
    await ctx.send(embed=myEmbed6)


#client function(on disconnect)
@client.event
async def on_disconnect():
    
    potato=client.get_channel(857989327702327336)
    await potato.send("GG, Bye!")


#client function(on any message)
@client.event
async def on_message(message):
    
    if message.content=="Hey" or message.content=="Hello" or message.content=="hey" or message.content=="hello":
        potato=client.get_channel(857989327702327336)
        await potato.send(f"Hope you had a nice day {message.author.name}!\nUse #Help command for more information")
    await client.process_commands(message)    


#to run the bot
client.run('ODU3OTgwNDg0NzM5MDA2NDY0.YNXemA.hDTkJ1-0exhgLquDO_jTHkMFXpQ')
