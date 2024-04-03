import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.serializers import CarSerializer
from car.models import Car


def deserialize_car_object(json_bytes: bytes) -> Car:
    stream = io.BytesIO(json_bytes)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    serialized_data = serializer.data
    json_data = JSONRenderer().render(serialized_data)
    return json_data
