def number_generator(values):
    for val in values:
        yield val

def even_number_generator(start_val, end_val):
    for val in range(start_val, end_val + 1):
        if val % 2 == 0:
            yield val

def odd_number_generator(start_val, end_val):
    for val in range(start_val, end_val + 1):
        if val % 2 != 0:
            yield val

def fibonacci_generator():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

def prime_number_generator(max_limit):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    for val in range(2, max_limit + 1):
        if is_prime(val):
            yield val

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node:
        yield node.val
        yield from pre_order_traversal(node.left)
        yield from pre_order_traversal(node.right)

def in_order_traversal(node):
    if node:
        yield from in_order_traversal(node.left)
        yield node.val
        yield from in_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        yield from post_order_traversal(node.left)
        yield from post_order_traversal(node.right)
        yield node.val

def dfs_traversal(graph_structure, start_node):
    visited_nodes = set()
    stack = [start_node]
    while stack:
        current_node = stack.pop()
        if current_node not in visited_nodes:
            yield current_node
            visited_nodes.add(current_node)
            stack.extend(reversed(graph_structure[current_node]))

from collections import deque

def bfs_traversal(graph_structure, start_node):
    visited_nodes = set()
    queue = deque([start_node])
    while queue:
        current_node = queue.popleft()
        if current_node not in visited_nodes:
            yield current_node
            visited_nodes.add(current_node)
            queue.extend(graph_structure[current_node])

def dict_keys_generator(dictionary):
    for key in dictionary.keys():
        yield key

def dict_values_generator(dictionary):
    for val in dictionary.values():
        yield val

def dict_items_generator(dictionary):
    for item in dictionary.items():
        yield item

def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

def string_chars_generator(text_string):
    for char in text_string:
        yield char

def unique_elements_generator(input_list):
    seen_elements = set()
    for element in input_list:
        if element not in seen_elements:
            seen_elements.add(element)
            yield element

def reverse_list_generator(input_list):
    for element in reversed(input_list):
        yield element

def cartesian_product_generator(list1, list2):
    for item1 in list1:
        for item2 in list2:
            yield (item1, item2)

from itertools import permutations

def permutations_generator(input_list):
    for perm in permutations(input_list):
        yield perm

from itertools import combinations

def combinations_generator(input_list):
    for r in range(1, len(input_list) + 1):
        for comb in combinations(input_list, r):
            yield comb

def tuple_list_generator(input_list):
    for tup in input_list:
        yield tup

def parallel_lists_generator(*lists):
    for items in zip(*lists):
        yield items

def flatten_list_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_generator(item)
        else:
            yield item

def nested_dict_generator(dictionary):
    for key, val in dictionary.items():
        if isinstance(val, dict):
            yield from nested_dict_generator(val)
        else:
            yield (key, val)

def powers_of_two_generator(power_limit):
    for i in range(power_limit + 1):
        yield 2 ** i

def powers_of_base_generator(base, max_limit):
    exponent = 0
    result = 1
    while result <= max_limit:
        yield result
        exponent += 1
        result = base ** exponent

def squares_generator(start_val, end_val):
    for val in range(start_val, end_val + 1):
        yield val ** 2

def cubes_generator(start_val, end_val):
    for val in range(start_val, end_val + 1):
        yield val ** 3

def factorials_generator(limit):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    for i in range(limit + 1):
        yield factorial(i)

def collatz_sequence_generator(number):
    while number != 1:
        yield number
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
    yield 1

def geometric_progression_generator(first_term, ratio, max_limit):
    term = first_term
    while term <= max_limit:
        yield term
        term *= ratio

def arithmetic_progression_generator(first_term, difference, max_limit):
    term = first_term
    while term <= max_limit:
        yield term
        term += difference

def running_sum_generator(values):
    running_total = 0
    for val in values:
        running_total += val
        yield running_total

def running_product_generator(values):
    running_total = 1
    for val in values:
        running_total *= val
        yield running_total
