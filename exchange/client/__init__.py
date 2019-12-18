class BaseClient(object):

    async def ticks(self, *args, **kwargs):
        raise NotImplementedError
