import discord 
from discord.ext import commands 

import biscord 
import json # For debug purposes 
import zlib 

bot = commands.Bot(command_prefix = "!", case_insensitive = True) 
inter = biscord.Bot(bot) 

@bot.event 
async def on_ready():
    
    print("Logging in as %s" % bot.user)
    
@bot.command() 
async def button(ctx): 
    
    interaction = inter.new_button() 
    interaction.add_action_row(
            interaction.add_button(label = "DANGER!", style = biscord.ButtonStyle.red(), custom_id = "danger"),
            interaction.add_button(label = "click this", style = biscord.ButtonStyle.green(), custom_id = "plot")
        )
    
    await interaction.send(
        ctx, 
        content = "Button Interaction", 
        components = interaction.component 
    )    
    
    await interaction.wait_for_button_click() 

bot.run("ODQ5MTIxNDEyNjE4MjU2NDE3.YLWj8A.D6xmmHk3s1g9OKCrR87Fm7y8IbA")  