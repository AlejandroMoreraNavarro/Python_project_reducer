REGISTRY = {}

def register(name: str):
    def decorator(func):
        REGISTRY[name] = func
        return func
    return decorator

@register("plugin_a")
def plugin_a_func() -> str:
    return "plugin a executed"
