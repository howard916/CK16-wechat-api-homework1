from jsonpath import jsonpath
from deepdiff import DeepDiff
from jsonschema import validate, ValidationError


def jp(json_object, expr):
    return jsonpath(json_object, expr)

def diff(d1, d2, ignore_order=False, exclude_paths=None):
    return DeepDiff(d1, d2, ignore_order=ignore_order, exclude_path=exclude_paths)

def jsc(instance, schema):
    try:
        validate(instance=instance, schema=schema)
        return True
    except ValidationError as v:
        raise v

    except Exception as e:
        raise e

