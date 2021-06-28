'''for each step in steps_clean folder,
extract the respective screen and widget without the touch indicator'''

import os
import glob
import shutil

### input parameters you need to change ###
usage_root_dir = os.path.abspath('../../video_data_examples')
input_dir = 'steps_clean'
output_dir = 'ir_data'
### end of input parameters

def extract_screen(step_image_file, app_root_dir):
    filename = os.path.basename(step_image_file).replace('.jpg', '')
    frame_id_with_touch = str(filename).replace('bbox-', '')
    frame_id = int(frame_id_with_touch) - 1
    src_file = os.path.join(app_root_dir, 'detected_frames', 'bbox-' + '{0:0=4d}'.format(frame_id) + '.jpg')
    dst_file = os.path.join(app_root_dir, output_dir, filename + '-screen.jpg')
    # print(src_file, dst_file)
    shutil.copy(src_file, dst_file)

def extract_widget(step_image_file, app_root_dir):
    # TO DO
    print('extract widget...')

def main():
    for step_dir in glob.glob(usage_root_dir + '/*/' + input_dir):
        if not os.path.exists(step_dir.replace(input_dir, output_dir)):
            os.mkdir(step_dir.replace(input_dir, output_dir))
        app_root_dir = step_dir.replace(input_dir, '')
        for step_image_file in os.scandir(step_dir):
            # print(step_image_file.path) # full abs path
            if step_image_file.path.endswith('.jpg'):
                extract_screen(step_image_file, app_root_dir)
                extract_widget(step_image_file, app_root_dir)

if __name__ == '__main__':
    main()
    print('all done! :)')