def f(param1, param2):
    """GOOGLE Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter,
    and return types are annotated according to `PEP 484`_, they do not
    need to be included in the docstring:

    Attributes:
        vad_state (string): dialogue turn information (agent_turn,
            user_turn, silence, interruption, etc) from VADTurnModule.

    Args:
        vad_state (string): dialogue turn information (agent_turn,
            user_turn, silence, interruption, etc) from VADTurnModule.
        param1 (int): The first parameter. `PEP 484`_ type annotations
            are supported. If attribute, parameter, and return types are
            annotated according to `PEP 484`_, they do not need to be
        param2 (str): The second parameter. `PEP 484`_ type annotations
            are supported. If attribute, parameter, and return types are
            annotated according to `PEP 484`_, they do not need to be

    Returns:
        bool: The return value. True for success, False otherwise.
    """
    return True


def f():
    """Wraps a paragraph from a description, following the google docstring style.

    Args:
        paragraphs (list): the list of already wrapped paragraphs from
            docstring
        paragraph (str): the paragraph to wrap
        wrap_length (int, optional): The column to wrap each line at.
            Defaults to 72.
        tab_nb_space (int, optional): Number of spaces in a tabulation.
            Defaults to 4.
        section_line (bool, optional): Boolean describing whether it is
            a special section (Args, Raises, Returns) or not. Defaults
            to False.
        regex (str, optional): The regex used to gather the components
            from the special section. Defaults to None.
    """


class A:
    def f(self, param1, param2):
        """GOOGLE Example function with types documented in the docstring.

        `PEP 484`_ type annotations are supported. If attribute,
        parameter, and return types are annotated according to `PEP
        484`_, they do not need to be included in the docstring:

        Args:
            param1 (int): The first parameter. `PEP 484`_ type
                annotations are supported. If attribute, parameter, and
                return types are annotated according to `PEP 484`_, they
                do not need to be
            param2 (str): The second parameter. `PEP 484`_ type
                annotations are supported. If attribute, parameter, and
                return types are annotated according to `PEP 484`_, they
                do not need to be

        Returns:
            bool: The return value. True for success, False otherwise.
        """
        return True


def f2():
    """SPHINX Example function with types documented in the docstring. Example function
    with types documented in the docstring. Example function with types documented in
    the docstring. Example function with types documented in the docstring.

    Type annotations are supported. If attribute, parameter, and return
    types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:     :param param1: The first parameter.
    Type annotations are supported.     If attribute, parameter, and
    return types are annotated     according to `PEP 484`_.     :type
    param1: int, optional     :param     param2: The second parameter.
    Type annotations are supported.     If attribute, parameter, and
    return types are annotated     according to `PEP 484`_.     :type
    param2: int, optional ...     :return: The return value. True for
    success, False otherwise. The     return value. True for success,
    False otherwise.     :rtype: bool     .. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/
    """


t = """GOOGLE Example function with types documented in the docstring. and return types are annotated according to `PEP 484`_, they do not

        `PEP 484`_ type annotations are supported. If attribute, parameter, and return types are annotated according to `PEP 484`_, they do not
        need to be included in the docstring:

        Args:
            param1 (int): The first parameter. `PEP 484`_ type annotations and return types are annotated according to `PEP 484`_, they do not
                are supported. If attribute, parameter, and return types are
                annotated according to `PEP 484`_, they do not need to be
            param2 (str): The second parameter. `PEP 484`_ type annotations
                are supported. If attribute, parameter, and return
                types are annotated according to `PEP 484`_, they do not
                    need to be

        Returns:
            bool: The return value. True for success, False otherwise. and return types are annotated according to `PEP 484`_, they do not need to be
                and return types are annotated according to `PEP 484`_, they do not need to be

        Raises:
            IndexError: The return value. True for success, False otherwise. and return types are annotated according to `PEP 484`_, they do not need to be
                and return types are annotated according to `PEP 484`_, they do not need to be
        
        """

"""Example function with types documented in the docstring.

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
