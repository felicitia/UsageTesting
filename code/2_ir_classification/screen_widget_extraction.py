'''for each step in steps_clean folder,
extract the respective screen and widget without the touch indicator'''

### NEED TO CONSIDER SPECIAL CASES IN THE FILENAME

import os
import glob
import shutil
import json

### input parameters you need to change ###
usage_root_dir = os.path.abspath('../../video_data_examples')
input_dir = 'steps_clean'
output_dir = 'ir_data'
### end of input parameters

def extract_screen(step_image_file, app_root_dir):
    filename = os.path.basename(step_image_file).replace('.jpg', '')
    if 'swipe' in filename:
        return # don't copy the screen associated with swipe action
        # swipe_direction = filename.split('-swipe-')[1]
        # filename = filename.replace('-swipe-' + swipe_direction, '')
        # print('filename', filename)
    elif 'long' in filename:
        filename = filename.replace('-long', '')
    frame_id_with_touch = str(filename).replace('bbox-', '')
    frame_id = int(frame_id_with_touch) - 1
    src_file = os.path.join(app_root_dir, 'detected_frames', 'bbox-' + '{0:0=4d}'.format(frame_id) + '.jpg')
    dst_file = os.path.join(app_root_dir, output_dir, os.path.basename(os.path.normpath(app_root_dir)) + '-' + filename + '-screen.jpg')
    # print(src_file, dst_file)
    shutil.copy(src_file, dst_file)

def extract_widget(step_image_file, app_root_dir, detected_actions_json):
    # make sure to name the file with app_roo_folder name in the beginning
    filename = os.path.basename(step_image_file).replace('.jpg', '')
    # print(filename)
    if 'swipe' in filename:
        return  # skip swipe steps since they don't need ir classification
    elif 'long' in filename:
        filename = filename.replace('-long', '')
    frame_id_with_touch = int(str(filename).replace('bbox-', ''))
    x, y = get_coordinates(detected_actions_json, frame_id_with_touch)


def get_coordinates(detected_actions_json, frame_id):
    for item in detected_actions_json:
        for tap in item['taps']:
            if tap['frame'] == frame_id:
                return tap['x'], tap['y']
    print('no frame', frame_id, 'found...')


def main():
    for step_dir in glob.glob(usage_root_dir + '/*/' + input_dir):
        if not os.path.exists(step_dir.replace(input_dir, output_dir)):
            os.mkdir(step_dir.replace(input_dir, output_dir))
        app_root_dir = step_dir.replace(input_dir, '') # /Users/yixue/Documents/Research/UsageTesting/UsageTesting-Repo/video_data_examples/6pm-video-signin-3/
        print(app_root_dir)
        with open(os.path.join(app_root_dir, 'detected_actions.json'), 'r') as f:
            detected_actions_json = json.load(f)
            for step_image_file in os.scandir(step_dir):
                # print(step_image_file.path) # full abs path
                if step_image_file.path.endswith('.jpg'):
                    extract_screen(step_image_file, app_root_dir)
                    extract_widget(step_image_file, app_root_dir, detected_actions_json)

if __name__ == '__main__':
    main()
    print('all done! :)')