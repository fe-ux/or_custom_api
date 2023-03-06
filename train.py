import os
os.system("python model_main_tf2.py "
          "--pipeline_config_path=models/efficientdet_d0_coco17_tpu-32/v1/pipeline.config "
          "--model_dir=my_models")
