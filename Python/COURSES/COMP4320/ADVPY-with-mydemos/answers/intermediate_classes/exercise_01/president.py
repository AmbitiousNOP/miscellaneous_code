from datetime import datetime


class President:
    def __init__(self, index):
        with open("../../data/presidents.txt") as pres_in:
            for idx, line in enumerate(pres_in, start=1):
                if index != idx:
                    continue
                data = line.rstrip().split(":")
                self._term_number = int(data[0])
                self._last_name = data[1]
                self._first_name = data[2]
                self._birth_date = President.__string_to_date(data[3])
                self._death_date = President.__string_to_date(data[4])
                self._birth_place = data[5]
                self._birth_state = data[6]
                self._term_start_date = President.__string_to_date(data[7])
                self._term_end_date = President.__string_to_date(data[8])
                self._party = data[9]

    @property
    def term_number(self):
        return self._term_number

    @property
    def last_name(self):
        return self._last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def birth_date(self):
        return self._birth_date

    @property
    def death_date(self):
        return self._death_date

    @property
    def birth_place(self):
        return self._birth_place

    @property
    def birth_state(self):
        return self._birth_state

    @property
    def term_start_date(self):
        return self._term_start_date

    @property
    def term_end_date(self):
        return self._term_end_date

    @property
    def party(self):
        return self._party

    def __str__(self):
        fmt = ("#{}\n{} {}\nDateOfBirth: {}\nDateOfDeath: {}\n"
               "Birth Place: {}, {}\nTermStart: {}\nTermEnd: {}\nParty: {}")
        data = (self._term_number, self._first_name, self._last_name,
                self._birth_date, self._death_date, self._birth_place,
                self._birth_state, self._term_start_date,
                self._term_end_date, self._party)

        return fmt.format(*data)

    @staticmethod
    def __string_to_date(a_date):
        result = None
        if a_date != "NONE":
            result = datetime.strptime(a_date, '%Y-%m-%d').date()
        return result
