import json
import shutil

frame_index = 0 #Index of the frame list
dir_to_json = 'detected_actions.json' #directory to json file
dir_to_frames = '/Users/jasonyee/Downloads/ACT-Mac-App/step_extraction/detected_frames/' #directory to the folder with frames
dir_to_new_folder = '/Users/jasonyee/Downloads/ACT-Mac-App/step_extraction/detected_frames/clicked_frames/' #directory to a new folder for the clicked frames

file = open(dir_to_json,)
data = json.load(file)

for j in range(len(data)):
    img_index = (data[j]['frames'][frame_index])
    
    if(len(str(img_index)) == 1):
        img = 'bbox-000'+str(data[j]['frames'][frame_index])+'.jpg'
    elif(len(str(img_index)) == 2):
        img = 'bbox-00'+str(data[j]['frames'][frame_index])+'.jpg'
    elif(len(str(img_index)) == 3):
        img = 'bbox-0'+str(data[j]['frames'][frame_index])+'.jpg'
    elif(len(str(img_index)) == 4):
        img = 'bbox-'+str(data[j]['frames'][frame_index])+'.jpg'

    imgdir = dir_to_frames+img
    print(img)
    
    shutil.move(imgdir, dir_to_new_folder+img)
    

file.close()
