class Award(object):
    Awards = {}
    def __init__(self, id: str, description: int, emoji: str) -> None:
        if id in Award.Awards:
            raise Exception("Duplicate award id: " + id)
        self.id = id
        self.description = description
        self.emoji = emoji
        Award.Awards[id] = self

    def getById(id: str):
        return Award.Awards[id]

class Awards:
    NONE = Award('0', '', ':thumbsup:') 
    HELPS_ME = Award('1', 'Helped Me', ':tada:')
    OUR_TEAM = Award('2', 'Our Team', ':sparkles:')
    OUR_USERS = Award('3', 'Our Users', ':medal:')
    ABOVE_BEYOND = Award('4', 'Above & Beyond', ':gift:')
    




