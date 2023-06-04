from abc import ABC, abstractstaticmethod


class JSONSerializerAbstractmethods(ABC):
    @abstractstaticmethod
    def serialize(self, obj):
        pass

    @abstractstaticmethod
    def deserialize(self, obj):
        pass
