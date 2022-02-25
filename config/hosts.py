from django_hosts import patterns, host


host_patterns = patterns(
    '',
    host('office', 'config.urls.office', name='office'),
    host('survey', 'config.urls.survey', name='survey'),
    host('admin', 'config.urls.admin', name='admin'),
    
)
