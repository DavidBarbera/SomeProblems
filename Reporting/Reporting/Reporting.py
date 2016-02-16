import os


def onlydirectories(path):
    fileslist = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
    directorieslist = os.listdir(path)
    [directorieslist.remove(x) for x in fileslist]
    return directorieslist

#current working directory
wpath = os.getcwd()

#may be useful later on
#path1, path2 = os.path.split(wpath)

#path has directory with all domains
lpath = wpath.split('\\')
lpath.pop()
lpath.pop()
lpath.insert(len(lpath),'Solutions')
path = '\\'.join(lpath)

domains = onlydirectories(path)

print domains

for d in domains:
    dpath = "%s\%s" % (path,d)
    print dpath
    sections = onlydirectories(dpath)
    print sections
    for s in sections:
        spath = "%s\%s" % (dpath,s)
        SectionReportName = "%s\%s.md" % (dpath,s)
        freportSection = open(SectionReportName,'w')
        freportSection.write( "###%s  \n" % s )
        print spath
        for file in os.listdir(spath):
            if file.endswith(".md"):
                filepath = "%s\%s" % (spath,file)
                fproblem = open(filepath,'r')
                print filepath
                freportSection.write(fproblem.read())
                fproblem.close()
        freportSection.close()
