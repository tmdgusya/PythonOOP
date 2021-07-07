class BaseError(Exception):

    """예시 코드에서 간단하게 쓰려고 생성하는 커스텀 에러"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message



