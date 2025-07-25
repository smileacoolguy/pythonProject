#custom_exception
class InvalidInputError(Exception):
    """Custom exception for invalid input values."""

    def __init__(self, value, message="Invalid input value"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.value}"

    def process_data(self, data):
        if not isinstance(data, int) or data < 0:
            raise InvalidInputError(data, "Data must be a non-negative integer")
        # Further processing
        return data * 2

if __name__ == '__main__' :
    try:
        ice = InvalidInputError(-5)
        result = ice.process_data(-5)
        print(f"Processed result: {result}")
    except InvalidInputError as e:
        print(f"Warning: {e}")
    except Exception as e:  # Catch other potential exceptions
        print(f"An unexpected error occurred: {e}")
