from src.fields import Name, Phone


class Record:
    """
    Клас для зберігання інформації про контакт.

    Args:
        name (str): Ім'я контакту
    """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """
        Додає номер телефону до списку номерів контакту.

        Args:
            phone (str): Номер телефону

        Returns:
            bool: True якщо номер додано успішно, False якщо такий номер вже існує або невалідний
        """
        if self.find_phone(phone):
            return False

        new_phone = Phone(phone)
        if not new_phone.is_phone_set():
            print("Phone number must contain only 10 digits")
            return False

        self.phones.append(new_phone)
        return True

    def remove_phone(self, phone):
        """
        Видаляє телефон зі списку телефонів.

        Args:
            phone (str): Номер телефону

        Returns:
            bool: True якщо телефон знайдено та видалено, False якщо не знайдено
        """
        found_phone = self.find_phone(phone)
        if found_phone:
            self.phones.remove(found_phone)
            return True
        return False

    def edit_phone(self, old_phone, new_phone):
        """
        Замінює старий номер телефону на новий.

        Args:
            old_phone (str): Старий номер телефону
            new_phone (str): Новий номер телефону

        Returns:
            bool: True якщо номер змінено успішно, в іншому випадку False
        """
        if self.find_phone(new_phone):
            print("The new number is already in the phone book")
            return False

        if self.remove_phone(old_phone):
            return self.add_phone(new_phone)
        return False

    def find_phone(self, phone):
        """
        Шукає телефон у списку телефонів контакту.

        Args:
            phone (str): Номер телефону для пошуку

        Returns:
            Phone or None: Знайдений телефон або None
        """
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        """
        Повертає рядкове представлення контакту.

        Returns:
            str: Рядок з ім'ям та телефонами контакту
        """
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
