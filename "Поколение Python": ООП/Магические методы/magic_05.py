from functools import singledispatchmethod


class IPAddress:

    @singledispatchmethod
    def __init__(self, ipaddress: str) -> None:
        self.ipaddress = ipaddress

    @__init__.register(list)
    @__init__.register(tuple)
    def _from_list_tuple(self, ipaddress):
        self.ipaddress = '.'.join(map(str, ipaddress))

    def __str__(self) -> str:
        return f"{self.ipaddress}"
    
    def __repr__(self) -> str:
        return f"IPAddress('{self.ipaddress}')"


