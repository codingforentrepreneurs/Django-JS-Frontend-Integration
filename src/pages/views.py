from django.views.generic import View
from django.shortcuts import render


class FrontendRenderView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/front-end-render.html", {})