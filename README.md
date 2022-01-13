# SpamClassification

Fine-Tuning BERT for Spam Classification

## Prerequisite

- Linux
- Python 3
- PyTorch 1.3 or higher
- CUDA 9.0 or higher

## Installation

a. Create a conda virtual environment and activate it

```bash
conda create -n spam-cls python=3.7.0
conda activate spam-cls
```

b. Install PyTorch following the [official instructions](https://pytorch.org/), e.g.,

```bash
conda install pytorch -c pytorch
```

c. Install requirements

```bash
pip install -r requirements.txt
```

## Data Augmentation

Based on [SMS and review dataset](https://github.com/Giruvegan/stoneskipping), we synthesize a larger spam text
dataset with custom augmentation techniques. The dataset before augmentation is placed
in [dataset/original](dataset/original) and the augmented version is placed in [dataset/augmented](dataset/augmented).
The augmented dataset is generated with  `spam_data_augment.py` and `ham_data_augment.py`:

```bash
python spam_data_augment.py dataset/original/test/spam.txt spam_aug.txt
python ham_data_augment.py dataset/original/test/ham.txt ham_aug.txt
```

See [augment/README.md](augment/README.md) for more details.

## Quick Run

To test the [pre-trained model](https://drive.google.com/file/d/1IqkXfJjjYmj1Hj7n_2q83vCMKtlZpcSK/view?usp=sharing), run

```bash
python test.py configs/bert.toml ${PATH_TO_MODEL}
```

To test on your own dataset, please modify `test_dir` in config file.

## Training

```bash
python train.py ${CONFIG}
```

For example, use bert as backbone

```bash
python train.py configs/bert.toml
```

## Testing

```bash
python train.py ${CONFIG} ${CHECKPOINT}
```

## License

This project is under Apache-2.0 License, see [LICENSE](./LICENSE) for more details

## Acknowledgement

We
thank [Bert-Chinese-Text-Classification-PyTorch](https://github.com/649453932/Bert-Chinese-Text-Classification-Pytorch)
, [textConversion](https://github.com/Niefee/textConversion), [AbstractCN](https://github.com/blackfrog638/AbstractCN)
, [zh2emoji](https://github.com/techkang/zh2emoji) for their work,
and [StoneSkipping](https://github.com/Giruvegan/stoneskipping)
, [SimilarCharacter](https://github.com/contr4l/SimilarCharacter) for sharing dataset  
