
RESPONSE_CODE_STATUS_OK = 1
RESPONSE_CODE_STATUS_FAIL = 0
RESPONSE_MESSAGE_STATUS_OK = "Ok"
RESPONSE_MESSAGE_STATUS_FAIL = "Fail"

class Response:

	def __init__(self, code = RESPONSE_CODE_STATUS_OK, message = RESPONSE_MESSAGE_STATUS_OK):
		self.code = code
		self.message = message
