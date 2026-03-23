# Single quotes and double quotes are interchangeable — choose based on content
name = 'Lea'
city = "Stockholm"

# Use double quotes when your string contains an apostrophe
message = "It's a beautiful day"
message_city = f"It's a beautiful day in {city}!"

# Use single quotes when your string contains double quotes
quote = 'He said "hello" to everyone'
quote_name = f'{name} said "hello" to everyone'

print(message_city)
print(quote_name)