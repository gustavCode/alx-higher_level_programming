#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    d_names = dir(hidden_4)

    for i in range(len(d_names)):
        if d_names[i][:2] != "__":
            print(d_names[i])
