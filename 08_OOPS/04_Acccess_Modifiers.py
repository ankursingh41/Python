# Public modifier: Accessible from anywhere
class ABC:
    def __init__(self):
        self.public_var = "I am public" # this is a public attribute

    def public_function(): # this is a public function
        print("This is a public function")


# Private modifier: Accessible only within the class
class XYZ:
    def __init__(self):
        self.__private_var = "I am private" # this is a private attribute   

    def __private_function(): # this is a private function
        print("This is a private function")


# Protected modifier: Accessible within the class and its subclasses
class PQR:
    def __init__(self):
        self._protected_var = "I am protected" # this is a protected attribute

    def _protected_function(): # this is a protected function
        print("This is a protected function")


