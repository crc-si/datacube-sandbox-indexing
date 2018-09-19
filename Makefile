index-sentinel:
	docker-compose run indexer \
		/opt/odc/indexing/update_products.py 7 -p sent2_nrt -i 4

init:
	docker-compose run indexer \
		datacube system init

add-products:
	# docker-compose run indexer datacube product add /opt/odc/docs/config_samples/dataset_types/ls_usgs.yaml
	# docker-compose run indexer datacube product add /opt/odc/docs/config_samples/dataset_types/ga_s2_ard.yaml
	# docker-compose run indexer datacube product add /opt/odc/docs/config_samples/dataset_types/s2_granules.yaml
	docker-compose run indexer datacube product add /opt/odc/indexing/sentinel_products.yaml
