file_= " Sila Nerangalil Sila Manithargal (2022) Tamil HQ HDRip - 1080p - HEVC - x265 - (DD+5.1 - 192Kbps & AAC 2.0) - 1.5GB - ESub"

keyword = ""
for split_word in file_:

    if split_word.isdigit():
        
        break
        
    else:
        keyword = keyword + split_word +""
re = len(keyword)-1
print(f"keyword :{keyword[0:re]} \n\nTitle : {file_}")


