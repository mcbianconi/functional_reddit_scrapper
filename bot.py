import collections
import pickle
from pprint import pprint
import os
import praw
import praw.models

submission_file = "submission.pickle"

Submission = collections.namedtuple('Submission', [
  'fullname', 
  'url', 
  'title',
  'comments',
  'author'
])

Comment = collections.namedtuple('Comment', [
  'id', 
  'parent_id', 
  'permalink', 
  'body',
  'author'
])

Frame = collections.namedtuple('Frame', [
  'image',
  'sound'
])

def create_submition(submission: praw.models.Submission):
  return Submission(
    fullname=submission.fullname,
    url=submission.url,
    title=submission.title,
    author=submission.author.name,
    comments=fetch_comments(submission)
  )

def create_comment(comment: praw.models.Comment):
  if comment.author:
    return Comment(
      id=comment.id,
      parent_id=comment.parent_id,
      permalink=comment.permalink,
      body=comment.body,
      author= comment.author.name
    )

def fetch_comments(submission: praw.models.Submission):
  submission.comments.replace_more()
  return tuple(map(create_comment, submission.comments.list()))

def save_submission(submission_list: list):
    for submission in submission_list:
      return create_submition(submission)


def select_submission():
  reddit = praw.Reddit(
          client_id="5F-D7_H2_UjZ7Q",
          client_secret="Dcw9gR5MTPzIps6nC9YqxzJA5x4",
          user_agent="terminal:redditspeaker:1 (by /u/mcbianconi)")

  selected_submission = save_submission(reddit.front.hot(limit=5))
  with open(submission_file, "wb") as file:
    pickle.dump(selected_submission, file)

if __name__ == "__main__":

  if not os.path.exists(submission_file):
    save_submission()

  submission = None
  with open(submission_file, 'rb') as f:
    submission = pickle.load(f)


  pprint(submission)

