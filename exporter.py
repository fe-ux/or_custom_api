import os
os.system("python exporter_main_v2.py "
          "--pipeline_config_path=models/efficientdet_d0_coco17_tpu-32/v1/pipeline.config "
          "--trained_checkpoint_dir=my_models "
          "--output_directory=my_models/saved_model "
          "--input_type=image_tensor")