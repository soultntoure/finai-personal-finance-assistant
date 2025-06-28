from fastapi import HTTPException, status

class FinAIException(HTTPException):
    def __init__(self, detail: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        super().__init__(status_code=status_code, detail=detail)

class UserNotFoundException(FinAIException):
    def __init__(self):
        super().__init__("User not found", status_code=status.HTTP_404_NOT_FOUND)

class UnauthorizedException(FinAIException):
    def __init__(self):
        super().__init__("Not authorized", status_code=status.HTTP_401_UNAUTHORIZED)

class PlaidAPIException(FinAIException):
    def __init__(self, detail: str):
        super().__init__(f"Plaid API Error: {detail}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
