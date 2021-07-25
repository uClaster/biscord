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
        components = interaction.component 
    )    
    
    cbutton = await interaction.wait_for_button_click() 
    
    if cbutton.clicked_button == "plot":
        
        await cbutton.send(content = "Good.")
        
    elif cbutton.clicked_button == "danger":
        
        await cbutton.send(content = "That's not good.")

bot.run("ODQ5MTIxNDEyNjE4MjU2NDE3.YLWj8A.dx-O_T6gP6Qqxbv8R6Nrjv_9K6Q")  