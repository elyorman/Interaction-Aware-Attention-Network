import os
from glob import glob

# Modify openSMILE paths HERE:
SMILEpath = '../../opensmile-2.3.0/bin/linux_x64_standalone_static/SMILExtract'
SMILEconf = '../../opensmile-2.3.0/config/emobase_v2.conf'


# Paths
audio_folder    = './wav/S1/'
features_folder = './extracted_features/'

def extract_iemocap(audio_folder, features_folder):
    # Load file list
    instances = glob(audio_folder+'wav_mod/*')
    all_files = []
    for i in instances:
        all_files += glob(i+'/*.wav')
    # Iterate through partitions and extract features
    if not os.path.exists(features_folder):
        os.mkdir(features_folder)       
    # Extract openSMILE features for the whole partition (LLD-only)
    for f in all_files:
        os.system(SMILEpath + ' -C ' + SMILEconf + ' -I ' + f + \
        ' -O ' + features_folder + f.split("/")[-1].replace('wav','arff'))

extract_iemocap(audio_folder, features_folder)