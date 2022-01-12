# SpamClassification

Fine-Tuning BERT for Spam Classification

## Prerequisite

- Linux
- Python 3

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
