
""" TODO 
inter = biscord.add_action_row(
            biscord.add_button(label = '', style = 1, custom_id = 'gottem')
        )
""" 

from discord.http import Route

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

class Button:
    
    """ Represent a button Object 
    Returned by :: interaction.new_button :: 
    """
    
    def __init__(self, bot):
        
        self.bot = bot 
        self.component = []
        self.http = None 
    
    def add_action_row(self, *func):
        
        action_row = {
            "type": 1, 
            "components": [f for f in func] 
        }
        
        self.component.append(action_row)
        
        return self  
        
    def add_button(self, **kwargs):
        
        expected = ["label", "style", "custom_id"]
        
        btn = {"type": 2}  
        
        for k, v in kwargs.items():
            if k in expected: btn[k] = v 
        
        return btn 
        
    async def send(self, ctx, **kwargs):
        
        msg = {}
        
        if kwargs.get("content") == None and kwargs.get("embed") == None:
            
            raise TypeError("Invalid form body.") 
            
        msg = {k: v for k, v in kwargs.items() if k in ["content", "embed", "components"]}    
        
        await self.bot.http.request(
            Route("POST", f"/channels/{ctx.channel.id}/messages"), 
            json = msg 
            )
            
    async def wait_for_button_click(self):
        
        while True:
            
            message = await self.bot.wait_for("socket_response") 
            
            print(message) 
        
        return 