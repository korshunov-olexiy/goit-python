from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def create(self):
        pass

    def send_messages(self, value) -> str:
        product = self.create()
        result = product.sending(value)
        return result


class SendingMessages(ABC):
    @abstractmethod
    def sending(self, value) -> str:
        pass


class CreatorPush(Creator):
    def create(self) -> SendingMessages:
        return SendingPushMessages()


class CreatorSMS(Creator):
    def create(self) -> SendingMessages:
        return SendingSMSMessages()


class SendingPushMessages(SendingMessages):
    def sending(self, value) -> str:
        return f"Выполнена Push рассылка сообщения: {value}"


class SendingSMSMessages(SendingMessages):
    def sending(self, value) -> str:
        return f"Выполнена SMS рассылка сообщения: {value}"


def client_code(creator: Creator) -> None:
    print(f"Мы ничего не знаем про код создателя, который работает")
    result = creator.send_messages("my message")
    print(f"Результат: {result}")


if __name__ == "__main__":
    print("Приложение выполняет Push рассылки.")
    client_code(CreatorPush())
    print("\n")

    print("Приложение выполняет SMS рассылки")
    client_code(CreatorSMS())
