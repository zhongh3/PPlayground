import subprocess
import os
import pandas as pd


def parse_input(csv_file, in_file, out_dir, out_ext, artist, album, re_encode=False):
    cmds = []
    if re_encode:
        codec = '-c:a libfdk_aac -b:a 256k -ar 44100 -ac 2 -vn'
    else:
        codec = '-c copy'

    df = pd.read_csv(csv_file)
    for row in df.values:
        track, out_name, st_hh, st_min, st_sec, et_hh, et_min, et_sec = row
        out_name = out_name.replace(':', ' ')  # handle invalid char in file name
        cmds.append('ffmpeg -i {} -ss {:0>2d}:{:0>2d}:{:0>2d} -to {:0>2d}:{:0>2d}:{:0>2d} {} '
                    '-metadata track={} -metadata title="{}" -metadata album_artist="{}" '
                    '-metadata album="{}" {}"{:0>2d} {}.{}"'.format(
            in_file,
            st_hh,
            st_min,
            st_sec,
            et_hh,
            et_min,
            et_sec,
            codec,
            track,
            out_name,
            artist,
            album,
            out_dir,
            track,
            out_name,
            out_ext))

    return cmds


def main():
    # path = os.getcwd()
    csv_file = './data/' + 'input.csv'
    in_file = './data/' + '2015.m4a'
    out_ext = 'm4a'
    out_dir = './data/'
    artist = '柴咲コウ'
    album = '2015 Live'
    re_encode = True
    commands = parse_input(csv_file, in_file, out_dir, out_ext, artist, album, re_encode=re_encode)

    for cmd in commands:
        print(cmd)
        # subprocess.run(cmd, shell=True)
    return commands


if __name__ == "__main__":
    main()