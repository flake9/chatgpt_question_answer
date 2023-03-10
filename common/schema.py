from marshmallow import Schema, fields, validate


class ChatGPTRequestSchema(Schema):
    conversation_key = fields.String(required=True, allow_none=False)
    question = fields.String(required=True, allow_none=True)


class ChatGPTResponseSchema(Schema):
    ok = fields.Boolean(default=True)
    question = fields.String(required=True, allow_none=True)
    result = fields.String(required=True, default='')
