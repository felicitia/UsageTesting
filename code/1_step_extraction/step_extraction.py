import json
import shutil, os

# read from detected_actions.json to extract action steps
# and put such bbox-xxx files into clicked_frames folder

frame_index = 0 #Index of the frame list
dir_to_videos = "Spring_data/AddCart/" # directory to v2s data of a particular usage

for folder in os.listdir(dir_to_videos):
    if os.path.isdir(os.path.join(dir_to_videos, folder)):
        dir_to_json = dir_to_videos+folder+"/detected_actions.json"
        dir_to_frames = dir_to_videos+folder+"/detected_frames/"
        dir_to_new_folder = dir_to_videos+folder+"/clicked_frames/"

        if not os.path.exists(dir_to_new_folder):
            os.makedirs(dir_to_new_folder)

        print("\nStarting "+folder)
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
            
            try:
                shutil.copy(imgdir, dir_to_new_folder+img)
            except FileNotFoundError:
                print(img+" does not exist")
            except:
                print("error")
            
        print(folder+" finished")
        file.close()

print("Done!")
