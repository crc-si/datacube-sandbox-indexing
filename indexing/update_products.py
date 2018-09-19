#!/usr/bin/env python3

from multiprocessing import pool
import multiprocessing
import os
import datetime
import click

from scripts.index_from_s3_bucket import iterate_datasets, add_dataset

# def iterate_datasets(bucket_name, config, prefix, suffix, func, unsafe, sources_policy):
def indexMe(prefix_suffix):
	iterate_datasets('dea-public-data', None, prefix_suffix[0], prefix_suffix[1], add_dataset, True, 'verify')

def prepare_prefix(products,num_days):

	albers_x_tiles = ['x_' + str(x) +'/' for x in range(-20, 25)]
	albers_y_tiles = ['y_' + str(y) +'/' for y in range(-37,-10)]

	fractional_cover_prefix_ls8 = 'fractional-cover/fc/v2.2.0/ls8/'
	fractional_cover_prefix_ls5 = 'fractional-cover/fc/v2.2.0/ls5/'
	WOFs_prefix = 'WOfS/WOFLs/v2.1.0/combined/'
	sentinel2_NRT_prefix = 'L2/sentinel-2-nrt/S2MSIARD/'

	#prepare date field
	start_day = datetime.datetime.now()
	end_day = datetime.datetime.now() - datetime.timedelta(days=num_days)
	delta = start_day - end_day

	dates_inbetween = [start_day - datetime.timedelta(i) for i in range((delta.days + 1))]
	prefix_suffix = []

	for case_date in dates_inbetween:
		o_day = '%02d' % (case_date.day) +'/'
		o_month = '%02d' % (case_date.month)+'/'
		o_year = str(case_date.year)+'/'
		sent_date =  str(case_date.year) + '-' + '%02d' % (case_date.month) + '-' + '%02d' % (case_date.day)+ '/'

		#sentinel workload
		if ('sent2_nrt' in products) or ('all' in products):
			prefix_suffix.append([sentinel2_NRT_prefix + sent_date, 'ARD-METADATA.yaml'])
		if ('all' in products):
			for xx in albers_x_tiles:
				for yy in albers_y_tiles:
					prefix_suffix.append([WOFs_prefix + xx + yy + o_year + o_month + o_day, '.yaml']) #look for WOFs
					prefix_suffix.append([fractional_cover_prefix_ls8 + xx + yy + o_year + o_month + o_day, '.yaml']) #look for FC8
					prefix_suffix.append([fractional_cover_prefix_ls5 + xx + yy + o_year + o_month + o_day, '.yaml']) #look for FC5

	return prefix_suffix

@click.command(help="""Enter amount of days from today that require updating.
					Optional enter products 'sent2_nrt' or 'all' append
					Optional enter amount of instances to start""")
@click.argument('num_days')
@click.option('--products', '-p', help="Pass which product 'sent2_nrt' or 'all'")
@click.option('--num_instances', '-i', help="Pass the prefix of the object to the bucket")
def main(num_days, products, num_instances):
	prefix_suffixes = prepare_prefix(products,int(num_days))

	for prefix_suffix in prefix_suffixes:
		indexMe(prefix_suffix)

if __name__ == "__main__":
    main()
