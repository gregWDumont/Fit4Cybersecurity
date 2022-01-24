# -*- coding: utf-8 -*-

from django.urls import path

from stats import views


urlpatterns = [
    path("", views.index, name="index"),
    path("overall.json", views.overall, name="overall"),
    path(
        "survey-status-count.json",
        views.survey_status_count,
        name="survey_status_count",
    ),
    path(
        "survey-language-count.json",
        views.survey_language_count,
        name="survey_language_count",
    ),
    path(
        "answers-per-section.json",
        views.answers_per_section,
        name="answers_per_section",
    ),
]
