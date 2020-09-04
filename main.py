import loadAndPreProcess
from excecutionModule import runTest1


def main():
    print("\nHi! welcome to the program :)\n")

    path_to_images_dir = "C:/Users/royru/Downloads/spatialGeneExpression/images"
    path_to_mtx_tsv_files_dir = "C:/Users/royru/Downloads/spatialGeneExpression"
    gene_name = 'MKI67'
    stdl_ds = loadAndPreProcess.STDL_Dataset(path_to_images_dir=path_to_images_dir,
                                          path_to_mtx_tsv_files_dir=path_to_mtx_tsv_files_dir,
                                          chosen_gene_name=gene_name)

    #runTest1(stdl_ds, device !)

    print("\nGoodbye\n")
    pass






if __name__ == "__main__":
    main()