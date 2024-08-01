from typing import Optional


def annoy_cat(times: Optional[int] = None) -> str:
    if times is None:
        return 'meow'
    else:
        return 'meow' * times


print(annoy_cat(3))
print(annoy_cat(None))
