def import_kaggle_data(data_set, extract_zip=False):

	from kaggle.api.kaggle_api_extended import KaggleApi
	from zipfile import ZipFile

	print('Download {} from kaggle.com...'.format(data_set), end='')
	api = KaggleApi()
	api.authenticate()
	api.dataset_download_file(
		dataset='benjaminperucco/udacitydata',
		file_name=data_set,
		force=True
	)

	if extract_zip:
		zf = ZipFile(data_set + '.zip')
		zf.extractall()
		zf.close()

	print('done')
