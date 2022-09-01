from . import placeholder

def generate(payload):
    img = placeholder.placeholder(payload)
    img.save('cache/out_weekly.png', 'PNG', quality=100, optimize=True)