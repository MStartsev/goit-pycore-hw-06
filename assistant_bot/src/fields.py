class Field:
    """
    Базовий клас для всіх полів запису.

    Args:
        value: Значення поля
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """
    Клас для зберігання імені контакту. Обов'язкове поле.

    Args:
        value (str): Ім'я контакту
    """

    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    """
    Клас для зберігання номера телефону з валідацією формату.
    """

    def __init__(self, value):
        """
        Ініціалізація номера телефону.

        Args:
            value (str): Номер телефону (10 цифр)
        """
        self.value = None
        if self.validate_phone(value):
            self.value = value

    def is_phone_set(self):
        """
        Перевіряє чи був номер успішно встановлений.

        Returns:
            bool: True якщо номер валідний і встановлений, False якщо ні
        """
        return bool(self.value)

    @staticmethod
    def validate_phone(phone):
        """
        Перевіряє правильність введення номера телефону.

        Args:
            phone (str): Номер телефону для перевірки

        Returns:
            bool: True якщо номер правильний, False якщо ні
        """
        return len(phone) == 10 and phone.isdigit()
