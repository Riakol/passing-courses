from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version) -> None:
        self.version = self.parse(version)
        self.edited_ver = list(map(int, self.version.split('.')))

    def __repr__(self) -> str:
        return f"Version('{self.version}')"
    
    def __str__(self) -> str:
        return self.version
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Version):
            return self.version == __value.version
        return NotImplemented
    
    def __gt__(self, __value: object) -> bool:
        if isinstance(__value, Version):
            return self.edited_ver[0] > __value.edited_ver[0] or (self.edited_ver[0] == __value.edited_ver[0] and self.edited_ver[1] > __value.edited_ver[1])
        return NotImplemented


    @staticmethod
    def parse(version):
        if version.count('.') == 0:
            return f"{version}.0.0"
        elif version.count('.') == 1:
            return f"{version}.0"
        else:
            return version
        
        