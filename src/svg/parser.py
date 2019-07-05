from svgpathtools import svg2paths
paths, attributes = svg2paths("example/note.svg")

SAMPLES_PER_PX = 1

myPaths = {}
for path,attr in zip(paths, attributes):
    myPathList = []
    pathLength = path.length()
    pathColour = attr['stroke']
    numSamples = int(pathLength * SAMPLES_PER_PX)
    for i in range(numSamples):
        #parametric length = ilength(geometric length)
        myPathList.append(path.point(path.ilength(pathLength * i / (numSamples-1))))
    myPaths[pathColour] = np.array(myPathList)


print(myPaths)
