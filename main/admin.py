from django.contrib import admin

from .models import MovieImage, Movie, Genre, Comment


class MovieImageInLine(admin.TabularInline):
    model = MovieImage
    max_num = 5
    min_num = 1


@admin.register(Movie)
class PostAdmin(admin.ModelAdmin):
    inlines = [MovieImageInLine, ]


admin.site.register(Genre)
admin.site.register(Comment)
# admin.site.register(MovieUserRelation)
