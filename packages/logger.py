def logger(log):
    with open("History.txt" , "a") as f:
        f.write(log + "\n")
