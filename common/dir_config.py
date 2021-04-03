import os

base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
test_data_dir = os.path.join(base_dir, "data")
test_case_dir = os.path.join(base_dir, "test_case")
screen_dir = os.path.join(base_dir, "output/screenshots/")
log_path = os.path.join(base_dir, "output/log/")
report_path = os.path.join(base_dir, "output/report/")
