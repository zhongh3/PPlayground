import subprocess
import os
import pandas as pd


def parse_input(csv_file, in_file, out_dir, out_ext):
    cmds = []
    df = pd.read_csv(csv_file)
    for row in df.values:
        track, out_name, st_hh, st_min, st_sec, et_hh, et_min, et_sec = row
        out_name = out_name.replace(':', ' ')  # handle invalid char in file name
        cmds.append('ffmpeg -i {} -ss {:0>2d}:{:0>2d}:{:0>2d} -to {:0>2d}:{:0>2d}:{:0>2d} -c copy "{}.{}"'.format(
            in_file,
            st_hh,
            st_min,
            st_sec,
            et_hh,
            et_min,
            et_sec,
            out_dir + out_name,
            out_ext))

    return cmds


def main():
    # path = os.getcwd()
    csv_file = './data/' + 'input.csv'
    in_file = './data/' + '2015.m4a'
    out_ext = 'm4a'
    out_dir = './data/'
    cmds = parse_input(csv_file, in_file, out_dir, out_ext)

    for cmd in cmds:
        subprocess.run(cmd, shell=True)
    return cmds


if __name__ == "__main__":
    main()