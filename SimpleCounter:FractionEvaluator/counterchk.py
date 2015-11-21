from counter import Counter

def main():
    print("Test starting ...")

    # Create the counter
    counter = Counter()

    # Display the initial counter value (must be 0)
    print("Counter value is:", counter.get())
    if counter.get() != 0:
            print("Test failed!")

    # Push it three times
    counter.push()
    counter.push()
    counter.push()

    # Display the counter value again (must be 3 now)
    print("Counter value is:", counter.get())
    if counter.get() != 3:
            print("Test failed!")

    # Down the counter by 2
    counter.down()
    counter.down()

    # Display the counter value again (must be 1 now)
    print("Counter value is:", counter.get())
    if counter.get() != 1:
            print("Test failed!")

    # Down the counter by another 2
    counter.down()
    counter.down()

    # Display the counter value again (must be 0 not -1)
    print("Counter value is:", counter.get())
    if counter.get() != 0:
            print("Test failed!")

    # Push it another three times and reset
    counter.push()
    counter.push()
    counter.push()
    counter.reset()

    # Display the counter value again (must be 0)
    print("Counter value is:", counter.get())
    if counter.get() != 0:
            print("Test failed!")


# Execute the main function
main()
