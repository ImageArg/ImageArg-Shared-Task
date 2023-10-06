# ImageArg-Shared-Task-2023

## 1. Information

Webpage: [ImageArg Shared Task](https://imagearg.github.io/)

Join Slack: [ImageArg Slack](https://join.slack.com/t/imagearg/shared_invite/zt-1ss5hdb6d-eNCaWOAEe4O_8UE1gQxIxA)

Signup
Form: [Google Form (Closed)](https://docs.google.com/forms/d/e/1FAIpQLSci3TSw6ylcWnjXQsoUjh3buAQx7IdgiJwrJDR2pDHMm8DIpQ/viewform)

## 2. Introduction

There has been a recent surge of interest in developing methods and corpora to improve and evaluate persuasiveness in
natural language applications. However, these efforts have mainly focused on the textual modality, neglecting the
influence of other modalities. [Liu et al.](https://aclanthology.org/2022.argmining-1.1.pdf) introduced a new multimodal
dataset called “ImageArg” This dataset includes persuasive tweets along with associated images, aiming to identify the
image's stance towards the tweet and determine its persuasiveness score concerning a specific topic. The ImageArg
dataset is a significant step towards advancing multimodal persuasive text analysis and opens up avenues for exploring
the persuasive impact of images in social media. To further this goal, we designed this shared task, which utilizes the
ImageArg dataset to advance multimodal persuasiveness techniques.

## 3. Dataset

The dataset to download should only be used for scientific or research purposes. Any other use is explicitly prohibited. 
The datasets must not be redistributed or shared in part or full with any third party per [Twitter Developer Policy](https://developer.twitter.com/en/developer-terms/policy).
Redirect interested parties to [ImageArg](https://imagearg.github.io/) website.

All the tweets are instantly crawled from Twitter. Organizers are aware some tweets could not be available when
participants start to download (e.g., a tweet could be deleted by its author). Organizers will regularly monitor the
dataset to provide data patches that will replace invalid tweets with new annotated ones. Participants are required to
fill out
the [Google Form (Closed)](https://docs.google.com/forms/d/e/1FAIpQLSci3TSw6ylcWnjXQsoUjh3buAQx7IdgiJwrJDR2pDHMm8DIpQ/viewform)
in order to receive data patches and the shared task updates.

Please install `requirements.txt` (`pip install -r requirements.txt`) dependencies ~~and run `python get_train_dev_data.py` to download training and dev
datasets for both shared subtasks. The dataset downloader is adopted from [stweet](https://github.com/markowanga/stweet).
Participants are suggested to run the script twice to make sure each tweet is successfully crawled.~~

**[UPDATE]** The organizers noticed recent changes to the Tweet policy that prevents viewing content without a logged-in
account. It might make [stweet](https://github.com/markowanga/stweet) not work at the moment. In this case, please pull 
`plugins` folder and run `python get_train_dev_data_v2.py`. The test data (with labels) is also available by running `python get_test_data_v2.py`. 

**[NOTICE]** The code will work best with macOS-ARM/X86 and Ubuntu/Debian
systems with a Python 3.9 environment. If you are macOS users please install XCode (`xcode-select --install`). If you are 
Linux users please install essential build tools (`sudo apt-get install build-essential`). If
you are Windows users or have any other issues, please contact the organizers by email or 
[ImageArg Slack](https://join.slack.com/t/imagearg/shared_invite/zt-1ss5hdb6d-eNCaWOAEe4O_8UE1gQxIxA). 

## 4. Submission
Please note organizers use email addresses and team names to identify registered teams. Please ensure to input ANY email address
you used in the registration phrase when you make a submission. If you don't remember your team names or emails 
(used in the registration phase) please contact the organizers at imagearg [at] gmail.com

Organizers use Google From for submissions because all the other submission portals do not meet data privacy requirements.
Participants need to read the following instruction carefully before the submission. The instruction is 
also available in the submission form.

### File Format Validation
The file should be in .csv format with a maximum of two columns: `tweet_id` and either `stance` or `persuasiveness`
depends on subtasks. 

Participants need to include predictions in `abortion` and `gun control` topics in a single .csv
file regardless of their orders.

TaskA (Stance Classification) .csv file should include:
```angular2html
tweet_id, stance
1204712613394944000, oppose
1204712613394933000, support
...                , ...
```
TaskB (Persuasiveness Classification) .csv file should include:
```angular2html
tweet_id, persuasiveness
1204712613394944000, yes
1204712613394933000, no
...                , ...
```
Please note `tweet_id` should be an integer, `stance` should be either `support` or `oppose`, and `persuasiveness` should be either `yes` or `no`. All are lower cases.

### File Name Validation
The file name should be composed of the following parts:
- `team_name`: the name of participants' team
- `method_name`: the name of the model/method (we accept multiple methods/models participants might try)
- `task_name`: the name of shared task (for Stance Classification the name is `TaskA`, while for Persuasiveness Classification the name is `TaskB`)
- `attempt_number`: the number of submission attempts (participants can do a total of 5 submission for each subtask regardless of whether the same method/model or not in each submission)
- No period symbol in `team_name`, `method_name`, `task_name`, and `attempt_number`.

Your file name should be like 
`{team_name}.{method_name}.{task_name}.{attempt_number}.csv`, i.e., `test-team.baseline.TaskA.1.csv`.

### Submission Form
If you are not sure your format meets the requirement please run `python check_submission_format.py <your_file_name>` to check it.

If you participated in two subtasks, you would need to submit this **[Google Form (Closed)](https://forms.gle/pUTqU5Vc2q2K91M58)** twice.

The best score in all the submissions from the same team will be automatically used for leaderboard ranking for each subtask.
## 5. Citation
Please cite our papers if you use the data for academic purposes.
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
    
@inproceedings{liu-etal-2023-overview,
    title = "Overview of {I}mage{A}rg-2023: The First Shared Task in Multimodal Argument Mining",
    author = "Liu, Zhexiong  and Elaraby, Mohamed  and Zhong, Yang  and Litman, Diane",
    booktitle = "Proceedings of the 10th Workshop on Argument Mining",
    month = Dec,
    year = "2023",
    address = "Online and in Singapore",
    publisher = "Association for Computational Linguistics"
    }
```

## 6. Organizers

[Zheixong Liu](https://people.cs.pitt.edu/~zhexiong/), [Mohamed Elaraby](https://engsalem.github.io/), [Yang Zhong](http://yangzhongcs.com/), and [Diane Litman](https://people.cs.pitt.edu/~litman/) at University of
Pittsburgh.
