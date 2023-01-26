import os
import openai


class OpenAIBot:
    def __init__(self, cfg):
        self.conversation_history = ""
        openai.api_type = "azure"
        openai.api_base = "https://mma-openai.openai.azure.com/"
        openai.api_version = "2022-12-01"
        openai.api_key = cfg.OAI_KEY

        self.model_engine = "text-davinci-003"
        self.chatbot_prompt = """
        As an advanced chatbot, your primary goal is to assist users to the best of your ability. This may involve answering questions, providing helpful information, or completing tasks based on user input. In order to effectively assist users, it is important to be detailed and thorough in your responses. Use examples and evidence to support your points and justify your recommendations or solutions.

        <conversation history>

        User: <user input>
        Chatbot:"""

    def get_response(self,user_input):

        prompt = self.chatbot_prompt.replace(
            "<conversation_history>", self.conversation_history).replace("<user input>", user_input)

        # Get the response from GPT-3
        response = openai.Completion.create(
            engine=self.model_engine, prompt=prompt, max_tokens=2048, n=1, stop=None, temperature=0.5)

        # Extract the response from the response object
        response_text = response["choices"][0]["text"]

        chatbot_response = response_text.strip()
        self.conversation_history += f"User: {user_input}\nChatbot: {chatbot_response}\n"

        return chatbot_response


    def main(self):
        # conversation_history = ""

        while True:
            user_input = input("> ")
            if user_input == "exit":
                break
            chatbot_response = self.get_response(user_input)
            print(f"Chatbot: {chatbot_response}")



# OAICHAT = OpenAIBot()
# OAICHAT.main()