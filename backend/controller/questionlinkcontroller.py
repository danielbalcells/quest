from django.db import IntegrityError

from backend import models


def create_link(source, target, symmetrical=True):
    """
    Creates a QuestionLink between the source and target Questions.
    If symmetrical=True, a second QuestionLink between target and source is
    created as well.
    If the link already exists, does nothing.
    Returns the QuestionLink object.
    """
    try:
        link = models.QuestionLink(source=source, target=target)
        link.save()
        if symmetrical:
            link_back = models.QuestionLink(source=target, target=source)
            link_back.save()
        return link
    except IntegrityError:
        return models.QuestionLink.get_by_questions(source=source,
                                                    target=target)


def delete_link(source, target):
    """
    Deletes the QuestionLink between two Questions.
    """
    link = models.QuestionLink.get_by_questions(source=source, target=target)
    link.delete()


def delete_symmetrical_link(source, target):
    """
    Deletes both instances of a symmetrical link between two Questions.
    """
    delete_link(source, target)
    delete_link(target, source)


def get_by_source(source):
    """
    Gets all QuestionLink objects given a source Question
    """
    return models.QuestionLink.objects.filter(source=source)
