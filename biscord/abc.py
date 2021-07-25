
from discord.http import Route 

class MessageAble: 
    
    async def send(self, ctx = None, **kwargs):
        
        """ 
        :param ctx: The context of current invoked command (Optional. depends on button instance)
        """
        
        if kwargs.get("content") == None and kwargs.get("embed") == None:
            raise TypeError("Invalid form body.") 
            
        endpoint: str = ""     
        message_payload: dict = {} 
            
        if self.__class__.__name__ == "Button": 
            
            if ctx is None: raise TypeError("Unknown destination.") 
            
            endpoint = f"/channels/{ctx.channel.id}/messages"
            
            message_payload = kwargs 
            
        else:
            endpoint = f"/interactions/{self.inter_id}/{self.token}/callback" 
            
            message_payload["type"], message_payload["data"] = 4, kwargs
        
        await self.bot.http.request(
            Route("POST", endpoint), 
            json = message_payload 
            )