import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base_app.settings')
django.setup()

from treasurehunt.models import AnswerChecker

answer = [
    "sachintendulkar", "iamironman", "zinedinezidane", "generalmotors",
    "frenchdefence", "trivedi", "australia", "area51", "humble", "hiroshima",
    "stpatricksday", "sarabhaivssarabhai", "magnuseffect", "throughawindow",
    "divinecomedy", "1016", "unlock", "28", "chardham", "valmiki"
]


def populate(N=5):
    for i in range(N):

        u = AnswerChecker.objects.get_or_create(index=i, answer=answer[i])[0]


if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("populating complete")
