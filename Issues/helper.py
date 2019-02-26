STORY = 'ST'
BUG = 'BG'
EPIC = 'EP'
TASK = 'TK'

ISSUE_TYPE_CHOICES = (
    (TASK, 'Task'),
    (STORY, 'Story'),
    (BUG, 'Bug'),
    (EPIC, 'Epic'),
)

HIGHEST = 'HGH'
HIGH = 'HG'
MEDIUM = 'MD'
LOW = 'LW'
LOWEST = 'LWW'

PRIORITY_TYPE_CHOICES=(
    (HIGHEST,'Highest'),
    (HIGH,'High'),
    (MEDIUM,'Medium'),
    (LOW,'Low'),
    (LOWEST,'Lowest'),
)