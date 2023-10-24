from typing import TypedDict

course = TypedDict(
    'course',
    {
        'name': str,
        'fess': int
    }
)

myData = TypedDict(
    'myData',
    {
        'name': str,
        'age': int,
        'course': course
    }
)

data: myData = {
    "name": "isfhan",
    "age": 26,
    "course": {
        'name': 'AI',
        'fess': 4500
    }
}

print(data['course']['name'])
