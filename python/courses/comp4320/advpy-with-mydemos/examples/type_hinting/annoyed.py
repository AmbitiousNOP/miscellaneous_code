from typing import Optional


def annoy_cat(times: Optional[int]) -> str:
    return 'meow' * times

print(annoy_cat(3))
print(annoy_cat(None))
