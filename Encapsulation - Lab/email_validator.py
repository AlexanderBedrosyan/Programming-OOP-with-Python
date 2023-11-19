class EmailValidator:

    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        username = name.split('@')[0]
        return len(username) >= self.min_length

    def __is_mail_valid(self, mail):
        first_split = mail.split('.')
        current_mail = first_split[0].split('@')[-1]
        return current_mail in self.mails

    def __is_domain_valid(self, domain):
        current_domain = domain.split('.')[-1]
        return current_domain in self.domains

    def validate(self, email):
        return self.__is_domain_valid(email) and self.__is_name_valid(email) and self.__is_mail_valid(email)



mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
