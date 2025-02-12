from django.conf.urls import include, url
from basicviz import views

# for single-file LDA experiments
lda_single_patterns = [
    url(r'^show_docs/(?P<experiment_id>\w+)/$', views.show_docs, name='show_docs'),
    url(r'^show_doc/(?P<doc_id>\w+)/$', views.show_doc, name='show_doc'),
    url(r'^start_viz/(?P<experiment_id>\w+)/$', views.start_viz, name='start_viz'),
    url(r'^start_annotated_viz/(?P<experiment_id>\w+)/$', views.start_annotated_viz,
        name='start_annotated_viz'),
    url(r'^get_graph/(?P<vo_id>\w+)/$', views.get_graph, name='get_graph'),
    url(r'^get_doc_topics/(?P<doc_id>\w+)/$', views.get_doc_topics, name='get_doc_topics'),
    url(r'^view_parents/(?P<motif_id>\w+)/$', views.view_parents, name='get_parents'),
    url(r'^get_parents/(?P<motif_id>\w+)/(?P<vo_id>\w+)/$', views.get_parents, name='get_parents'),
    url(r'^get_parents/(?P<motif_id>\w+)/$', views.get_parents_no_vo, name='get_parents_no_vo'),
    url(r'^get_parents_metadata/(?P<motif_id>\w+)/$', views.get_parents_metadata, name='get_parents_metadata'),
    url(r'^get_all_parents_metadata/(?P<experiment_id>\w+)/$', views.get_all_parents_metadata, name='get_all_parents_metadata'),
    url(r'^view_mass2motifs/(?P<experiment_id>\w+)/$', views.view_mass2motifs,
        name='view_mass2motifs'),
    url(r'^topic_table/(?P<experiment_id>\w+)/$', views.topic_table, name='topic_table'),
    url(r'^document_pca/(?P<experiment_id>\w+)/$', views.document_pca, name='document_pca'),
    url(r'^topic_pca/(?P<experiment_id>\w+)/$', views.topic_pca, name='topic_pca'),
    url(r'^get_pca_data/(?P<experiment_id>\w+)/$', views.get_pca_data, name='get_pca_data'),
    url(r'^get_word_graph/(?P<motif_id>\w+)/(?P<vo_id>\w+)/$', views.get_word_graph,
        name='get_word_graph'),
    url(r'^get_intensity/(?P<motif_id>\w+)/(?P<vo_id>\w+)/$', views.get_intensity,
        name='get_intensity'),
    url(r'^view_word_graph/(?P<motif_id>\w+)/$', views.view_word_graph, name='view_word_graph'),
    url(r'^view_intensity/(?P<motif_id>\w+)/$', views.view_intensity, name='view_intensity'),
    url(r'^get_topic_pca_data/(?P<experiment_id>\w+)/$', views.get_topic_pca_data,
        name='get_topic_pca_data'),
    url(r'^rate_by_conserved_motif_rating/(?P<experiment_id>\w+)/$',
        views.rate_by_conserved_motif_rating, name='rate_by_conserved_motif_rating'),
    url(r'^validation/(?P<experiment_id>\w+)/$', views.validation, name='validation'),
    url(r'^toggle_dm2m/(?P<experiment_id>\w+)/(?P<dm2m_id>\w+)/$', views.toggle_dm2m,
        name='toggle_dm2m'),
    url(r'^dump_validations/(?P<experiment_id>\w+)/$', views.dump_validations,
        name='dump_validations'),
    url(r'^mass2motif_feature/(?P<fm2m_id>\w+)/$', views.mass2motif_feature,
        name='mass2motif_feature'),
    url(r'^extract_docs/(?P<experiment_id>\w+)/$', views.extract_docs, name='extract_docs'),
    url(r'^compute_topic_scores/(?P<experiment_id>\w+)/$', views.compute_topic_scores,
        name='compute_topic_scores'),
    url(r'^high_classyfire/(?P<experiment_id>\w+)/$', views.high_classyfire,
        name='high_classyfire'),    
    url(r'^get_features/(?P<experiment_id>\w+)/$',views.get_features,name = 'get_features'),
    url(r'^get_all_topics/(?P<experiment_id>\w+)/$',views.get_all_topics,name = 'get_all_topics'),
    url(r'^get_annotated_topics/(?P<experiment_id>\w+)/$',views.get_annotated_topics,name = 'get_annotated_topics'),
    url(r'^get_doc_m2m/(?P<experiment_id>\w+)/$',views.get_doc_m2m,name = 'get_doc_m2m'),
    url(r'^get_beta/(?P<experiment_id>\w+)/$',views.get_beta,name = 'get_beta'),
    url(r'^get_all_doc_data/(?P<experiment_id>\w+)/$',views.get_all_doc_data,name = 'get_all_doc_data'),
    url(r'^get_proportion_annotated_docs/(?P<experiment_id>\w+)/$',views.get_proportion_annotated_docs,name = 'get_proportion_annotation_docs'),
    url(r'^summary/(?P<experiment_id>\w+)/$',views.summary,name = 'summary'),
    url(r'^short_summary/(?P<experiment_id>\w+)/$',views.short_summary,name = 'short_summary'),
    url(r'^start_match_motifs/(?P<experiment_id>\w+)/$',views.start_match_motifs,name = 'start_match_motifs'),
    url(r'^manage_motif_matches/(?P<experiment_id>\w+)/$',views.manage_motif_matches,name = 'manage_motif_matches'),
    url(r'^add_link/(?P<from_motif_id>\w+)/(?P<to_motif_id>\w+)/$',views.add_link,name = 'add_link'),
    url(r'^remove_link/(?P<from_motif_id>\w+)/$',views.remove_link,name = 'remove_link'),
    url(r'^feature_info/(?P<feature_id>\w+)/(?P<experiment_id>\w+)/$',views.feature_info,name = 'feature_info'),
    url(r'^set_doc_annotation/$',views.set_doc_annotation,name = 'set_doc_annotation'),
    url(r'^get_doc_annotation/$',views.get_doc_annotation,name = 'get_doc_annotation'),
    url(r'^get_gnps_summary/(?P<experiment_id>\w+)/$',views.get_gnps_summary,name = 'get_gnps_summary'),
    url(r'^toggle_public/(?P<experiment_id>\w+)/$',views.toggle_public,name = 'toggle_public'),
    url(r'^delete/(?P<experiment_id>\w+)/$',views.delete_experiment,name = 'delete_experiment'),
]

