import discord
from discord.ext import commands
import requests
import aiohttp

class User(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(
   name="user",
   description="Check a player's stats!",
   aliases=["player", "User", "Player"])
  async def user_(self, ctx, user="Please input a user's name!"):
   async with aiohttp.ClientSession() as cs:
     async with cs.get(f'https://ch.tetr.io/api/users/{user}') as r:
        res = await r.json()
        embed = discord.Embed(
        title=f"Tetr.io ",
        description=f"**Username:** {res['data']['user']['username']}\n**Country:** :flag_{res['data']['user']['country']}:\n**Supporter Tier:** {res['data']['user']['supporter_tier']}\n\n**Verified: **{res['data']['user']['verified']}\n**Games Played:** {res['data']['user']['gamesplayed']}\n**Games Won:** {res['data']['user']['gameswon']}",
        color=0x89d89b
         )
        embed.set_thumbnail(url=f"https://tetr.io/user-content/avatars/{res['data']['user']['_id']}.jpg?rv=AVATAR_REVISION")
        await ctx.reply(embed=embed)



def setup(bot):
  bot.add_cog(User(bot))
