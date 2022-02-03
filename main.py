import base64
import os
import argparse
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input_dir', default='./input', type=str,
                        help='Input directory for image(s)')
    parser.add_argument('--output', dest='output_file', default='./output.json', type=str,
                        help='Output file name')
    args = parser.parse_args()
    input_dir = args.input_dir
    output_file = args.output_file

    output_dict = dict()

    for sub_folder in os.listdir(input_dir):
        sub_path = os.path.join(input_dir, sub_folder)
        base64_arr = dict()
        for img in os.listdir(sub_path):

            with(open(os.path.join(sub_path, img), 'rb')) as f:
                img_byte = f.read()
                img_base64 = base64.b64encode(img_byte)
                img_base64_str = img_base64.decode('utf-8')
                base64_arr[img] = img_base64_str

        output_dict[sub_folder] = base64_arr

    with open(output_file, 'w') as f:
        json.dump(output_dict, f)






