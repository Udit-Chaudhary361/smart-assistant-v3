def logger(log):
    with open(r"C:\AI Agent\Smart Assistant\Smart Assistant V3\data\History.txt" , "a") as f:
        f.write(log + "\n")