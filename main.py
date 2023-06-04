from utils import JSONSerializerAbstractmethods


class JSONSerializer(JSONSerializerAbstractmethods):
    @staticmethod
    def serialize(obj):
        if isinstance(obj, (str, int, float, bool, type(None))):
            return JSONSerializer._serialize_primitive(obj)
        elif isinstance(obj, list):
            return JSONSerializer._serialize_list(obj)
        elif isinstance(obj, dict):
            return JSONSerializer._serialize_dict(obj)
        else:
            raise ValueError("Object type not supported for serialization")

    @staticmethod
    def deserialize(json_data):
        return JSONSerializer._deserialize(json_data)

    @staticmethod
    def _serialize_primitive(obj):
        if isinstance(obj, str):
            return '"' + obj + '"'
        elif isinstance(obj, bool):
            return 'true' if obj else 'false'
        else:
            return str(obj)

    @staticmethod
    def _serialize_list(obj):
        items = [JSONSerializer.serialize(item) for item in obj]
        return '[' + ', '.join(items) + ']'

    @staticmethod
    def _serialize_dict(obj):
        items = [f'"{key}": {JSONSerializer.serialize(value)}' for key, value in obj.items()]
        return '{' + ', '.join(items) + '}'

    @staticmethod
    def _deserialize(json_data):
        if isinstance(json_data, str):
            if json_data.startswith('{') and json_data.endswith('}'):
                return JSONSerializer._deserialize_dict(json_data[1:-1])
            elif json_data.startswith('[') and json_data.endswith(']'):
                return JSONSerializer._deserialize_list(json_data[1:-1])
            elif json_data.startswith('"') and json_data.endswith('"'):
                return json_data[1:-1]
            elif json_data == 'true':
                return True
            elif json_data == 'false':
                return False
            elif json_data == 'null':
                return None
            elif '.' in json_data:
                return float(json_data)
            else:
                return int(json_data)
        else:
            return json_data

    @staticmethod
    def _deserialize_dict(json_data):
        if not json_data:
            return {}
        items = json_data.split(',')
        result = {}
        for item in items:
            key, value = item.split(':')
            result[key.strip()[1:-1]] = JSONSerializer._deserialize(value.strip())
        return result

    @staticmethod
    def _deserialize_list(json_data):
        if not json_data:
            return []
        items = json_data.split(',')
        return [JSONSerializer._deserialize(item.strip()) for item in items]


data = {
    'name': 'John',
    'age': 30,
    'is_student': True,
    'grades': [85, 92, 78]
}

json_data = JSONSerializer.serialize(data)
print(json_data)

deserialized_data = JSONSerializer.deserialize(json_data)
print(deserialized_data)