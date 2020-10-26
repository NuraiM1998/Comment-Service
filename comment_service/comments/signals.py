from django.db.models.signals import post_save
from django.dispatch import receiver
from comments.models import PostComment, CommentHierarchy


@receiver(post_save, sender=PostComment)
def save_hierarchy(sender, instance=None, created=False, **kwargs):
    print('instance: ', instance)
    print('instance.parent: ',instance.parent)
    # print('instance.child: ',instance.child)
    if created:
        self_comment = CommentHierarchy.objects.create( # текущий коммент
                                        parent=instance,
                                        child=instance)
        if instance.parent: # если у комента есть родитель
            parent_hierarchy = CommentHierarchy.objects.filter( # фильтруем родителей которые не вложенны(root)
                                                    child=instance.parent,
                                                    depth__gt=0)
            CommentHierarchy.objects.create(parent=instance.parent,
                                            child=instance,
                                            depth=1)
            for node in parent_hierarchy:
                CommentHierarchy.objects.create(
                                    parent=node.parent,
                                    child=instance,
                                    depth=node.depth+1)
                print('node: ', node)
                print('node.parent: ', node.parent)
