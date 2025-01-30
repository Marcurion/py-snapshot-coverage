from itertools import product

class Generator:

    def __init__(self):
        pass

    def generate_combinations(self, previous_combinations, *lists):
        """
        Generate all possible combinations from a variable number of lists while preserving order.

        :param previous_combinations: Previously generated combinations to maintain order.
        :param lists: Multiple lists containing possible values.
        :return: List of tuples representing all possible combinations.
        """
        # Generate all possible combinations
        all_combinations = list(product(*lists))

        if previous_combinations is None:
            return all_combinations  # First call, return all combinations

        # Preserve previous combinations
        previous_set = set(previous_combinations)
        new_combinations = [combo for combo in all_combinations if combo not in previous_set]

        return previous_combinations + new_combinations

if __name__ == '__main__':

    # Example Usage:
    generator = Generator()

    # Initial lists
    strings = ["a", "b"]
    integers = [1, 2]
    booleans = [True, False]

    # First round of combinations
    combinations = generator.generate_combinations(None, strings, integers, booleans)
    print("First round:", combinations)

    # Extend one of the lists
    strings.append("c")

    # Second round of combinations
    combinations = generator.generate_combinations(combinations, strings, integers, booleans)
    print("Second round:", combinations)

    # Extend another list
    integers.append(3)

    # Third round of combinations
    combinations = generator.generate_combinations(combinations, strings, integers, booleans)
    print("Third round:", combinations)
