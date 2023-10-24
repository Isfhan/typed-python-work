from typing import Union, TypedDict, Tuple, Set, List
import pprint

cdeDataType = TypedDict(
    'cdeDataType',
    {
        "a": int,
        "b": int
    }
)

myDataType = TypedDict(
    'myDataType', {
        "fname": str,
        "name": str,
        "education": str,
        "abc": List[int],
        'xyz': Set[int],
        'efg': Tuple,
        'cde': cdeDataType
    }
)


# Key = Union[int, str]  # create custom type
# Value = Union[int, str, list, tuple, set]


data: myDataType = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
    "abc": [1, 2, 3],
    'xyz': {1, 2, 3},
    'efg': (1, 2, 3),
    'cde': {"a": 1, "b": 2}
}

print(data['cde']['b'])
