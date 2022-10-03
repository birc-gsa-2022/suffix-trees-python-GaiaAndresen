from dataclasses import dataclass

@dataclass
class Leaf:
    label: tuple[int, int]
    parent: 'Tree | None' = None

@dataclass
class Tree:
    children: dict[str, 'Tree | Leaf'] #Could also be a list based on ex. ord()
    label: tuple[int, int]
    parent: 'Tree | None' = None
