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

We use seven types of augmentation method in this project, see [augment/README.md](augment/README.md) for more details

```bash
python augment.py ${PATH_TO_INPUT} --output ${PATH_TO_OUTPUT}
```

For example,

```bash
python augment.py dataset/train/spam.txt --output spam_aug.txt
```

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

We thank [Bert-Chinese-Text-Classification-PyTorch](https://github.com/649453932/Bert-Chinese-Text-Classification-Pytorch), [textConversion](https://github.com/Niefee/textConversion), [AbstractCN](https://github.com/blackfrog638/AbstractCN), [zh2emoji](https://github.com/techkang/zh2emoji) for their work, and [StoneSkipping](https://github.com/Giruvegan/stoneskipping), [SimilarCharacter](https://github.com/contr4l/SimilarCharacter) for sharing dataset  