# for multi-file LDA experiments
lda_multi_patterns = [
    url(r'^multi_alphas/(?P<mf_id>\w+)/$', views.multi_alphas, name='multi_alphas'),
    url(r'^alpha_pca/(?P<mf_id>\w+)/$', views.alpha_pca, name='alpha_pca'),
    url(r'^get_alpha_matrix/(?P<mf_id>\w+)/$', views.get_alpha_matrix, name='get_alpha_matrix'),
    url(r'^get_degree_matrix/(?P<mf_id>\w+)/$', views.get_degree_matrix, name='get_degree_matrix'),
    url(r'^view_multi_m2m/(?P<mf_id>\w+)/(?P<motif_name>\w+)/$', views.view_multi_m2m,
        name='view_multi_m2m'),
    url(r'^get_alphas/(?P<mf_id>\w+)/(?P<motif_name>\w+)/$', views.get_alphas, name='get_alphas'),
    url(r'^get_degrees/(?P<mf_id>\w+)/(?P<motif_name>\w+)/$', views.get_degrees, name='get_degrees'),
    url(r'^alpha_correlation/(?P<mf_id>\w+)/$', views.alpha_correlation, name='alpha_correlation'),
    url(r'^get_alpha_correlation_graph/(?P<acviz_id>\w+)/$', views.get_alpha_correlation_graph,
        name='alpha_correlation'),
    url(r'^dump_topic_molecules/(?P<m2m_id>\w+)/$', views.dump_topic_molecules,
        name='dump_topic_molecues'),
    url(r'^wipe_cache/(?P<mf_id>\w+)/$', views.wipe_cache, name='wipe_cache'),
    url(r'^get_doc_table/(?P<mf_id>\w+)/(?P<motif_name>\w+)/$', views.get_doc_table,
        name='get_doc_table'),
    url(r'^alpha_de/(?P<mfe_id>\w+)/$', views.alpha_de, name='alpha_de'),
    url(r'^get_individual_names/(?P<mf_id>\w+)/$', views.get_individual_names,
        name='get_individual_names'),
    url(r'^get_multifile_mass2motif_metadata/(?P<mf_id>\w+)/(?P<motif_name>\w+)/$',
        views.get_multifile_mass2motif_metadata, name='get_multifile_mass2motif_metadata'),
    url(r'^get_individual_ids/(?P<mf_id>\w+)/$',views.get_individual_ids,name = 'get_individual_ids'),
]

lda_admin_patterns = [
    url(r'^list_log/$',views.list_log,name = 'list_log'),
    url(r'^show_log_file/(?P<experiment_id>\w+)/$', views.show_log_file, name='show_log_file'),
]

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^', include(lda_single_patterns)),
    url(r'^', include(lda_multi_patterns)),
    url(r'^', include(lda_admin_patterns)),
]
