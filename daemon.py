#!/usr/bin/env python

from slack import RTMClient
import config as c
from message import Message
from actions import run_action


@RTMClient.run_on(event="message")
async def get_message(**payload):

    _data = payload["data"]

    message = Message(
        client=payload["web_client"],
        channel_id=_data["channel"],
        ts=_data["ts"],
        user=_data["user"],
        team=_data["team"],
        text=_data['text']
    )

    if not message.is_valid_user:
        message.respond('User is not allowed to communicate with bot')
        return None

    if not message.is_valid_team:
        message.respond('Bad team name')
        return None

    response_text = run_action(message)
    await message.respond(response_text)


if __name__ == "__main__":
    import asyncio

    async def run():
        loop = asyncio.get_event_loop()
        rtm_client = RTMClient(
            token=c.AUTHKEY, loop=loop, run_async=True, connect_method='rtm.connect'
        )
        await rtm_client.start()

    asyncio.run(run(), debug=True)
