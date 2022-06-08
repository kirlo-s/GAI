from . import placeholder

def generate(payload):
    img = placeholder.placeholder(payload)
    img.save('cache/out_information.png', 'PNG', quality=100, optimize=True)