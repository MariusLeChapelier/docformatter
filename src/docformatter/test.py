import re

from docformatter.syntax import reindent, strip_leading_blank_lines


GOOGLE_REGEX = r"^ *[a-zA-Z0-9_\- ]*:$"
chatgpt_regex = r"^\s*Args:\s*$"
SPHINX_REGEX = r":(param|raises|return|rtype|type|yield)[a-zA-Z0-9_\-.() ]*:"

t = """GOOGLE Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Args:
        param1 (int): The first parameter. `PEP 484`_ type annotations are supported. If attribute, parameter, and return types are annotated according to `PEP 484`_, they do not need to be
        param2 (str): The second parameter. `PEP 484`_ type annotations are supported. If attribute, parameter, and return types are annotated according to `PEP 484`_, they do not need to be

    Returns:
        bool: The return value. True for success, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """

t = """GOOGLE Example function with types documented in the docstring.

        `PEP 484`_ type annotations are supported. If attribute, parameter,
        and return types are annotated according to `PEP 484`_, they do not
        need to be included in the docstring:

        Args:
            param1 (int): The first parameter. `PEP 484`_ type annotations
                are supported. If attribute, parameter, and return types are
                annotated according to `PEP 484`_, they do not need to be
            param2 (str): The second parameter. `PEP 484`_ type annotations
                are supported. If attribute, parameter, and return
                types are annotated according to `PEP 484`_, they do not
                    need to be

        Returns:
            bool: The return value. True for success, False otherwise.
        """


st = """SPHINX Example function with types documented in the docstring. Example function
    with types documented in the docstring. Example function with types documented in
    the docstring. Example function with types documented in the docstring.

    Type annotations are supported. If attribute, parameter, and return
    types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    :param param1: The first parameter. Type annotations are supported. If attribute, parameter, and return types are annotated according to `PEP 484`_.
    :type param1: int, optional
    :param param2: The second parameter. Type annotations are supported.     If attribute, parameter, and return types are annotated     according to `PEP 484`_. 
    :type param2: int, optional
    ... 
    :return: The return value. True for success, False otherwise. The     return value. True for success, False otherwise. 
    :rtype: bool 
    .. 
    _PEP 484:
    https://www.python.org/dev/peps/pep-0484/
    """

text = """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
# line = text.splitlines()[0]
# indentation = " " * (len(line) - len(line.lstrip()))
# text2 = strip_leading_blank_lines(text)
# print(text2)
# text2 = reindent(text, indentation).rstrip()
# print(text2)

text = """lalal:

fqefbqiefbiqeubfiqbef

lfqel:
    fefwefw
    
feibwfei: 
fewf
"""

text = " args:"

_field_idx = [
    (_field.start(0), _field.end(0)) for _field in re.finditer(GOOGLE_REGEX, text)
]
print(_field_idx)

_field_idx = [
    (_field.start(0), _field.end(0)) for _field in re.finditer(SPHINX_REGEX, st)
]
print(_field_idx)
# split_lines = text.rstrip().splitlines()
# # print(split_lines)
# # print([re.match(GOOGLE_REGEX, line) for line in split_lines])
# # print(re.match(GOOGLE_REGEX, text))
# # print([re.finditer(GOOGLE_REGEX, line) for line in split_lines])

# for line in split_lines:
#     _field_idx = [
#         (_field.start(0), _field.end(0)) for _field in re.finditer(GOOGLE_REGEX, line)
#     ]
#     print(_field_idx)
