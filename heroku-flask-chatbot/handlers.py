import agents

DEFAULT_GREEDING = "Привет!"
DEFAULT_BYE = "Пока!"


class BaseHandler:
    def __init__(self):
        pass

    def get_response(self):
        raise NotImplementedError


class MarusiaSimpleHandler(BaseHandler):
    def __init__(self, request, agent_type, greeding=DEFAULT_GREEDING, bye=DEFAULT_BYE):
        super(MarusiaSimpleHandler, self).__init__()
        self.version = request.json["version"]
        self.session = request.json["session"]
        self.command = request.json["request"]["command"]
        self.end_session = False
        self.greeding = greeding
        self.bye = bye
        if agent_type == "dialogflow2":
            self.agent = agents.DialogFlowAgent(self.command)
        else:
            raise ValueError("agent_type must be only 'dialogflow2' yet")

    def get_response(self):
        if self.session["new"]:
            text = self.greeding
        elif self.command == "on_interrupt":
            text = self.bye
        else:
            text = self.agent.get_agent_response()
        response = {
            "version": self.version,
            "session": self.session,
            "response": {"end_session": self.end_session, "text": text},
        }
        return response
