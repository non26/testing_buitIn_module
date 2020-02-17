import os


def auto_copy(level):
    if level== "--all":
        level = float("inf")
    def throughDirectory(path, count):
        itFile = iter(os.listdir(path))
        cnt = count
        for item in itFile:
            itemPath = path+"\\"+item
            if os.path.isfile(itemPath):
                print(" "*cnt*2+item)
            else:
                print(" "*(cnt)*2+item)
                if cnt < level:
                    cnt += 1
                    # recursive
                    throughDirectory(itemPath, cnt)
                    cnt -= 1
                else:
                    continue
    return throughDirectory
x = auto_copy("--all")
x(r"C:\Users\EiCh9001\PycharmProjects\PyNielsen\AutoNAD_NEW_editting", 1)