from django import template

register = template.Library()


@register.filter
def salary_num(value_int):
    value = str(value_int)
    res = [value[0:len(value) % 3]]
    slice_val = value[len(value) % 3:len(value)]
    for gnum in range(0, len(slice_val), 3):
        res.append(slice_val[gnum:gnum + 3])
    return " ".join(res)


@register.filter
def dot_skill(skills):
    skill_list = skills.split(', ')
    return ' • '.join(skill_list)
