import discord 
from discord.ext import commands 

import biscord 

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
        content = "Button Interaction Test", 
        components = interaction.components 
    )    
    
    cbutton = await interaction.wait_for_button_click() 
    
    if cbutton.clicked_button == "plot":
        
        embed = discord.Embed(title = "good", description = "smart", color = discord.Colour.green())
        
        await cbutton.send(content = "correct.", embed = embed)
        
    elif cbutton.clicked_button == "danger":
        
        embed = discord.Embed(title = "Bruh", description = "Incorrect button.", color = discord.Colour.red())
        
        await cbutton.send(embed = embed)

bot.run(TOKEN)  