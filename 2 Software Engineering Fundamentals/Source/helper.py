def import_kaggle_data(data_set, extract_zip=False):
	"""
	Download a data_set from personal kaggle account.

	Args:
		data_set: (string) name of dataset
		extract_zip: (boolean) if dataset is stored in zip file on kaggle,
		extract locally

	Returns:
		Downloaded or extracted dataset is available on file system

	"""

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
