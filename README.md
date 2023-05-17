# ImageArg-Shared-Task-2023

## Information
Webpage: [ImageArg Shared Task](https://imagearg.github.io/)

Join Slack: [ImageArg Slack](https://join.slack.com/t/imagearg/shared_invite/zt-1ss5hdb6d-eNCaWOAEe4O_8UE1gQxIxA)

Signup Form: [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSci3TSw6ylcWnjXQsoUjh3buAQx7IdgiJwrJDR2pDHMm8DIpQ/viewform)

## Introduction
There has been a recent surge of interest in developing methods and corpora to improve and evaluate persuasiveness in natural language applications. However, these efforts have mainly focused on the textual modality, neglecting the influence of other modalities. [Liu et al.](https://aclanthology.org/2022.argmining-1.1.pdf) introduced a new multimodal dataset called “ImageArg” This dataset includes persuasive tweets along with associated images, aiming to identify the image's stance towards the tweet and determine its persuasiveness score concerning a specific topic. The ImageArg dataset is a significant step towards advancing multimodal persuasive text analysis and opens up avenues for exploring the persuasive impact of images in social media. To further this goal, we designed this shared task, which utilizes the ImageArg dataset to advance multimodal persuasiveness techniques.

## Dataset
Please note that the downloaded dataset should only be used for participating in ImageArg Shared Task. Any other use is explicitly prohibited. Any participants are not allowed to redistribute the dataset per Twitter Developer Policy: https://developer.twitter.com/en/developer-terms/policy.

All the tweets are instantly crawled from Twitter. We are aware that some tweets could not be available when participants start to download (e.g., a tweet is deleted by its author). We will regularly monitor the whole dataset and provide data patches to replace invalid tweets. Therefore, it is required to fill out the [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSci3TSw6ylcWnjXQsoUjh3buAQx7IdgiJwrJDR2pDHMm8DIpQ/viewform) in order to receive data patches and to participate in the shared task.

Please run `python get_tweet_data.py`

## Citation
``````
@inproceedings{liu-etal-2022-imagearg,
    title = "{I}mage{A}rg: A Multi-modal Tweet Dataset for Image Persuasiveness Mining",
    author = "Liu, Zhexiong  and Guo, Meiqi  and Dai, Yue  and Litman, Diane",
    booktitle = "Proceedings of the 9th Workshop on Argument Mining",
    month = oct,
    year = "2022",
    address = "Online and in Gyeongju, Republic of Korea",
    publisher = "International Conference on Computational Linguistics",
    url = "https://aclanthology.org/2022.argmining-1.1",
    pages = "1--18"
    }
``````

## Organizer

Zheixong Liu, Mohamed Elaraby, Yang Zhong, and Diane Litman (University of Pittsburgh)