class Config:
    _singletone = None

    def __new__(cls, *args, **kwargs):
        if Config._singletone is None:
            Config._singletone = super().__new__(cls)
        return Config._singletone
    
    def __init__(self) -> None:
        self.program_name = 'GenerationPy'
        self.environment = 'release'
        self.loglevel = 'verbose'
        self.version = '1.0.0'


