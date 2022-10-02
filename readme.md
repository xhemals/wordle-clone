# SPELLER (Wordle clone)
<img width="414" alt="image" src="https://user-images.githubusercontent.com/91919183/193477366-39fa0908-e5ea-4487-9aff-04941d691f96.png">

## Scoring system
The scoring system is created using a mixture of the players time, multiplied by a score based on their attempts. The max score is calculated by dividing the max score by the users time. When I create harder difficulties, this score will be higher in order to increase the score of the user

```
maxScore = 100000
scoreMultiplier = {
    6: 1.1,
    5: 1.3,
    4: 1.5,
    3: 1.9,
    2: 2.5,
    1: 5
}
score = maxScore / timeTaken
score *= scoreMultiplier[attempts]
score = round(score)
```


### Goals
- [x] ~~Create game~~
- [ ] Create GUI verion
  - [ ] Tkinter
  - [ ] Web (Django)
    - [ ] Mobile friendly
- [ ] Create longer & shorter word versions
  - [ ] 3 letter words
  - [ ] 6 letter words
- [ ] Create different modes
  - [ ] Easy (Unlimited attempts)
  - [ ] Hard (3 attempts)
  - [ ] Impossible (no colour mode)
- [ ] Scoring system
  - [x] ~~Time based score~~
  - [x] ~~Time x Attempts based score~~
  - [ ] Factor difficulty into score
  - [ ] Leaderboard for web version



