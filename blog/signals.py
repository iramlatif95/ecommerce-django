from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment

@receiver(post_save, sender=Comment)
def notify_post_author(sender, instance, created, **kwargs):
    if created:
        post_author = instance.post.author
        commenter = instance.user
        #print(f"{commenter.username} commented on your post: {instance.post.title}")
        pass
