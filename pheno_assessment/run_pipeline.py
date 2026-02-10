from src.io import get_paths
from src.clean import clean_all_tables
from src.synth import synthesize_all_tables
from src.validate import validate_all

PROJECT_ROOT = "/Users/yizj/Desktop/HBN/pheno_assessment"

def main():
    paths = get_paths(PROJECT_ROOT)
    clean_all_tables(paths)
    synthesize_all_tables(paths)
    validate_all(paths)

if __name__ == "__main__":
    main()