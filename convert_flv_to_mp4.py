import os
import subprocess


def main():
    # path = os.getcwd() + "/AKB/"
    path = os.getcwd()

    files = os.listdir(path)
    count = 0

    for item in files:
        if item.find(".flv") >= 0:
            count += 1
            print(item)
            output = item.split("flv")[0] + "mp4"
            print(output)

            os.chdir(path)
            subprocess.call(['ffmpeg', '-i', item, '-c', 'copy', output])

            os.remove(item)

    if count == 0:
        print("Couldn't find any *.flv file in {}.".format(path))
        return

    print("Converted {} *.flv to *.mp4".format(count))


if __name__ == "__main__":
    main()