# Biscord 
> Simple button extension for discord.py 

# Example usage 
```py 
import discord 
from discord.ext import commands 

import biscord # You should able to locate the module file in your repository.

bot = commands.Bot(command_prefix = "!", case_insensitive = True) 
inter = biscord.Bot(bot) 
    
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

bot.run(TOKEN)  
``` 
