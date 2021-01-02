import dialogflow_v2
from config import keys


class BaseAgent(BaseAgent):
    def __init__(self, command):
        self.command = command

    def get_agent_response(self):
        raise NotImplementedError


class DialogFlowAgent(BaseAgent):
    def __init__(self, command):
        super(DialogFlowAgent, self).__init__(command)
        self.language_code = keys.values["dialogFlowSessionLanguageCode"]
        self.google_project_id = keys.values["googleProjectID"]
        self.dialogflow_session_id = keys.values["dialogFlowSessionID"]
        self.session_client = dialogflow_v2.SessionsClient()
        self.session_path = self.session_client.session_path(
            self.google_project_id, self.dialogflow_session_id
        )

    def get_agent_response(self):
        text_input = dialogflow_v2.types.TextInput(
            self.command, language_code=self.language_code
        )
        query_input = dialogflow_v2.types.QueryInput(text=text_input)
        response = self.session_client.detect_intent(self.session_path, query_input)
        text_output = response.query_result.fulfillment_text
        return text_output
