def sourcetemplate(url):
    def generation(**kwargs):
        copy_url = url
        ulr_edited = f"{copy_url}?{'&'.join([str(i) + '=' + str(j) if len(kwargs) > 1 else str(i) + '=' + str(j) for i, j in sorted(kwargs.items())])}"
        return ulr_edited if len(kwargs) else url
    return generation
