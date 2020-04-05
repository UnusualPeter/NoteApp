class Error(Exception):
    # Base class for other exceptions
    pass


class EmptyField(Error):
    # Raised when an input or textarea is empty
    pass


class MaxCharacters(Error):
    # Raised when the input title note has more than 100 characters
    pass
