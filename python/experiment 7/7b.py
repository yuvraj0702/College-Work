def greet(name, message="Good morning!"):
    print(f"Hello, {name}! {message}")

# Using default argument
greet("Alice")
# Output: Hello, Alice! Good morning!

# Overriding default argument
greet("Bob", "How are you?")
# Output: Hello, Bob! How are you?
