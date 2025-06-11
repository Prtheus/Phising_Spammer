import config
from utils.person import Person

class Group:
    def __init__(self,
                 number_of_identities: int,
                 first_names_file: str = config.first_name_file,
                 second_names_file: str = config.last_name_file,
                 streets_file: str = config.street_name_file,
                 municipalities_file: str = config.municipality_file,
                 emails_file: str = config.email_file,
                 passwords_file: str = config.passwd_file,
                 user_agents_file: str = config.user_agents_file):

        self.first_names = self.reader(first_names_file)
        self.second_names = self.reader(second_names_file)
        self.streets = self.reader(streets_file)
        self.municipalities = self.reader(municipalities_file)
        self.emails = self.reader(emails_file)
        self.passwords = self.reader(passwords_file)
        self.user_agents = self.reader(user_agents_file)

        self.identities = self.create_identities(number_of_identities)

    def create_identities(self, number_of_identities: int) -> list[Person]:
        return [
            Person(
                self.first_names,
                self.second_names,
                self.streets,
                self.municipalities,
                self.emails,
                self.passwords,
                self.user_agents
            )
            for _ in range(number_of_identities)
        ]

    def reader(self, file_name: str) -> list[str]:
        with open(file_name, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
