#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/1
# @Author  : zhangl
import datetime
import linecache
import os

# nltk.download('punkt')
from nltk.tokenize import sent_tokenize


# import nltk


def get_filename(filepath):
    return os.path.basename(filepath).split(".")[0]


def get_fileext(filepath):
    return os.path.splitext(filepath)[1]


def get_subtype(filepath):
    line5 = linecache.getline(filepath, 5).strip()
    if len(line5) == 0:
        return ("CHSEN", 5)
    else:
        line3 = linecache.getline(filepath, 3).strip().replace(" ", "")
        for w in line3:
            if '\u4e00' <= w <= '\u9fff':
                return ("CNS", 4)
        return ("EN", 4)


def sentence_split(str_centence):
    list_ret = list()
    for s_str in str_centence.split('.'):
        if '?' in s_str:
            list_ret.extend(s_str.split('?'))
        elif '!' in s_str:
            list_ret.extend(s_str.split('!'))
        elif ',' in s_str:
            splits = s_str.split(',')
            flag = True
            for s in splits:
                if len(s.split(" ")) < 8:
                    flag = False
            if flag:
                list_ret.extend(splits)
        elif len(s_str) > 15 and 'and' in s_str:
            and_spilts = s_str.split('and')
            flag = True
            for and_str in and_spilts:
                if len(and_str.split(" ")) < 8:
                    flag = False
            if flag:
                list_ret.extend(and_spilts)
        else:
            list_ret.append(s_str)
    return list_ret


def sentence_token_nltk(target):
    sent_tokenize_list = sent_tokenize(target)
    return sent_tokenize_list


def split_srt(filepath):
    filename = get_filename(filepath)
    fileext = get_fileext(filepath)
    timestr = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    subtype = get_subtype(filepath)

    linenums = []
    for i, line in enumerate(open(filepath, "r", encoding="UTF-8")):
        if i % subtype[1] == 0:
            linenums.append(int(line.strip()))

    subs_new = list()
    for num in linenums:
        timeline = linecache.getline(filepath, num * subtype[1] + 2).strip()
        timeline_split = timeline.split(" --> ")
        day = datetime.datetime.now().strftime("%Y-%m-%d ")
        timestr_start = day + timeline_split[0]
        timestr_end = day + timeline_split[1]
        time_start = datetime.datetime.strptime(timestr_start, "%Y-%m-%d %H:%M:%S,%f")
        time_end = datetime.datetime.strptime(timestr_end, "%Y-%m-%d %H:%M:%S,%f")
        time_period = round(time_end.timestamp() - time_start.timestamp(), 3)
        # print(time_period)
        words = linecache.getline(filepath, num * subtype[1] + 3).strip()
        if subtype[0] == "EN":
            count = len(words.split(" "))
            # print(words,count)
            if count < 20:
                subs_new.append((timeline, words))
            else:
                time_start_temp = time_start
                words_splits = sentence_split(words)
                for word in words_splits:
                    word_time = round(time_period * ((len(word.split(" ")) / count)), 3)
                    word_time_end = time_start_temp + datetime.timedelta(seconds=word_time)
                    # print(time_start_temp, word_time_end, word)
                    time_line_temp = time_start_temp.strftime("%H:%M:%S,%f")[0:12] + " --> " \
                                     + word_time_end.strftime("%H:%M:%S,%f")[0:12]
                    subs_new.append((time_line_temp, word))
                    time_start_temp = word_time_end

    target = filename + "_" + timestr + fileext
    writer = open(target, "w")
    for i, sub in enumerate(subs_new):
        writer.write(str(i) + "\n")
        writer.write(sub[0] + "\n")
        writer.write(sub[1] + "\n")
        writer.write("\n")
    writer.flush()
    writer.close()
    return (target, subtype)


def write_en_txt(target, subtype):
    if subtype[0] == "EN":
        txt = list()
        for i, line in enumerate(open(target, "r", encoding="UTF-8"), start=1):
            print(i)
            if i % subtype[1] == 3:
                txt.append(line.strip())
        writer = open(get_filename(target) + ".txt", "w")
        for l in txt:
            writer.write(str(l) + "\n")
        writer.flush()
        writer.close()


if __name__ == '__main__':
    target, subtype = split_srt("C:/Project/Python/scripts/file-tool/EN_猫鼠游戏.srt")
    write_en_txt(target, subtype)