import os



def get_directory_files(path):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        f.extend(filenames)
        break
    return f


def get_article_names(article_list):
    names = []
    for a in article_list:
        pos = a.find('.')
        n = a[0:pos]
        names.append(n)
    return names

