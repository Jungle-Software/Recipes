import graphene
from graphene_django import DjangoObjectType
from .models import Category, Recipe


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'title')


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'description',
            'portion_size',
            'prep_time',
            'cook_time',
            'ingredients',
            'instructions',
            'additional_notes',
            'nutritional_info',
            'date_created',
        )


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    recipes = graphene.List(RecipeType)

    def resolve_recipes(root, info, **kwargs):
        # Querying a list
        return Recipe.objects.all()

    def resolve_categories(root, info, **kwargs):
        # Querying a list
        return Category.objects.all()


schema = graphene.Schema(query=Query)
