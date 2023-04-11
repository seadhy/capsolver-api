class CapsolverException(Exception):
    def __init__(self, exception_message):
        super(CapsolverException, self).__init__(exception_message)
        self.exception_message = exception_message

