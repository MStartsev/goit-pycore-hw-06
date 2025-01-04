from collections import UserDict


class AddressBook(UserDict):
    """
    Клас для зберігання та управління записами контактів.
    """

    def add_record(self, record):
        """
        Додає новий запис до книги контактів.

        Args:
            record (Record): Об'єкт запису контакту

        Returns:
            bool: True якщо запис додано успішно, False якщо запис з таким ім'ям вже існує
        """
        if record.name.value in self.data:
            return False
        self.data[record.name.value] = record
        return True

    def find(self, name):
        """
        Знаходить запис за ім'ям.

        Args:
            name (str): Ім'я контакту

        Returns:
            Record or None: Знайдений запис або None
        """
        return self.data.get(name)

    def delete(self, name):
        """
        Видаляє запис за ім'ям.

        Args:
            name (str): Ім'я контакту

        Returns:
            bool: True якщо запис знайдено та видалено, False якщо не знайдено
        """
        if name in self.data:
            del self.data[name]
            return True
        return False
