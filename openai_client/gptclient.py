import openai
import os
import logging 

logger = logging.getLogger(__name__)

# make a map conversationid -> conversation so we can keep track of the conversation
convmap = {}

class GptClient:
    def __init__(self):
        openai.api_key = os.environ["OPENAI_API_KEY"]
    def send_message(self, message, tailoring="please tailor the response for a person which doesn't know much about science", conversation_id=None):
        conversation_history = ""
        if conversation_id and conversation_id in convmap:
            conversation_history = convmap[conversation_id]
            conversation_history+=f"User:{message}\nAI:"
        else:
            conversation_history = f"User:{message}\nAI:"  
        logger.info(conversation_history)
        response = openai.Completion.create(
        engine="curie:ft-personal-2023-03-30-12-25-45",
        prompt=conversation_history,
        temperature=0.01,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0,
        stop=["\nQ", "\n"]
        )
        logger.info(f"Message to openai: {message}, response: {response.choices[0].text.strip().replace('AI:', '')}")
        # also append this log line to a file
        try:
            with open("openai.log", "a") as f:
                f.write("{"+ f"\"Message to openai\": \"{message}\", \"response\": \"{response.choices[0].text.strip()}\"" + "}")
        except Exception as e:
            logger.error(f"Could not write to openai.log, {str(e)}")
        conversation_history+=f"AI:{response.choices[0].text.strip().replace('AI:', '')}\n"

        convmap[conversation_id] = conversation_history
        return response.choices[0].text.strip()
