This repository provides the dataset introduced in our paper titled ["K-pop Lyric Translation: Dataset, Analysis, and Neural Modelling."](https://arxiv.org/abs/2309.11093)

If you find this dataset useful for your research, please consider citing our paper. (Our paper is still under review as of December 31, 2023)

```
@misc{kim2023kpop,
  title={K-pop Lyric Translation: Dataset, Analysis, and Neural Modelling},
  author={Haven Kim and Jongmin Jung and Dasaem Jeong and Juhan Nam},
  year={2023},
  eprint={2309.11093},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
}
```

Please note that our dataset is related to alignment, not the lyrics themselves. We do not claim ownership of the lyrics in any way.

1. Obtain Lyrical Text
To obtain lyrics for the corresponding title and artist, please refer to meta.csv and retrieve them manually. We provide an example code for retrieving lyrics using the Genius Lyrics API and refining them. To execute the code, follow these steps:

```
python crawl.py
python refine.py
```

2. Match Symbolic Data to Lyrical Text
In symbol.json, each line is represented by the initials of words as well as the first and last words. You will need to find the corresponding line manually. We provide an example code for matching the symbolic data to lyrical text in match.py. To execute the code, follow these steps:

```
python crawl.py
python refine.py
```
