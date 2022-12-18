# video_id,frame_timestamp,entity_box_x1,entity_box_y1,entity_box_x2,entity_box_y2,label,entity_id,label_id,instance_id
# 0b4cacb1-970f-4ef0-85da-371d81f899e0,2007,635.3,626.17,727.6899999999999,749.3499999999999,0,0b4cacb1-970f-4ef0-85da-371d81f899e0_2007_2048:2,0,0b4cacb1-970f-4ef0-85da-371d81f899e0_2007_2048:2:0
# import pandas as pd
# import random
# df = pd.read_csv("./student_data/train/seg/0b4cacb1-970f-4ef0-85da-371d81f899e0_seg.csv")
import os
import csv
seg_dir = "./student_data/train/seg"
bbox_dir = "./student_data/train/bbox"
# video_name = "0b4cacb1-970f-4ef0-85da-371d81f899e0"
seg_files = sorted([os.path.join(seg_dir, x) for x in os.listdir(seg_dir)])
bbox_files = sorted([os.path.join(bbox_dir, x) for x in os.listdir(bbox_dir)])
output_dir = "train_merged.csv"
for k in range(len(seg_files)):
    # print(len(seg_files))
    video_name = seg_files[k].split("_")[-2].split("/")[-1]
    id = []
    start_frame = []
    end_frame = []
    speaking  = []
    ttm = []
    with open(seg_files[k], 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            id.append(row[0])
            start_frame.append(row[1])
            end_frame.append(row[2])
            ttm.append(row[3])
            if row[3] == "0":
                speaking.append("NOT_SPEAKING")
            else:
                speaking.append("SPEAKING_AUDIBLE")
    person_id = []
    frame_id = []
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    with open(bbox_files[k], 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            person_id.append(row[0])
            frame_id.append(row[1])
            x1.append(row[2])
            x2.append(row[3])
            y1.append(row[4])
            y2.append(row[5])
    video_id =[] 
    frame_timestamp =[]
    entity_box_x1 =[]
    entity_box_y1 =[]
    entity_box_x2 =[]
    entity_box_y2 =[]
    label = []
    entity_id =[]
    label_id =[]
    instance_id =[]
    # print(end_frame)
    for i in range(1,len(id)):
        for j in range(int(end_frame[i]) - int(start_frame[i]) + 1):
            video_id.append(video_name)
            frame_timestamp.append(j + int(start_frame[i]))
            entity_box_x1.append(x1[int(start_frame[i])+j])
            entity_box_x2.append(x1[int(start_frame[i])+j])
            entity_box_y1.append(y1[int(start_frame[i])+j])
            entity_box_y2.append(y2[int(start_frame[i])+j])
            label.append(speaking[i])
            entity_id.append(video_name+"_"+str(int(start_frame[i])/30)+"_"+str(int(end_frame[i])/30)+":"+str(id[i]))
            label_id.append(ttm[i])
            instance_id.append(video_name+"_"+str(int(start_frame[i])/30)+"_"+str(int(end_frame[i])/30)+":"+str(id[i])+":"+str(ttm[i]))
    with open(output_dir, 'a') as f:
        if k ==1 :
            f.write('video_id,frame_timestamp,entity_box_x1,entity_box_y1,entity_box_x2,entity_box_y2,label,entity_id,label_id,instance_id\n')
        for i in range(len(video_id)):
            if entity_box_x1[i] == "-1":
                continue
            f.write('{},{},{},{},{},{},{},{},{},{}\n'.format(video_id[i],frame_timestamp[i]/30,entity_box_x1[i],entity_box_y1[i],entity_box_x2[i],entity_box_y2[i],label[i],entity_id[i],label_id[i],instance_id[i]))
        f.close   
# video_id,frame_timestamp,entity_box_x1,entity_box_y1,entity_box_x2,entity_box_y2,label,entity_id,label_id,instance_id
# _mAfwH6i90E,1080.0,0.39375,0.0277778,0.679167,0.469444,NOT_SPEAKING,_mAfwH6i90E_1080_1140:1,0,_mAfwH6i90E_1080_1140:1:0