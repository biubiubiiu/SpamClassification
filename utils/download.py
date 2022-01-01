import os

PRETRAINED_MODELS = {
    'bert': [
        'https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-chinese.tar.gz',
        'https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-chinese-vocab.txt'
    ],
    'ernie': ['http://image.nghuyong.top/ERNIE.zip'],  # NOTE: not available
}


def download_pretrained(name):
    """Download pretrained models"""

    if name not in PRETRAINED_MODELS:
        raise ValueError('Invalid name of pretrained model {}, supported models: {}'
                         .format(name, str(list(PRETRAINED_MODELS.keys()))))

    # Create model folder if it does not exist
    model_dir = os.path.join('../pretrained', name)
    os.makedirs(model_dir, exist_ok=True)

    # Download pretrained model
    for dl_url in PRETRAINED_MODELS[name]:
        dl_file = os.path.basename(dl_url)
        dst_file = os.path.join(model_dir, dl_file)
        print('>> downloading model {} archive {}'.format(name, dl_url))
        os.system('wget {} -O {}'.format(dl_url, dst_file))

        if dst_file.endswith('tar.gz'):
            # create tmp folder
            dst_dir_tmp = os.path.join(model_dir, 'tmp')
            os.system('mkdir {}'.format(dst_dir_tmp))
            # extract in tmp folder
            os.system('tar -zxf {} -C {}'.format(dst_file, dst_dir_tmp))
            # remove all (possible) subfolders by moving only files in dst_dir
            os.system('find {} -type f -exec mv -i {{}} {} \\;'.format(dst_dir_tmp, model_dir))
            # remove tmp folder
            os.system('rm -rf {}'.format(dst_dir_tmp))
            print('>> Extracted, deleting model {} archive {}...'.format(name, dl_file))
            os.system('rm {}'.format(dst_file))
        elif dst_file.endswith('zip'):
            os.system('unzip {}'.format(dst_file))  # TODO check


if __name__ == '__main__':
    download_pretrained('bert')
