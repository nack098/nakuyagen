from typing import Generic, TypeVar

T = TypeVar("T")


class Result(Generic[T]):
    def __init__(self, value):
        self._value = value

    def bind(self, func):
        if self.is_error():
            return self
        return Result(func(self._value))

    def is_error(self) -> bool:
        if isinstance(self._value, BaseException):
            return True
        return False

    def error(self) -> BaseException | None:
        if isinstance(self._value, BaseException):
            return self._value
        return None

    def unwrap(self) -> T:
        if self.is_error():
            raise self._value
        return self._value
