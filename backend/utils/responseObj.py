from typing import Dict


class ResponseObj:
    msg: str

    def __init__(self, msg: str) -> None:
        self.msg = msg

    def get(self) -> Dict[str, str]:
        return {"msg": self.msg}
