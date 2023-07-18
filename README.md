# ImageArg-Shared-Task-2023

## Information

Webpage: [ImageArg Shared Task](https://imagearg.github.io/)

Join Slack: [ImageArg Slack](https://join.slack.com/t/imagearg/shared_invite/zt-1ss5hdb6d-eNCaWOAEe4O_8UE1gQxIxA)

Signup
Form: *DEADLINE PASSED*

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

Please install `requirements.txt` (`pip install -r requirements.txt`) dependencies ~~and run `python get_train_dev_data.py` to download training and dev
datasets for both shared subtasks. The dataset downloader is adopted from [stweet](https://github.com/markowanga/stweet).
Participants are suggested to run the script twice to make sure each tweet is successfully crawled.~~

**[UPDATE]** The organizers noticed recent changes to the Tweet policy that prevents viewing content without a logged-in
account. It might make [stweet](https://github.com/markowanga/stweet) not work at the moment. In this case, please pull 
`plugins` folder and run `python get_train_dev_data_v2.py`. The test data is available by running `python get_test_data_v2.py`. 

**[NOTICE]** The code will work best with macOS-ARM/X86 and Ubuntu/Debian
systems with a Python 3.9 environment. If you are macOS users please install XCode (`xcode-select --install`). If you are 
Linux users please install essential build tools (`sudo apt-get install build-essential`). If
you are Windows users or have any other issues, please contact the organizers by email or 
[ImageArg Slack](https://join.slack.com/t/imagearg/shared_invite/zt-1ss5hdb6d-eNCaWOAEe4O_8UE1gQxIxA). 

## Submission
Please note organizers use email addresses and team names to identify registered teams. Please ensure to input ANY email address
you used in the registration phrase when you make a submission. If you don't remember your team names or emails 
(used in the registration phase) please contact the organizers at imagearg [at] gmail.com

We use Google From for submissions because all the other submission portals do not meet our data privacy requirement.
Participants need to read the following instruction carefully before the submission. The instruction is 
also available in the submission form.

### File Format Validation
The file should be in .csv format with a maximum of two columns: `tweet_id` and either `stance` or `persuasiveness`.
depends on subtasks.

TaskA (Stance Classification) .csv file should include:
```angular2html
tweet_id, stance
1204712613394944000, oppose
1204712613394933000, support
```
TaskB (Persuasiveness Classification) .csv file should include:
```angular2html
tweet_id, persuasiveness
1204712613394944000, yes
1204712613394933000, no
```
Please note `tweet_id` should be an integer and `stance`/`persuasiveness` should be lower cases.

### File Name Validation
The file name should be composed of the following parts:
- `team_name`: your team name
- `method_name`: please give a name to your model/method (we accept multiple methods/models you might try)
- `task_name`: shared task name (for Stance Classification the task name is "TaskA", while for Persuasiveness Classification the task name is "TaskB")
- `attempt_number`: the number of submission attempts (you can do a total of 5 submission attempts)
- No period symbol in Team_Name, Method_Name, Task_Name, and Attempt_Number.

Your file name should be like 
`{team_name}.{method_name}.{task_name}.{attempt_number}.csv`
i.e., `test-team.baseline.TaskA.1.csv`.

### Submission Form
If you are not sure your format meets the requirement please run `python check_submission_format.py <your_file_name>` to check it.
If you participated in two subtasks, you would need to submit this **[Google Form]**(https://forms.gle/pUTqU5Vc2q2K91M58) twice.

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
