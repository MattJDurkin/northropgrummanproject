import pathlib
import csv
import os
import shutil

currdir = str(pathlib.Path(__file__).parent.resolve())
print(currdir + "/n")

# with open('%s/train.csv' % currdir, newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)
#     for row in reader:
#         img = row[0]
#         cat = int(row[1])
#         shutil.copy("%s\\train\images\%s" %(currdir,img), "%s\\categories\cat%d\%s" %(currdir,cat,img))
#         print(img + str(cat))

with open('%s/sample_submission_ns2btKE.csv' % currdir, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        img = row[0]
        shutil.copy("%s\\train\images\%s" %(currdir,img), "%s\\categories\\cat1_1\%s" %(currdir,img))
        print(img)