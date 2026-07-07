from dataclasses import dataclass
from datetime import datetime


@dataclass
class Application:
    name: str
    description: str
    price: float
    begin: str
    end: str
    contact: str

    def __post_init__(self):
        if not self.name or len(self.name.strip()) == 0:
            raise ValueError("Название не может быть пустым")

        if not self.description or len(self.description.strip()) == 0:
            raise ValueError("Описание не может быть пустым")

        if self.price <= 0:
            raise ValueError("Цена должна быть больше 0")

        try:
            begin_date = datetime.strptime(self.begin, "%Y-%m-%d")
            end_date = datetime.strptime(self.end, "%Y-%m-%d")
            if end_date < begin_date:
                raise ValueError("Дата окончания не может быть раньше даты начала")
        except ValueError as e:
            if "does not match format" in str(e):
                raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД")
            raise e

        if not self.contact or len(self.contact.strip()) == 0:
            raise ValueError("Контакт не может быть пустым")