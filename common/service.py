from .models import Chatbot
from .utils import get_configuration


class ChatGPTService:
    def __init__(self, **kwargs):
        self.question: str = kwargs['question']
        self.conversation_key: str = kwargs['conversation_key']

    def response(self):
        chatbot = Chatbot(
            config=get_configuration(),
            conversation_id=self.conversation_key,
        )

        response, prev_text = "", ""

        for data in chatbot.ask(self.question):
            response += data["message"][len(prev_text) :]
            prev_text = data["message"]

        return {"result": response, "question": self.question}
