import re
import json
import logging

import dialogflow_v2
from flask import Flask
from flask import request


from config import keys
from handlers import MarusiaSimpleHandler

app = Flask(__name__)


@app.route("/", methods=["POST"])
def main():
    logging.info("Request: %r", request.json)
    handler = MarusiaSimpleHandler(request, agent_type="dialogflow2")
    response = handler.get_response()
    logging.info("Response: %r", response)

    return json.dumps(response, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    app.run()
