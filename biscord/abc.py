
from discord.http import Route 

class MessageAble: 
    
    async def __maybe_inter(self, **kwargs):
        
        msg = {"type": 4} 
        msg["data"] = {k: v for k, v in kwargs.items() if k in ["content", "embed"]}
        
        await self.bot.http.request(
            Route("POST", f"/interactions/{self.inter_id}/{self.token}/callback"), 
            json = msg 
            )
    
    async def __common_send(self, ctx = None, **kwargs):
        
        if ctx is None: raise TypeError("Unknown destination.") 
        
        msg = {k: v for k, v in kwargs.items() if k in ["content", "embed", "components"]}
        
        await self.bot.http.request(
            Route("POST", f"/channels/{ctx.channel.id}/messages"), 
            json = msg 
            )
    
    async def send(self, ctx = None, **kwargs):
        
        """ 
        :param ctx: The context of current invoked command (Optional. depends on button instance)
        """
        
        if kwargs.get("content") == None and kwargs.get("embed") == None:
            raise TypeError("Invalid form body.") 
            
        class_name = self.__class__.__name__     
        
        await self.__maybe_inter(**kwargs) if class_name == "ButtonInteraction" else await self.__common_send(ctx, **kwargs)