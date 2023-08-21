from django.urls import path
from .views import SubjectViewRelated,SubjectGradeViewRelated,CalculatePointViewRelated


urlpatterns = [
    
    
    path('subject-list/',SubjectViewRelated.as_view(),name="SubjectList"),
    path('check-level-grade/',SubjectGradeViewRelated.as_view(),name="CheckSubjectLevel"),
    path('calculate-coa-point/',CalculatePointViewRelated.as_view(),name="CheckSubjectLevel"),

    
]