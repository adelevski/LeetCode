from collections import defaultdict

paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]


def findDuplicate(paths):
    c = defaultdict(list)
    # key = content, value = tuple(path,name)
    for path in paths:
        path = path.split(" ")
        folder = path[0]
        for s in path[1:]:
            s = s.split(".txt")
            name = s[0]
            content = s[1]
            c[content].append((folder,name))
    output = []
    for k,v in c.items():
        if len(v)>1:
            tmp = []
            for path,name in v:
                tmp.append(path+'/'+name+'.txt')
            output.append(tmp)
    return output

print(findDuplicate(paths))



