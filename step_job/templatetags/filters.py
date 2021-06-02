from django import template

register = template.Library()

@register.filter
def salary_num(value_int):
    value=str(value_int)
    res = []
    res.append(value[0:len(value) % 3])
    slice_val = value[len(value) % 3:len(value)]
    for x in range(0, len(slice_val), 3):
        res.append(slice_val[x:x + 3])
    return " ".join(res)

