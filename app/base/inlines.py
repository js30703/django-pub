from nested_inline.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline


class StackedInline(NestedStackedInline):
    template = 'admin/nline/custom_stacked.html'
    extra = 0


class TabularInline(NestedTabularInline):
    template = 'admin/nline/custom_tabular.html'
    extra = 0

class ModelAdmin(NestedModelAdmin):
    pass
