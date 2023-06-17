"""constants """
EXPECTED_BAKE_TIME = 40
TIME_TAKES = 2
def bake_time_remaining(remaining_time):
    """Calculate the bake time remaining.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - remaining_time

def preparation_time_in_minutes(number_layers):
    """Calculate the preparation time in minutes.
    :param number_of_layers: int - number of layersd is 2.
    :return: int - time taken (in minutes) derived from 'EXPECTED_BAKE_TIME'. Function that takes the actual number layers in lasagna as an argument and returns how many minutes it will take to create each layer of lasagna based on the `EXPECTED_BAKE_TIME`.
    """
    return number_layers * TIME_TAKES

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time.
    :param number_of_layers: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `TIME_TAKES`.
    """
    return number_of_layers*TIME_TAKES + elapsed_bake_time
    