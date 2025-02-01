class AnyClass:

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
        self.formatted = ', '.join([f"{k}={repr(v)}" for k, v in self.__dict__.items()])

    def __str__(self) -> str:
        return f"AnyClass: {self.formatted}"
    
    def __repr__(self) -> str:
        return f"AnyClass({self.formatted})"


