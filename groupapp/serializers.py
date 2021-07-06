from rest_framework.serializers import ModelSerializer

from groupapp.models import ApplicationToNeedProfession


class ApplicationsToTeamSerializer(ModelSerializer):
    class Meta:
        model = ApplicationToNeedProfession
        fields = ['id', 'to_need_profession', 'author_application', 'description_self', 'acceptation']
