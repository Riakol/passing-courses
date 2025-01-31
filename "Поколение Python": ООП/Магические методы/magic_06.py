class PhoneNumber:
    def __init__(self, phone_number) -> None:
        self.phone_number = ''.join(phone_number.split())

    def __str__(self) -> str:
        return "({}) {}-{}".format(self.phone_number[:3], self.phone_number[3:6], self.phone_number[6:])
    
    def __repr__(self) -> str:
        return f"PhoneNumber('{self.phone_number}')"
    
    