# ImageArg-Shared-Task-2023

## Information

Webpage: [ImageArg Shared Task](https://imagearg.github.io/)

Join Slack: [ImageArg Slack](https://join.slack.com/t/imagearg/shared_invite/zt-1ss5hdb6d-eNCaWOAEe4O_8UE1gQxIxA)

Signup
Form: [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSci3TSw6ylcWnjXQsoUjh3buAQx7IdgiJwrJDR2pDHMm8DIpQ/viewform)

## Introduction

There has been a recent surge of interest in developing methods and corpora to improve and evaluate persuasiveness in
natural language applications. However, these efforts have mainly focused on the textual modality, neglecting the
influence of other modalities. [Liu et al.](https://aclanthology.org/2022.argmining-1.1.pdf) introduced a new multimodal
dataset called “ImageArg” This dataset includes persuasive tweets along with associated images, aiming to identify the
image's stance towards the tweet and determine its persuasiveness score concerning a specific topic. The ImageArg
dataset is a significant step towards advancing multimodal persuasive text analysis and opens up avenues for exploring
the persuasive impact of images in social media. To further this goal, we designed this shared task, which utilizes the
ImageArg dataset to advance multimodal persuasiveness techniques.

## Dataset

The dataset to download should only be used for participating in the ImageArg Shared Task. Any other use is explicitly
prohibited. Participants are not allowed to redistribute the dataset
per [Twitter Developer Policy](https://developer.twitter.com/en/developer-terms/policy).

All the tweets are instantly crawled from Twitter. Organizers are aware some tweets could not be available when
participants start to download (e.g., a tweet could be deleted by its author). Organizers will regularly monitor the
dataset to provide data patches that will replace invalid tweets with new annotated ones. Participants are required to
fill out
the [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSci3TSw6ylcWnjXQsoUjh3buAQx7IdgiJwrJDR2pDHMm8DIpQ/viewform)
in order to receive data patches and the shared task updates.

Please install `requirements.txt` dependencies and run `python get_train_dev_data.py` to download training and dev
datasets for both shared subtasks. The dataset downloader is adopted from [stweet](https://github.com/markowanga/stweet).
Participants are suggested to run the script twice to make sure each tweet is successfully crawled.

[**UPDATE**] We noticed recent changes to the Tweet policy that prevents viewing content without a logged-in account. It 
might make [stweet](https://github.com/markowanga/stweet) not work at the moment. In this case, please pull 
`src` folder and run `python get_train_dev_data_v2.py`. This code will work best with macOS-ARM/X86 and Ubuntu systems. 
If you are macOS users and have issues to run the script, please try again after install/update X-Code (`xcode-select 
--install`. Please contact the organizers if you have any other issues. 
## Citation

```
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
```

## Organizers

[Zheixong Liu](https://people.cs.pitt.edu/~zhexiong/), [Mohamed Elaraby](https://engsalem.github.io/), [Yang Zhong](http://yangzhongcs.com/), and [Diane Litman](https://people.cs.pitt.edu/~litman/) at University of
Pittsburgh.