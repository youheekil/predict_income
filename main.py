"""
This script is for the ML Pipeline
"""
import argparse
import src.clean_data
import src.data
import src.train_model
import logging


def run(args):
    """
    Runnig the ML pipeline
    """
    logging.basicConfig(level=logging.INFO)

    if args.action == "all" or args.action == "data_mining":
        logging.info("DATA CLEANING HAS STARTED")
        src.clean_data.run_clean_data()

    if args.action == "all" or args.action == "predicting":
        logging.info("TRAIN/TEST MODEL PROCEDURE HAS STARTED")
        logging.info("MODEL SCORING HAS STARTED")
        src.train_model.run_train_model()



if __name__ == "__main__":
    """
    Main entrypoint
    """
    parser = argparse.ArgumentParser(description="ML training pipeline")

    parser.add_argument(
        "--action",
        type=str,
        choices=["data_mining",
                "predicting",
                "all"],
        default="all",
        help="Pipeline action"
    )

    main_args = parser.parse_args()

    run(main_args)
