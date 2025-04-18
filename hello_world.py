
def run(params):
    name = params.get("name", "World")
    return {"message": f"Hello, {name}!"}
