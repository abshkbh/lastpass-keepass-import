import csv
import sys


def add_quotes_if_comma_present(arg):
    if "," in arg:
        return "\"" + arg + "\""
    return arg


def main():
    if len(sys.argv) < 1:
        print("keepass-to-lastpass <input-csv>")
        return

    with open(sys.argv[1]) as csvfile:
        print("url,username,password,extra,name,grouping,fav")
        # This flag is to ignore the first row i.e. the title row. Since we've already inserted our own above.
        flag = True
        rows = csv.reader(csvfile, delimiter=',')
        for row in rows:
            if flag:
                flag = False
                continue

            group = add_quotes_if_comma_present(row[0])
            title = add_quotes_if_comma_present(row[1])
            username = add_quotes_if_comma_present(row[2])
            password = add_quotes_if_comma_present(row[3])
            url = add_quotes_if_comma_present(row[4])
            # If no url is given derive it from title.
            if not url:
                url = "www." + title + ".com"
            notes = add_quotes_if_comma_present(row[5])
            # notes maps to extras. grouping is left empty. fav is hardcoded to 0.
            print(url + "," + username + "," + password +
                  "," + notes + "," + title + "," + "," + "0")


if __name__ == "__main__":
    main()
