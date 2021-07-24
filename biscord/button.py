
""" TODO 
inter = biscord.add_action_row(
            biscord.add_button(label = '', style = 1, custom_id = 'gottem')
        )
""" 

from __future__ import annotations 
from . import abc
from discord.http import Route
import typing 

class ButtonStyle: 
    
    """ Represent a button style """ 
    
    @classmethod 
    def blurple(cls):
        
        return 1 
        
    @classmethod 
    def grey(cls):
        
        return 2 
        
    @classmethod 
    def green(cls):
        
        return 3 
        
    @classmethod 
    def red(cls):
        
        return 4 
        
class ButtonInteraction(abc.MessageAble):
    
    """ 
    Represent a clicked button that has been made with interaction. 
        Returned by :: interaction.wait_for_button_click :: 
    """ 
    
    def __init__(self, **kwargs):
        
        self.bot = kwargs.get("bot")
        self._clicked_button = kwargs.get("clicked_button") 
        self._token = kwargs.get("token")
        self._inter_id = kwargs.get("inter_id")
        
    @property 
    def clicked_button(self):
        return self._clicked_button
        
    @property 
    def token(self):
        return self._token 
        
    @property 
    def inter_id(self):
        return self._inter_id 

class Button(abc.MessageAble):
    
    """ Represent a button Object 
    Returned by :: interaction.new_button :: 
    """
    
    def __init__(self, bot):
        
        self.bot = bot 
        self.component = []
        self.http = None 
    
    def add_action_row(self, *func) -> Button:
        
        action_row = {
            "type": 1, 
            "components": list(func) 
        }
        
        self.component.append(action_row)
        
        return self  
        
    def add_button(self, **kwargs) -> Button:
        
        expected = ["label", "style", "custom_id"]
        
        btn = {"type": 2}  
        
        for k, v in kwargs.items():
            if k in expected: btn[k] = v 
        
        return btn 
        
    async def wait_for_button_click(self, timeout: typing.Union[int, float] = 90) -> biscord.ButtonInteraction:
        
        _clicked_button: biscord.ButtonInteraction = None 
        
        while True:
            
            message = await self.bot.wait_for("socket_response", timeout = timeout) 
            
            t, d = message.get("t"), message.get("d")
            
            if t == "INTERACTION_CREATE":
                
                _clicked_button = ButtonInteraction(
                    bot = self.bot, 
                    token = d["token"], 
                    inter_id = d["id"], 
                    clicked_button = d["data"]["custom_id"]
                    )
                    
                break     
        
        return _clicked_button