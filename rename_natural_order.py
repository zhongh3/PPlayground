import os


def rename_num(file, num, prefix, ext, n_digits):

    num = (n_digits - len(num)) * "0" + num  # append 0s in front
    new_name = prefix + num + file[file.find(ext):]

    return new_name


def main():
    prefix = "JP_2017-2018 - "
    ext = "."

    # path = os.getcwd()
    path = "./data/order/"

    files = os.listdir(path)
    # print(files)
    print("number of files in {} = {}".format(path, len(files)))

    # find the maximum number
    max_num = "0"
    for item in files:
        if item.find(prefix) == 0:
            num = item[len(prefix): item.find(ext)]
            # print(num)
            if int(num) > int(max_num):
                max_num = num
        else:
            print("===> other file: {}".format(item))

    print("maximum number = {}; no. of digits = {}".format(max_num, len(max_num)))

    # rename file if number of digits < max number of digits
    # e.g. if max = 10 (2 digits) --> rename 3 to 03
    for item in files:
        # print(item)
        if item.find(prefix) == 0:
            num = item[len(prefix): item.find(ext)]
            if len(num) < len(max_num):
                os.rename(path + item, path + rename_num(item, num, prefix, ext, len(max_num)))


if __name__ == "__main__":
    main()
