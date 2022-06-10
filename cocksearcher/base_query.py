import abc
import dataclasses
from typing import Type


class BaseQuery:

    @staticmethod
    @abc.abstractmethod
    def from_query_string(self):
        pass

    @classmethod
    def get_keys_info(cls) -> list[tuple[str, Type]]:
        return [(field.name, field.type) for field in dataclasses.fields(cls)]
