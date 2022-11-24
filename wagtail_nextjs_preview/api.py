from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet

from wagtail_nextjs_preview.views import PagePreviewAPIViewSet, DraftPagesAPIEndpoint

# Init the Wagtail Router
api_router = WagtailAPIRouter('wagtailapi')

# Register API endpoints
api_router.register_endpoint('pages', DraftPagesAPIEndpoint)
api_router.register_endpoint('page_preview', PagePreviewAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)