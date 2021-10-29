import pathlib
import csv
import os
import shutil

currdir = str(pathlib.Path(__file__).parent.resolve())


#copy over data from kaggle

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

# copy sub pictures with new names

# path2 = str(pathlib.Path(__file__).parent.parent.resolve()) + "\surfaced_submarine_photos"

# iter = 0

# for file in os.listdir(str(pathlib.Path(__file__).parent.parent.resolve()) + "\surfaced_submarine_photos"):
#     shutil.copy("%s\\%s" %(path2,file), "%s\\categories\\sub\img_%d.jpg" %(currdir,iter))
#     print(str(iter))
#     iter += 1

# path3 = str(pathlib.Path(__file__).parent.parent.resolve()) + "\\fishing_boat_photos"

# iter = 0

# for file in os.listdir(str(pathlib.Path(__file__).parent.parent.resolve()) + "\\fishing_boat_photos"):
#     shutil.copy("%s\\%s" %(path3,file), "%s\\categories\\fishing\img_%d.jpg" %(currdir,iter))
#     print(str(iter))
#     iter += 1


path4 = str(pathlib.Path(__file__).parent.parent.resolve()) + "\\aircraft_carrier_photos"

iter = 0

for file in os.listdir(str(pathlib.Path(__file__).parent.parent.resolve()) + "\\aircraft_carrier_photos"):
    shutil.copy("%s\\%s" %(path4,file), "%s\\categories\\ac_carrier\img_%d.jpg" %(currdir,iter))
    print(str(iter))
    iter += 1