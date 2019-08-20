from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from models import Experiment, Document, Mass2Motif, Feature, FeatureMass2MotifInstance, VizOptions, \
    UserExperiment, ExtraUsers, MultiFileExperiment, MultiLink, Alpha, PeakSet, IntensityInstance, SystemOptions, \
    JobLog, Mass2MotifInstance
from import_export import resources


class UserExperimentAdmin(admin.ModelAdmin):
	list_display = ('experiment','user','permission')


class AlphaAdmin(ImportExportModelAdmin):
    pass


class AlphaResource(resources.ModelResource):
    class Meta:
        model = Alpha

class Mass2MotifInstanceAdmin(ImportExportModelAdmin):
    pass


class Mass2MotifInstanceResource(resources.ModelResource):
    class Meta:
        model = Mass2MotifInstance

admin.site.register(Experiment)
admin.site.register(Document)
admin.site.register(Mass2Motif)
admin.site.register(Feature)
admin.site.register(FeatureMass2MotifInstance)
admin.site.register(VizOptions)
admin.site.register(UserExperiment,UserExperimentAdmin)
admin.site.register(ExtraUsers)
admin.site.register(MultiFileExperiment)
admin.site.register(MultiLink)
admin.site.register(Alpha, AlphaAdmin)
admin.site.register(PeakSet)
admin.site.register(IntensityInstance)
admin.site.register(SystemOptions)
admin.site.register(JobLog)
admin.site.register(Mass2MotifInstance, Mass2MotifInstanceAdmin)

