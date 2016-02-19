import os

def getpath():
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
    return path

def onlydirectories(path):
    fileslist = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
    directorieslist = os.listdir(path)
    [directorieslist.remove(x) for x in fileslist]
    return directorieslist

def onlyfiles(path):
    fileslist = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
    return fileslist


path = getpath()
domains = onlydirectories(path)

#print domains

for d in domains:
    dpath = "%s\%s" % (path,d)
   
    #print dpath
    sections = onlydirectories(dpath)
    #print sections
    for s in sections:
        spath = "%s\%s" % (dpath,s)
        SectionReportName = "%s\%s.md" % (dpath,s)
        freportSection = open(SectionReportName,'w')
        freportSection.write( "###%s  \n" % s )
       # print spath
        sScore = 0
        for file in os.listdir(spath):
            if file.endswith(".md"):
                filepath = "%s\%s" % (spath,file)
                fproblem = open(filepath,'r')
                #print filepath
                line = fproblem.readline()
                line = fproblem.readline()
                line = line.replace('*','')
                line = line.replace("Score:",'')
                sScore += int(line)
               # print sScore
                fproblem.close()
        freportSection.write("###*Section Score: %d*  \n" % sScore)
        print sScore

        for file in os.listdir(spath):
            if file.endswith(".md"):
                filepath = "%s\%s" % (spath,file)
                fproblem = open(filepath,'r')
                #print filepath
                
                fproblem = open(filepath,'r')
                freportSection.write(fproblem.read())
                fproblem.close()
        freportSection.close()


path = getpath()
domains = onlydirectories(path)
#print domains

for d in domains:
    dpath = "%s\%s" % (path,d)
    DomainReportName = "%s\%s.md" % (path,d)
    #print DomainReportName
    freportDomain = open(DomainReportName, 'w')
    freportDomain.write( "##%s   \n" % d )
    #print os.listdir(dpath)
    #print dpath
    files = onlyfiles(dpath)
    #print files
    for f in files:
         #if f.endsiwth(".md"):
            filepath = "%s\%s" % (dpath,f)
            #print filepath
            fsection = open(filepath,'r')
            [freportDomain.write(line) for line in fsection.readlines()]
            fsection.close()
    freportDomain.close()

#print domains
#print path

lreadmepath=path.split("\\")
lreadmepath.pop()
readmepath= "\\".join(lreadmepath)
readmeFile = "%s\Readme.md" % readmepath
freadme = open(readmeFile,'w')

for x in os.listdir(path):
    if x.endswith(".md"):
        fpath = "%s\%s" % (path,x)
        fdomain = open(fpath,'r')
        [freadme.write(line) for line in fdomain.readlines()]
        fdomain.close()

freadme.close()

