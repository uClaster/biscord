
from discord.http import Route 
from discord import Embed 

class MessageAble: 
    
    async def send(self, ctx=None, **kwargs):
        
        """ 
        :param ctx: The context of current invoked command (Optional. depends on button instance)
        """
        
        if kwargs.get("content") == None and kwargs.get("embed") == None:
            raise TypeError("Invalid form body.") 
            
        endpoint: str = "" 
        message_payload: dict = {}
        
        if self.__class__.__name__ == "ButtonInteraction":
            
            message_payload["data"] = {} 
            message_payload["type"] = 4
            
            endpoint = f"/interactions/{self.inter_id}/{self.token}/callback"
            
        else:
            
            if ctx == None:
                raise TypeError("Unknown destination.")
                
            endpoint = f"/channels/{ctx.channel.id}/messages"    
            
        for k, v in kwargs.items():
            
            if isinstance(v, Embed): 
                
                k += "s" # We are using 'embeds' type instead of deprecated 'embed'
                v = [v.to_dict()]
                
            if message_payload.get("data") != None:
                
                message_payload["data"][k] = v
                continue 
            
            message_payload[k] = v 
        
        await self.bot.http.request(
            Route("POST", endpoint), 
            json = message_payload 
            )