import connexion
import six
import openai
import uuid
from openai_client.gptclient import GptClient
from swagger_server.models.gpt_message import GptMessage  # noqa: E501
from swagger_server.models.gpt_message_res import GptMessageRes
from swagger_server import util

# SAFE TO EDIT FILE
def gpt_chat(body):  # noqa: E501
    """Get answer from gpt

    Get a message from gpt # noqa: E501

    :param body: message to gpt
    :type body: dict | bytes

    :rtype: GptMessage
    """
    if connexion.request.is_json:
        gpt_client = GptClient()
        body = GptMessage.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            if not body.conversation_id:
                cid = uuid.uuid4()
            else:
                cid = body.conversation_id
            return GptMessageRes.from_dict(
                {"message":gpt_client.send_message(body.message, tailoring=body.tailoring , conversation_id=cid), "status_code":200, "conversation_id":cid}
            )
            #return GptMessageRes.from_dict(
            #    {"message":"Nothing new yet", "status_code":200}
            #)
        except openai.error.RateLimitError:
            return GptMessageRes.from_dict(
                {"message":"Rate Limit Error from OpenAI", "status_code":429}
            )
