def repeat(message: str, num_times: int):
    """Usage: repeat <message> [--num_times <num>]

    Arguments:
        message  A message to print to the console.

    Options:
        -n, --num-times <num>  The number of times to print the message [default: 1].
    """
    for i in range(num_times):
        print(message)
