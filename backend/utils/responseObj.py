from typing import Dict, Tuple


class ResponseObj:
    msg: str
    data: Dict | None

    def __init__(self, *args: Tuple | None, msg: str) -> None:
        self.msg = msg
        print(len(args))
        if len(args) > 0:
            self.data = args[0]
        else:
            self.data = None

    def get(self) -> Dict[str, str]:
        if self.data:
            return {"msg": self.msg, "data": self.data}
        return {"msg": self.msg}
