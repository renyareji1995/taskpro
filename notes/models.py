from django.db import models

# Create your models here.


#schema:task

#fileds:
            # title,
            # description,
            # create_date,
            # due-date,
            #category(personal,business)
            #status(pending,in-progress,done)
            #user
#step 1

class Task(models.Model):

    title=models.CharField(max_length=200)

    description=models.TextField()

    created_date=models.DateTimeField(auto_now_add=True)  #no need to give this in forms  #auto_now works updated every time changes applied,auto_now_add created date

    due_date=models.DateTimeField(null=True)

    updated_date=models.DateTimeField(auto_now=True)

    category_choices=(
        ("personal","personal"),
        ("business","business")
    )

    category=models.CharField(max_length=200,choices=category_choices,default="personal")

    status_choices=(
        ("pending","pending"),
        ("in-progress","in-progress"),
        ("done","done")
    )

    status=models.CharField(max_length=200,choices=status_choices,default="pending")

    user=models.CharField(max_length=200)

    def __str__(self) -> str:

        return self.title







