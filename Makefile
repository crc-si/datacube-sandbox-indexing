index-sentinel:
	docker-compose run indexer \
		/opt/odc/indexing/update_products.py 7 -p sent2_nrt -i 4

init:
	docker-compose run indexer \
		datacube system init