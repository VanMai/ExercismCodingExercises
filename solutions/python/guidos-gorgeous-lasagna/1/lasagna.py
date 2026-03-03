# 1. Define the EXPECTED_BAKE_TIME constant.
EXPECTED_BAKE_TIME = 40

# 2. Define the PREPARATION_TIME constant (minutes per layer).
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the total preparation time."""
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed cooking time (prep + bake)."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time