import random
from datetime import date, timedelta
import string


class Person:
    def __init__(self, first_name: list[str], second_name: list[str], street: list[str], municipality: list[str], email: list[str], password: list[str], user_agents: list[str]):
        # Details about person
        self.first_name = random.choice(first_name)
        self.second_name = random.choice(second_name)
        self.date_of_birth = self.generate_birth()
        self.street = random.choice(street)
        self.house_numer = random.choices(range(1, 201), weights=range(200, 0, -1))[0]
        self.zipcode = random.randint(10000, 999999)
        self.municipality = random.choice(municipality)

        # Online Identity
        self.email = self.generate_email(email)
        self.password = self.generate_password(password)
        self.ip = self.generate_ip()
        self.user_agents = random.choice(user_agents)

        # Card Details
        self.card_number = self.credit_card_generator()
        self.cvv = "".join(random.choices("0123456789", k=3))
        self.card_expire = f"{random.randint(1,12):02d}/{random.randint(26,30)}"

    def generate_ip(self) -> str:
        while True:
            octets = [random.randint(1, 255) for _ in range(4)]
            if (
                    octets[0] == 10 or
                    (octets[0] == 172 and 16 <= octets[1] <= 31) or
                    (octets[0] == 192 and octets[1] == 168) or
                    octets[0] == 127 or
                    octets[0] >= 224
            ):
                continue
            return ".".join(map(str, octets))

    def credit_card_generator(self):
        iins = ["4", "4", "4", "4", "4", "51", "52", "53", "54", "55", "56", "57", "58", "35"]
        iin = random.choice(iins)
        body_length = 16 - len(iin) -1
        body = "".join(random.choices("0123456789", k=body_length))
        partial_number = iin + body
        def luhn_checksum_digit(number: str) -> str:
            digits = [int(d) for d in number[::-1]]
            for i in range(1, len(digits), 2):
                digits[i] *= 2
                if digits[i] > 9:
                    digits[i] -= 9
            checksum = (10 - sum(digits) % 10) % 10
            return str(checksum)
        check_digit = luhn_checksum_digit(partial_number)
        return partial_number + check_digit

    def generate_password(self, passwords) -> str:
        password = random.choice(passwords)
        # Add Number
        if random.choices([True, False], weights=[3, 7])[0]:
            pos = random.randint(0, len(password))
            password = password[:pos] + str(random.randint(0, 999)) + password[pos:]
        # Add letter
        if random.choices([True, False], weights=[3, 7])[0]:
            zufallschar = random.choice(string.ascii_letters)  # a-z + A-Z
            pos = random.randint(0, len(password))
            password = password[:pos] + zufallschar + password[pos:]
        # Change capital/small letters
        if random.choices([True, False], weights=[3, 7])[0]:
            positions = random.sample(range(len(password)), k=min(random.randint(1, 3), len(password)))
            password = ''.join(
                c.upper() if i in positions and c.islower()
                else c.lower() if i in positions and c.isupper()
                else c
                for i, c in enumerate(password)
            )


        return password

    def generate_email(self, emails) -> str:
        ending = "@" + random.choice(emails)
        combiner = random.choice([".", "+", "-", "", "_", "."])
        first_name = self.first_name[:random.randint(2, len(self.first_name))]
        second_name = self.second_name[:random.randint(2, len(self.second_name))]

        if random.choices([True, False], weights=[3, 7])[0]:
            number = str(random.randint(0, 999))
        else:
            number = ""

        email = first_name + combiner + second_name + number + ending
        return email.lower()

    # Generate a random date of birth
    def generate_birth(self) -> date:
        today = date.today()
        oldest = today.replace(year=today.year - 60)
        youngest = today.replace(year=today.year - 18)

        delta_days = (youngest - oldest).days
        return oldest + timedelta(days=random.randint(0, delta_days))

