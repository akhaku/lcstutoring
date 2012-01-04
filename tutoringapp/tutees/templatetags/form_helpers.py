from django import template

register = template.Library()

def rows(value, arg):
    """
    Changes the rows of a textarea widget
    """
    attrs = value.field.widget.attrs
    orig = attrs['rows'] if 'rows' in attrs else None

    attrs['rows'] = arg
    rendered = str(value)

    if orig:
        attrs['rows']
    else:
        del attrs['rows']

    return rendered
register.filter('rows', rows)

def size(value, arg):
    """
    Add a size to a form widget 
    """
    attrs = value.field.widget.attrs
    orig = attrs['size'] if 'size' in attrs else None

    attrs['size'] = arg
    rendered = str(value)

    if orig:
        attrs['size']
    else:
        del attrs['size']

    return rendered
register.filter('size', size)
