# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount

class EchoBot(ActivityHandler):
    def __init__(self, oaibot):
        # handing over the openai bot to the echo bot
        self.OAICHAT = oaibot

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

    async def on_message_activity(self, turn_context: TurnContext):
        
        # get response from the Azure OpenAI service 
        chatbot_response = self.OAICHAT.get_response(turn_context.activity.text)
        # print(f"Chatbot: {chatbot_response}")
        
        # chatbot_response = turn_context.activity.text
        return await turn_context.send_activity(
            MessageFactory.text(f"AOAI: {chatbot_response}")
        )
