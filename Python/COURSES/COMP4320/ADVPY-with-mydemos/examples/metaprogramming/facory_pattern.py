
from abc import ABC, abstractmethod

class Localizer(ABC):
    @abstractmethod
    def localize(self, msg):
        """ Translate message """
        pass

class GermanLocalizer(Localizer):
    "German version"

    def __init__(self):
        """ Setup translations """
        self.translations = {"main.header": "Ich spreache deutsch"}

    def localize(self, msg):
        """Returns msg in German"""
        return self.translations.get(msg, msg)


class French(Localizer):
    """French version"""

    def __init__(self):
        """ Setup translations """
        self.translations = {"main.header": "Je parle français"}

    def localize(self, msg):
        """Returns msg in French"""
        return self.translations.get(msg, msg)


class EnglishLocalizer(Localizer):
    """English version"""

    def __init__(self):
        """ Setup translations """
        self.translations = {"main.header": "I speak English"}

    def localize(self, msg):
        """Returns msg in English"""
        return self.translations.get(msg, msg)


class Translate:

    @staticmethod
    def get_localizer(option="1") -> Localizer:
        """Factory Method"""
        localizers = {
            "1": EnglishLocalizer,
            "2": GermanLocalizer,
            "3": French,
        }

        return localizers[option]()


def main():

    while True:
        print("Please select your language:")
        print("1. English")
        print("2. German")
        print("3. French")
        print("4. Exit")

        option = input("Please select an option then hit enter:")
        if option == '4': break
        local = Translate.get_localizer(option)

        msg = "main.header"
        print(local.localize(msg))


if __name__ == "__main__":
    main()