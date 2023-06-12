#!/usr/bin/env python3

from caryle.yolov7.yolov7.utils.general import strip_optimizer
best_path = "/work1/gitlab-runner-docker-data/models/yolov7/yolov7small_tencincolstegreve_updated_may/weights/best.pt"
strip_optimizer(best_path)