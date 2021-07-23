
from __future__ import annotations 
import discord 

from .button import Button 

class Bot:
    
    """ Represent A Discord Bot object """ 
    
    def __init__(self, bot: discord.ext.commands.Bot):
        
        self.bot = bot
        
    def new_button(self):
        
        self.new_inter = Button(self.bot)
        
        return self.new_inter 