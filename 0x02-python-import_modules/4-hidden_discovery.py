#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    diff = dir(hidden_4)
    for a in range(0, len(diff)):
        if diff[a][:2] != "__":
            print("{}".format(diff[a]))
