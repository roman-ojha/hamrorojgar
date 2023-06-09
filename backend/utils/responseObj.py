from typing import Dict, Tuple


class ResponseObj:
    msg: str
    data: Dict | None

    def __init__(self, *args: Tuple | None, msg: str) -> None:
        self.msg = msg
        self.data = args[0]

    def get(self) -> Dict[str, str]:
        return {"msg": self.msg, "data": self.data}
