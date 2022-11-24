from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail_headless_preview.models import PagePreview
from rest_framework.response import Response


class DraftPagesAPIEndpoint(PagesAPIViewSet):
    def detail_view(self, request, pk):
        instance = self.get_object()

        if request.GET.get('draft'):
            instance = instance.get_latest_revision_as_page()
        elif not instance.live:
            raise Http404

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PagePreviewAPIViewSet(PagesAPIViewSet):
    known_query_parameters = PagesAPIViewSet.known_query_parameters.union(
        ["content_type", "token"]
    )

    def listing_view(self, request):
        page = self.get_object()
        serializer = self.get_serializer(page)
        return Response(serializer.data)

    def detail_view(self, request, pk):
        page = self.get_object()
        serializer = self.get_serializer(page)
        return Response(serializer.data)

    def get_object(self):
        app_label, model = self.request.GET["content_type"].split(".")
        content_type = ContentType.objects.get(app_label=app_label, model=model)

        page_preview = PagePreview.objects.get(
            content_type=content_type, token=self.request.GET["token"]
        )
        page = page_preview.as_page()
        if not page.pk:
            # fake primary key to stop API URL routing from complaining
            page.pk = 0

        return page
