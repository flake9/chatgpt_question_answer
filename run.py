from flask import Flask, abort, Response, request
from flask_restful import Resource, Api
from common import ChatGPTRequestSchema, ChatGPTResponseSchema, ChatGPTService, errors as err


URL = "/api/v1/<conversation_key>"

app = Flask(__name__)
api = Api(app)


class ChatGPTAPI(Resource):
    def post(self, **kwargs):
        kwargs.update(request.get_json())
        errors = ChatGPTRequestSchema().validate(kwargs)
        if errors:
            return abort(400, errors)
        try:
            return Response(
                ChatGPTResponseSchema().dumps(ChatGPTService(**kwargs).response()),
                mimetype='application/json',
                status=200,
            )
        except Exception as e:
            err['CHATGPT_ERROR']['message'] = getattr(e, 'message', str(e))
            return err['CHATGPT_ERROR'], 400


api.add_resource(ChatGPTAPI, URL)


if __name__ == '__main__':
    app.run(debug=True)
