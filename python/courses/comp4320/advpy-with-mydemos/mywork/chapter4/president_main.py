
from president import President


p = President(1)
fmt = "{0} was born at {1}, {2} on {3}"
print(fmt.format(p.first_name, p.birth_place, p.birth_state, p.birth_date))
