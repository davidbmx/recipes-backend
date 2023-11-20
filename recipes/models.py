from django.db import models

from utils.main_model import MainModel
from users.models import User

def upload_image(instance, filename):
    return f'recipes/{instance.user.username}/{filename}'

class Tag(MainModel):
    name = models.CharField(max_length=150)
    def __str___(self):
        return self.name

class Recipe(MainModel):
    DIFICULTY_CHOICES = (
        ('EASY', 'EASY'),
        ('MEDIUM', 'MEDIUM'),
        ('HARD', 'HARD'),
    )
    VISIBILITY_CHOICE = (
        ('PUBLIC', 'PUBLIC'),
        ('PRIVATE', 'PRIVATE'),
        ('DRAFT', 'DRAFT'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    dificulty = models.CharField(max_length=6, choices=DIFICULTY_CHOICES, default=DIFICULTY_CHOICES[0])
    prep_time = models.CharField(max_length=50)
    cook_time = models.CharField(max_length=50)
    bill_spent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    likes = models.IntegerField(default=0)
    bookmarks = models.IntegerField(default=0)
    visibility = models.CharField(max_length=7, choices=VISIBILITY_CHOICE, default=VISIBILITY_CHOICE[0])

    def __str__(self):
        return self.title
    

class Step(MainModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='instructions')
    step = models.IntegerField()
    description = models.TextField()
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.recipe

class Ingredient(MainModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    quantity = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    
    def __str__(self):
        return self.description

class ImageRecipe(MainModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=upload_image)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.image.name
    