import csv
import sys


def main():
    print("Hello World!")
    if len(sys.argv) < 1:
        print("keepass-to-lastpass <input-csv>")
        return

    with open(sys.argv[1]) as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for row in rows:
            if "," in row[3]:
                print(row)


if __name__ == "__main__":
    main()
