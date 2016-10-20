import csv
import collections

def slide(infile,outfile,window_size,excList):
    r=csv.reader(infile)
    w=csv.writer(outfile)
    # use queue data structure
    queue=collections.deque(maxlen=window_size)
    # get headers
    headers=next(r)
    l=[headers[0]]
    b = [item for item in range(len(headers)) if headers[item] in excList]
    #  1:5
    # print(reversed(range(window_size))
    for h in headers[1:(len(headers))]:
        #     reversed 2,1,0
        # print (h)
        if h not in excList:

            for i in reversed(range(window_size)):
                l.append("%s-%i"%(h,i))
        else:
                l.append("%s"%(h))
    # write last column

    w.writerow(l)
    # 1,2,3,4 (1,5)
    hrange=range(1,len(headers))

    for row in r:
         queue.append(row)
         if len(queue)==window_size:
            l=[queue[-1][0]]
             # print (l)
            for j in hrange:

                if j not in b:
                    for old in queue:
                        l.append(old[j])
            # write clearing price value
                else:
                    l.append(old[j])
            w.writerow(l)

ws=3
with open("./Datasets/smartGridTrainerData.csv","r") as inf:
    with open("slidedSmartGridData.csv","w") as outf:
        slide(inf,outf,ws,["solarflux","clearingprice"])




        # slide(inf,outf,ws,[3,4])
