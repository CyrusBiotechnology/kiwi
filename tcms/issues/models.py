from django.db import models
from dacc.authentication.models import Organization


class Project(models.Model):
    jid = models.IntegerField()
    key = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class IssueType(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    jid = models.IntegerField()
    icon_url = models.CharField(max_length=250)
    active = models.BooleanField(default=False)

    @classmethod
    def deactivate_project_issues(cls, project):
        issue_types = cls.objects.filter(project=project)
        for issue_type in issue_types:
            issue_type.active = False
            issue_type.save()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Issue(models.Model):
    jid = models.IntegerField()
    link = models.TextField()
    jira_key = models.CharField(max_length=10)
    fixVersions = models.TextField()
    summary = models.TextField()
    assignee = models.TextField(default=None)
    issue_type = models.ForeignKey(IssueType, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    iss_updated = models.DateTimeField(editable=True)
    iss_created = models.DateTimeField(editable=True)
    test_cases = models.ManyToManyField('testcases.TestCase')

    def __str__(self):
        return self.jira_key

    def get_human_url(self):
        key = self.jira_key
        base_url = Organization.objects.first().baseUrl
        return f'{base_url}/browse/{key}'

    class Meta:
        ordering = ('jira_key',)
