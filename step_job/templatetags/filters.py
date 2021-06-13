from django import template

register = template.Library()


@register.filter
def salary_num(value_int):
    my_val = str(value_int)
    res = [my_val[0:len(my_val) % 3]]
    slice_val = my_val[len(my_val) % 3:len(my_val)]
    for gnum in range(0, len(slice_val), 3):
        res.append(slice_val[gnum:gnum + 3])
    return " ".join(res)


@register.filter
def dot_skill(skills):
    skill_list = skills.split(', ')
    return ' • '.join(skill_list)
