import config as c


class Message:

    def __init__(self, **parameters) -> None:
        self.client = parameters["client"]
        self.channel_id = parameters["channel_id"]
        self.thread_ts = parameters["ts"]
        self.user = parameters["user"]
        self.team = parameters["team"]
        self.text = parameters['text']

    @property
    def is_valid_user(self):
        if len(c.ALLOWED_USER_IDS) == 0:
            return True
        elif self.user in c.ALLOWED_USER_IDS:
            return True
        return False

    @property
    def is_valid_team(self):
        if c.TEAM is None or self.team == c.TEAM:
            return True
        return False

    async def respond(self, text):
        await self.client.chat_postMessage(
            channel=self.channel_id,
            text=text,
            thread_ts=self.thread_ts
        )
