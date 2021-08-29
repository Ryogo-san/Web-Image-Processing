from django.views.generic import FormView
from django.conf import settings

import os
import shutil


class OperationView(FormView):

    def upload(self, request, Model):
        shutil.rmtree("media")
        os.mkdir("media")
        predict = Model()
        predict.image = request.FILES.get("image")
        predict.save()

    def before_operation(self, Model):
        input_img = Model.objects.order_by("-id").all()[0]
        input_img_path = str(settings.BASE_DIR)+input_img.image.url

        return input_img, input_img_path
