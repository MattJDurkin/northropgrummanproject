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

# with open('%s/sample_submission_ns2btKE.csv' % currdir, newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)
#     for row in reader:
#         img = row[0]
#         shutil.copy("%s\\train\images\%s" %(currdir,img), "%s\\categories\\cat1_1\%s" %(currdir,img))
#         print(img)

path2 = str(pathlib.Path(__file__).parent.parent.resolve()) + "\surfaced_submarine_photos"

iter = 0

for file in os.listdir(str(pathlib.Path(__file__).parent.parent.resolve()) + "\surfaced_submarine_photos"):
    shutil.copy("%s\\%s" %(path2,file), "%s\\categories\\sub\img_%d.jpg" %(currdir,iter))
    print(str(iter))
    iter += 1
