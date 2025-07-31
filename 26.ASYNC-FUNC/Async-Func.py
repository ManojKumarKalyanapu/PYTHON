import asyncio

# Define an async function
async def greet(name):
    print(f"👋 Hello, {name}!")
    await asyncio.sleep(2)  # Simulate an I/O operation (e.g., network, file)
    print(f"👋 Goodbye, {name}!")

# Define another async function
async def main():
    # Run two greet functions concurrently
    await asyncio.gather(
        greet("Alice"),
        greet("Bob")
    )

# Run the async main function
asyncio.run(main())
