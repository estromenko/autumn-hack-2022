import random
import string


class KeyGeneratorMixin:
    key_length = 10

    def generate_key(self):
        return ''.join(random.choice(string.ascii_letters) for _ in range(self.key_length))
